#pragma once
#include "types.hpp"
#include <iostream>

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

const auto _print_colored(std::string s, int c = 0) {
  printf("\033[%dm%s\n\033[0m", c, s.c_str());
}

const auto _passed(std::string s = "") { _print_colored("passed! " + s, 32); }

#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif

namespace fastio {}