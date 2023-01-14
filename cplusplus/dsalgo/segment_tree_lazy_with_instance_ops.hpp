#pragma once
#include "bit_length_32.hpp"
#include <cassert>
#include <vector>
using namespace std;
template<typename Ops> class lazy_segtree {
  using S = typename Ops::S;
  using F = typename Ops::F;
  Ops ops;
  vector<S> data;
  vector<F> lazy;
  auto n() -> int { return lazy.size(); }
  auto height() -> int { return bit_length(n()); }
  void merge(int i) { data[i] = ops.op(data[i << 1], data[i << 1 | 1]); }
  void apply_node(int i, F f) {
    data[i] = ops.map(f, data[i]);
    if(i < n()) lazy[i] = ops.compose(f, lazy[i]);
  }
  void propagate(int i) {
    apply_node(i << 1, lazy[i]);
    apply_node(i << 1 | 1, lazy[i]);
    lazy[i] = ops.id();
  }
  void pull(int i) {
    for(int j = height() - 1; j > 0; j--) propagate(i >> j);
  }
  void merge_above(int i) {
    for(i >>= 1; i >= 1; i >>= 1) { merge(i); }
  }

public:
  int size;
  lazy_segtree(Ops ops, int size): ops(ops), size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    data.resize(n << 1, ops.e());
    lazy.resize(n, ops.id());
  }
  auto apply(int l, int r, F f) {
    assert(0 <= l && l <= r && r <= size);
    int n = this->n();
    l += n, r += n;
    int l0 = l / (l & -l), r0 = r / (r & -r) - 1;
    pull(l0), pull(r0);
    while(l < r) {
      if(l & 1) apply_node(l++, f);
      if(r & 1) apply_node(--r, f);
      l >>= 1, r >>= 1;
    }
    merge_above(l0), merge_above(r0);
  }
  auto set(int i, S x) {
    assert(0 <= i && i < size);
    i += n();
    pull(i);
    data[i] = x;
    merge_above(i);
  }
  auto get(int l, int r) -> S {
    assert(0 <= l && l <= r && r <= size);
    int n = this->n();
    l += n, r += n;
    pull(l), pull(r - 1);
    S vl = ops.e(), vr = ops.e();
    while(l < r) {
      if(l & 1) vl = ops.op(vl, data[l++]);
      if(r & 1) vr = ops.op(data[--r], vr);
      l >>= 1, r >>= 1;
    }
    return ops.op(vl, vr);
  }
  template<typename G> auto max_right(G is_ok, int l) -> int {
    assert(l <= size);
    if(l == size) return size;
    int n = this->n();
    int i = l + n;
    S v = ops.e();
    pull(i);
    while(true) {
      i /= i & -i;
      S nv = ops.op(v, data[i]);
      if(!is_ok(nv)) break;
      v = nv;
      i++;
      if(__builtin_popcount(i) == 1) return size;
    }
    while(i < n) {
      propagate(i);
      i <<= 1;
      S nv = ops.op(v, data[i]);
      if(!is_ok(nv)) continue;
      v = nv;
      i++;
    }
    return i - n;
  }
  template<typename G> auto min_left(G is_ok, int r) -> int {
    assert(r <= size);
    if(r == 0) return 0;
    int n = this->n();
    int i = r + n;
    S v = ops.e();
    pull(i - 1);
    while(true) {
      i /= i & -i;
      S nv = ops.op(data[i - 1], v);
      if(!is_ok(nv)) break;
      v = nv;
      i--;
      if(!i || __builtin_popcount(i) == 1) return 0;
    }
    while(i < n) {
      propagate(i - 1);
      i <<= 1;
      S nv = ops.op(data[i - 1], v);
      if(!is_ok(nv)) continue;
      v = nv;
      i--;
    }
    return i - n;
  }
};
// RARS
struct Ops {
  using S = pair<long, int>;
  using F = long;
  auto op(const S& a, const S& b) -> S {
    return {a.first + b.first, a.second + b.second};
  }
  auto e() -> S { return {0, 0}; }
  auto compose(const F& a, const F& b) -> F { return a + b; }
  auto id() -> F { return 0; }
  auto map(F const& f, S const& x) -> S {
    return {x.first + f * x.second, x.second};
  }
};
