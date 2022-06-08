#ifndef COMBINATION_HPP
#define COMBINATION_HPP

#include "./factorial_table.hpp"
#include "./inverse_factorial_table.hpp"
#include <cstdint>
#include <vector>

template <typename S> class combination {
  std::vector<S> fact, inv_fact;

public:
  combination(unsigned long int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }
  S operator()(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    return fact[n] * inv_fact[k] * inv_fact[n - k];
  }

  S inverse(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    return inv_fact[n] * fact[k] * fact[n - k];
  }
};

#endif // COMBINATION_HPP