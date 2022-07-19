// TODO:
#include "kagemeka/algebra/abstract/structure.cpp"
#include <cassert>
#include <functional>
#include <iostream>
#include <vector>
template<typename S, typename F> struct SegmentTreeLazyConfig {
  Monoid<S> s;
  Monoid<F> f;
  std::function<S(F, S)> map;
};
template<typename S, typename F> class SegmentTreeLazy {
private:
  using C = SegmentTreeLazyConfig<S, F>;
  C c;
  int size, n, h;
  std::vector<S> data;
  std::vector<F> lazy;
  void merge(int i) { data[i] = c.s.op(data[i << 1], data[i << 1 | 1]); }
  void apply(int i, F f) {
    data[i] = c.map(f, data[i]);
    if(i < n) lazy[i] = c.f.op(f, lazy[i]);
  }
  void propagate(int i) {
    apply(i << 1, lazy[i]);
    apply(i << 1 | 1, lazy[i]);
    lazy[i] = c.f.e();
  }

public:
  SegmentTreeLazy(C c, std::vector<S> const& a): c(c), size((int)a.size()) {
    n = 1 << bit_length(size - 1);
    h = bit_length(n);
    data = std::vector<S>(n << 1, c.s.e());
    for(int i = 0; i < size; i++) data[n + i] = a[i];
    lazy = std::vector<F>(n, c.f.e());
    for(int i = n - 1; i > 0; --i) merge(i);
  }
  SegmentTreeLazy(C c, int n): SegmentTreeLazy(c, std::vector<S>(n, c.s.e())) {}
  void set(int l, int r, F f) {
    assert(0 <= l && l <= r && r <= size);
    l += n;
    r += n;
    for(int i = h; i > -1; --i) {
      if((l >> i) << i != l) propagate(l >> i);
      if((r >> i) << i != r) propagate((r - 1) >> i);
    }
    int l0 = l, r0 = r;
    while(l < r) {
      if(l & 1) apply(l++, f);
      if(r & 1) apply(--r, f);
      l >>= 1;
      r >>= 1;
    }
    l = l0, r = r0;
    for(int i = 1; i < h + 1; i++) {
      if((l >> i) << i != l) merge(l >> i);
      if((r >> i) << i != r) merge((r - 1) >> i);
    }
  }
  auto get(int l, int r) -> S {
    assert(0 <= l && l <= r && r <= size);
    l += n;
    r += n;
    for(int i = h; i > -1; --i) {
      if((l >> i) << i != l) propagate(l >> i);
      if((r >> i) << i != r) propagate((r - 1) >> i);
    }
    S vl = c.s.e(), vr = c.s.e();
    while(l < r) {
      if(l & 1) vl = c.s.op(vl, data[l++]);
      if(r & 1) vr = c.s.op(data[--r], vr);
      l >>= 1;
      r >>= 1;
    }
    return c.s.op(vl, vr);
  }
  void update(int i, S x) {
    assert(0 <= i && i < size);
    i += n;
    for(int j = h; j > -1; j--) propagate(i >> j);
    data[i] = x;
    for(int j = 1; j < h + 1; j++) merge(i >> j);
  }
};
