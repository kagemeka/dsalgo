#pragma once
#include "array_compression.hpp"
#include "fenwick_tree_additive.hpp"
template<typename T, typename A> auto inversion_number(const A& a) -> long {
  auto b = array_compression<T>::once(a);
  int n = a.size();
  fenwick<int> fw(n);
  long cnt = 0;
  for(int i = n - 1; i >= 0; i--) {
    cnt += fw.get(a[i]);
    fw.operate(a[i], 1);
  }
  return cnt;
}
