
#ifndef DSALGO_DEBUG_PRINT_HPP // use filename as the identifier.
#define DSALGO_DEBUG_PRINT_HPP

#pragma once

#include "rust_types.hpp"
#include <iostream>

namespace dsalgo::debug_print {
  using namespace rust_types;

  template <typename T>
  void print(vec<T> v) {
    for (usize i = 0; i < v.size(); ++i) {
      std::cout << v[i] << " \n"[i == v.size() - 1];
    }
  }

  template <typename T>
  void print(const T& t) {
    std::cout << t << '\n';
  }

  template <typename T, typename... U>
  void print(const T& t, const U&... args) {
    std::cout << t << ' ';
    print(args...);
  }

  template <typename T, typename... U>
  void print(char sep, const T& t, const U&... args) {
    if (sizeof...(args) > 0) {
      std::cout << t << sep;
      print(sep, args...);
    } else {
      print(t);
    }
  }

#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif

} // namespace dsalgo::debug_print

namespace dsalgo::debug_print::tests {

  void test_debug() {
    int a = 0, b = 2, c = 3;
    debug(a, b, c);

    vec<int> v{1, 2, 3, 4, 5};
    debug(v);
    debug(a, v);
    usize d = 0;
    print(d);
  }

} // namespace dsalgo::debug_print::tests

#endif
