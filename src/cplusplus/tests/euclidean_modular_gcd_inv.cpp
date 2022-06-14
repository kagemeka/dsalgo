#include "../dsalgo/extended_euclidean_modular_gcd_inv.hpp"
#include <gtest/gtest.h>

// (test_name, case_name)
TEST(euclidean_modular_gcd_inv, test) {
  using namespace dsalgo::euclidean_modular_gcd_inv;
  auto [gcd, x] = euclidean_mod_gcd_inv(15, 10);
  EXPECT_EQ(gcd, 4);
}
