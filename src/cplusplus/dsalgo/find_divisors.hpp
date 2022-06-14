// TODO:
#pragma once
#include "./rust_types.hpp"

namespace dsalgo::find_divisors_naive {
  using namespace rust_types;

  template <typename T>
  auto find_divisors(T n) -> vec<T> {
    vec<T> d(0);
    for (T i = 1; i * i <= n; i++) {
      if (n % i) {
        continue;
      }
      d.push_back(i);
      if (i * i != n) {
        d.push_back(n / i);
      }
    }
    sort(d.begin(), d.end());
    return d;
  }

} // namespace dsalgo::find_divisors_naive
