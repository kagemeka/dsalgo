#include "assign.hpp"
#include "cassert"
#include "io.hpp"

auto _test_chmin() -> void {
  int x = 10, y = 2;
  chmin(x, y);
  assert(x == 2);
  _passed("chmin");
}

auto main() -> int { _test_chmin(); }
