#pragma once
#include "array_unique.hpp"
#include <cassert>
#include <vector>

template <typename T>
class array_compression {
  std::vector<T> values;

public:
  template <typename A>
  array_compression(A a) {
    values = unique(std::vector<T>(a.begin(), a.end()));
  }

  auto operator()(T x) -> int {
    int i = std::lower_bound(values.begin(), values.end(), x) - values.begin();
    assert(i < (int)values.size() && values[i] == x);
    return i;
  }

  auto operator[](int i) const -> T { return values[i]; }

  template <typename A>
  auto static once(A a) -> std::vector<int> {
    auto f = array_compression(a);
    std::vector<int> indices(a.size());
    for (int i = 0; i < (int)a.size(); ++i) indices[i] = f(a[i]);
    return indices;
  }
};
