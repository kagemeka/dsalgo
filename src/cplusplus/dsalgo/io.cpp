#include "io.hpp"

void _test_debug() {
  int a = 0, b = 2, c = 3;
  debug(a, b, c);

  vec<int> v{1, 2, 3, 4, 5};
  debug(v);
  debug(a, v);
  usize d = 0;
  print(d);
}

auto main() -> int { _test_debug(); }
