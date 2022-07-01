#pragma once
#include "combination.hpp"

template <typename S>
class homogeneous_product {
  combination<S> choose;

public:
  homogeneous_product(int size) : choose(size) {}
  auto operator()(int n, int k) -> S { return choose(n + k - 1, k); }
};
