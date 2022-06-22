#include "bit.hpp"
#include "io.hpp"

auto main() -> int {
  // assert(bit::len::clz((u128)1 << 100) == 101);
  // assert(msb(1) == 0);
  print(clz((u32)1));
  print(clz((u64)1));
  print(clz((u128)1));
  print(bitlen((u128)1 << 100));
  print(popcnt((u128)1 << 100 | 1));
  print(ctz((u128)0)); // this != 128 -> c++'s bug.
  print(ctz((u128)1));

  _passed("bit");
}
