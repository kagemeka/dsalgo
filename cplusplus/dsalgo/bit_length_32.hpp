#pragma once
auto bit_length(int n) -> int { return 32 - __builtin_clz(n); }
