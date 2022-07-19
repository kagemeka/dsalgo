#pragma once
#include "bit_length_32.hpp"
#include <cassert>
#include <vector>
using namespace std;
template<typename T, typename G> class segtree {
  vector<T> data;
  G g;
  auto update(int i) { data[i] = g.op(data[i << 1], data[i << 1 | 1]); }
  auto n() -> int { return data.size() >> 1; }

public:
  int size;
  segtree(G g, int size): g(g), size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    data.resize(n << 1, g.e());
  }
  auto set(int i, T x) {
    assert(0 <= i && i < size);
    for(data[i += n()] = x, i >>= 1; i >= 1; i >>= 1) update(i);
  }
  auto operator[](int i) -> T { return data[i + n()]; }
  auto operator[](pair<int, int> lr) -> T {
    auto [l, r] = lr;
    assert(0 <= l && l <= r && r <= size);
    T vl = g.e(), vr = g.e();
    l += n();
    r += n();
    while(l < r) {
      if(l & 1) vl = g.op(vl, data[l++]);
      if(r & 1) vr = g.op(data[--r], vr);
      l >>= 1;
      r >>= 1;
    }
    return g.op(vl, vr);
  }
  template<typename F> auto max_right(F f, int l) const -> int {
    assert(0 <= l && l <= size);
    if(l == size) return size;
    T v = g.e();
    int i = l + n();
    while(true) {
      i /= i & -i;
      T nv = g.op(v, data[i]);
      if(!f(nv)) break;
      v = nv;
      i++;
      if(__builtin_popcount(i) == 1) return size;
    }
    while(i < n()) {
      i <<= 1;
      T nv = g.op(v, data[i]);
      if(!f(nv)) continue;
      v = nv;
      i++;
    }
    return i - n();
  }
  template<typename F> auto min_left(F f, int r) const -> int {
    assert(0 <= r && r <= size);
    if(r == 0) return 0;
    T v = g.e();
    int i = r + n();
    while(true) {
      i /= i & -i;
      T nv = g.op(data[i - 1], v);
      if(!f(nv)) break;
      i--;
      v = nv;
      if(__builtin_popcount(i) == 1) return 0;
    }
    while(i < n()) {
      i <<= 1;
      T nv = g.op(data[i - 1], v);
      if(!f(nv)) continue;
      i--;
      v = nv;
    }
    return i - n();
  }
};
