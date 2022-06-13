#pragma once

#include <cstdint>
#include <type_traits>
#include <vector>

namespace dsalgo {
namespace rust_types {
using u8 = uint8_t;
using u16 = uint16_t;
using u32 = uint32_t;
using u64 = uint64_t;
using u128 = __uint128_t;
using i8 = int8_t;
using i16 = int16_t;
using i32 = int32_t;
using i64 = int64_t;
using i128 = __int128_t;
using usize = std::size_t;
using isize = std::make_signed<std::size_t>::type;
using f32 = float;
using f64 = double;
using f128 = __float128;

template <typename T>
using vec = std::vector<T>;

} // namespace rust_types
} // namespace dsalgo
