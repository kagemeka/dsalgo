#ifndef HOMOGENEOUS_PRODUCT
#define HOMOGENEOUS_PRODUCT

#include "./combination.hpp"

template <typename S>
class homogeneous_product {
  combination<S> choose;

public:
  homogeneous_product(unsigned long int size) : choose(size) {}
  auto operator()(unsigned long int n, unsigned long int k) -> S {
    return n == 0 ? 0 : choose(n + k - 1, k);
  }
};

#endif // HOMOGENEOUS_PRODUCT
