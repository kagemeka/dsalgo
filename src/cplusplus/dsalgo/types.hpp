#pragma once
#include <cstdint>
#include <functional>

using namespace std;

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
using usize = size_t;
using isize = make_signed<usize>::type;
using f32 = float;
using f64 = double;
using f128 = __float128;

template <typename T>
using vec = vector<T>;

template <typename T>
using fn = function<T>;
