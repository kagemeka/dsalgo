#include "z_algorithm_findall_substr.hpp"
// #include <bits/stdc++.h>
#include <iostream>
#include <string>

auto main() -> int {
  std::string s = "ababababc", t = "aba";
  auto ind = z_algorithm_findall_substr(s, t);
  for (auto i : ind) {
    std::cout << i << '\n';
  }
}
