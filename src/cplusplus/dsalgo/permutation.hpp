#include "factorial_table.hpp"
#include "inverse_factorial_table.hpp"
#include <cassert>

template<typename S> class permutation {
  std::vector<S> fact, inv_fact;

public:
  permutation(int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }

  auto operator()(int n, int k) -> S {
    if(k < 0 || n < k) return 0;
    return fact[n] * inv_fact[n - k];
  }

  auto inv(int n, int k) -> S {
    assert(0 <= k && k <= n);
    return inv_fact[n] * fact[n - k];
  }
};
