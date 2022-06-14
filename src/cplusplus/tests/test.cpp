#include "../dsalgo/debug_print.hpp"
#include "../dsalgo/extended_euclidean_modular_gcd_inv.hpp"
auto main() -> int {
  std::cout.setstate(std::ios::failbit); // /dev/null
  std::cout.clear(); // reset failbit
  dsalgo::debug_print::tests::test_debug();
  using namespace dsalgo::euclidean_modular_gcd_inv;
  auto [gcd, x] = euclidean_mod_gcd_inv(15, 10);
  std::cout << gcd << ' ' << x << '\n';
  assert(gcd != 5);
}
