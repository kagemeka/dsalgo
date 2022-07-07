#pragma once
#include "factorial_table.hpp"
#include "inverse_factorial_table.hpp"
#include <cassert>
template<typename S> class factorial_tables_frequent_ops {
  std::vector<S> fact, inv_fact;

public:
  factorial_tables_frequent_ops(int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }
  auto p(int n, int k) -> S {
    if(k < 0 || n < k) return 0;
    return fact[n] * inv_fact[n - k];
  }
  auto c(int n, int k) -> S { return p(n, k) * inv_fact[k]; }
  auto h(int n, int k) -> S { return c(n - 1 + k, k); };
  auto inv(int n) -> S { return fact[n - 1] * inv_fact[n]; }
  auto inv_p(int n, int k) -> S {
    assert(0 <= k && k <= n);
    return inv_fact[n] * fact[n - k];
  }
  auto inv_c(int n, int k) -> S { return inv_p(n, k) * fact[k]; }
};
