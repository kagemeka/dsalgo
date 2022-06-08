#ifndef CACHED_PASCAL_TRIANGLE_HPP
#define CACHED_PASCAL_TRIANGLE_HPP

#include <unordered_map>

template <typename T> class cached_pascal_triangle {
  std::unordered_map<unsigned long long int, T> cache;

public:
  cached_pascal_triangle() {}

  T operator()(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    if (k == 0) return 1;
    unsigned long long int key = (unsigned long long int)n << 32 | k;
    if (cache.count(key) == 0) {
      cache[key] = (*this)(n - 1, k - 1) + (*this)(n - 1, k);
    }
    return cache[key];
  }
};

#endif // CACHED_PASCAL_TRIANGLE_HPP
