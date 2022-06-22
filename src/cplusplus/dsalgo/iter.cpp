#include "iter.hpp"
#include "io.hpp"

void _test_iterations() {

  rep(10) { print(_); }
  range(i, 0, 10, 2) { print(i); }

  int i = 0;
  loop {
    i += 1;
    print(i);
    if (i == 10) break;
  }
}

auto main() -> int { _test_iterations(); }
