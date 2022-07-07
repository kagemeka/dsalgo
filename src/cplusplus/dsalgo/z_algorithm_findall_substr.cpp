#include "z_algorithm_findall_substr.hpp"
#include <iostream>
#include <string>

auto main() -> int {
  std::string s = "ababababc", t = "aba";
  for(auto i: findall_substr(s, t)) { std::cout << i << '\n'; }
}
