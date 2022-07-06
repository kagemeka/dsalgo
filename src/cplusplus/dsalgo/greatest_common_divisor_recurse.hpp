#pragma once

template<typename T> auto gcd(T a, T b) -> T { return !b ? a : gcd(b, a % b); }
