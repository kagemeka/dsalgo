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
    for(int j = 1; j < height(); j++) update(i >> j);
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
    l += n, r += r;
    pull(l), pull(r - 1);
    int l0 = l, r0 = r;
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
    pull(l), pull(r);
    S vl = sg.e(), vr = sg.e();
    while(l < r) {
      if(l & 1) vl = sg.op(vl, data[l++]);
      if(r & 1) vr = sg.op(data[--r], vr);
      l >>= 1, r >>= 1;
    }
    return sg.op(vl, vr);
  }
};
