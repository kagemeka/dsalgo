#pragma once

#include <iostream>
using namespace std;

auto const _print_colored(string s, int c = 0) {
  printf("\033[%dm%s\n\033[0m", c, s.c_str());
}

auto const _passed(string s = "") { _print_colored("passed! " + s, 32); }
