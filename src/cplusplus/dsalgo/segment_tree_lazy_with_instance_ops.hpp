#pragma once
#include "bit_length_32.hpp"
#include <cassert>
#include <vector>
using namespace std;
template<typename Sg, typename Fg, typename Map> class lazy_segtree {
  using S = typename Sg::T;
  using F = typename Fg::T;
  Sg sg;
  Fg fg;
  Map map;
  vector<S> data;
  vector<F> lazy;
  int _size;
  auto n() -> int { return lazy.size(); }
  auto height() -> int { return bit_length(n()); }
  void update(int i) { data[i] = sg.op(data[i << 1], data[i << 1 | 1]); }
  void apply_node(int i, F f) {
    data[i] = map(f, data[i]);
    if(i < n()) lazy[i] = fg.op(f, lazy[i]);
  }
  void propagate(int i) {
    apply_node(i << 1, lazy[i]);
    apply_node(i << 1 | 1, lazy[i]);
    lazy[i] = fg.e();
  }
  void pull(int i) {
    for(int j = height() - 1; j > 0; j--) propagate(i >> j);
  }
  void update_above(int i) {
    for(i >>= 1; i >= 1; i >>= 1) { update(i); }
  }

public:
  lazy_segtree(Sg sg, Fg fg, Map map, int size)
    : sg(sg), fg(fg), map(map), _size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    data.resize(n << 1, sg.e());
    lazy.resize(n, fg.e());
  }
  auto size() -> int { return _size; }
  auto apply(int l, int r, F f) {
    assert(0 <= l && l <= r && r <= size());
    int n = this->n();
    l += n, r += n;
    int l0 = l / (l & -l), r0 = r / (r & -r) - 1;
    pull(l0), pull(r0);
    while(l < r) {
      if(l & 1) apply_node(l++, f);
      if(r & 1) apply_node(--r, f);
      l >>= 1, r >>= 1;
    }
    update_above(l0), update_above(r0);
  }
  auto set(int i, S x) {
    assert(0 <= i && i < size());
    i += n();
    pull(i);
    data[i] = x;
    update_above(i);
  }
  auto get(int l, int r) -> S {
    assert(0 <= l && l <= r && r <= size());
    int n = this->n();
    l += n, r += n;
    pull(l), pull(r - 1);
    S vl = sg.e(), vr = sg.e();
    while(l < r) {
      if(l & 1) vl = sg.op(vl, data[l++]);
      if(r & 1) vr = sg.op(data[--r], vr);
      l >>= 1, r >>= 1;
    }
    return sg.op(vl, vr);
  }
  template<typename G> auto max_right(G is_ok, int l) -> int {
    assert(l <= size());
    if(l == size()) return size();
    int n = this->n();
    int i = l + n;
    S v = sg.e();
    pull(i);
    while(true) {
      i /= i & -i;
      S nv = sg.op(v, data[i]);
      if(!is_ok(nv)) break;
      v = nv;
      i++;
      if(__builtin_popcount(i) == 1) return size();
    }
    while(i < n) {
      propagate(i);
      i <<= 1;
      S nv = sg.op(v, data[i]);
      if(!is_ok(nv)) continue;
      v = nv;
      i++;
    }
    return i - n;
  }
  template<typename G> auto min_left(G is_ok, int r) -> int {
    assert(r <= size());
    if(r == 0) return 0;
    int n = this->n();
    int i = r + n;
    S v = sg.e();
    pull(i - 1);
    while(true) {
      i /= i & -i;
      S nv = sg.op(data[i - 1], v);
      if(!is_ok(nv)) break;
      v = nv;
      i--;
      if(!i || __builtin_popcount(i) == 1) return 0;
    }
    while(i < n) {
      propagate(i - 1);
      i <<= 1;
      S nv = sg.op(data[i - 1], v);
      if(!is_ok(nv)) continue;
      v = nv;
      i--;
    }
    return i - n;
  }
};
// RARS
struct Sg {
  using T = pair<long, int>;
  auto op(const T& a, const T& b) -> T {
    return {a.first + b.first, a.second + b.second};
  }
  auto e() -> T { return {0, 0}; }
};
struct Fg {
  using T = long;
  auto op(const T& a, const T& b) -> T { return a + b; }
  auto e() -> T { return 0; }
};
auto map_(Fg::T const& f, Sg::T const& x) -> Sg::T {
  return {x.first + f * x.second, x.second};
}