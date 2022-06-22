#pragma once
#include "./factorial_table.hpp"
#include "./inverse_factorial_table.hpp"
#include <cstdint>
#include <vector>

template <typename S>
class combination {
  std::vector<S> f, if_;

public:
  combination(usize n) {
    f = factorials<S>(n);
    if_ = inv_factorials<S>(n);
  }
  auto operator()(usize n, usize k) -> S {
    if (n < k) return 0;
    return f[n] * if_[k] * if_[n - k];
  }

  auto inv(usize n, usize k) -> S {
    assert(k <= n);
    return if_[n] * f[k] * if_[n - k];
  }
};

template <typename S>
class homogeneous_product {
  combination<S> choose;

public:
  homogeneous_product(usize size) : choose(size) {}
  auto operator()(usize n, usize k) -> S {
    return n == 0 ? 0 : choose(n + k - 1, k);
  }
};
