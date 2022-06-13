#include "rust_types.hpp"

#ifndef BIT_LENGTH_HPP // use filename as the identifier.
#define BIT_LENGTH_HPP
#pragma once

namespace dsalgo::bit_length {
using namespace rust_types;

auto bit_length(u32 x) -> u8 { return 32 - __builtin_clz(x); }

auto bit_length(u64 x) -> u8 { return 64 - __builtin_clzll(x); }

auto bit_length(u128 x) -> u8 {
  return x >> 64 == 0 ? bit_length((u64)x) : bit_length((u64)(x >> 64)) + 64;
}

} // namespace dsalgo::bit_length

#endif
