#pragma once
#include <array>
using namespace std;
template<int N> class bit_array {
  constexpr static int K = 6;
  constexpr static int M = (1 << K) - 1;
  constexpr static int n = (N + M) >> K;
  array<long, n> d;
  using Self = bit_array;

public:
  auto operator[](int i) const -> bool { return d[i >> K] >> (i & M) & 1; }
  void set(int i, bool value) {
    if ((*this)[i] != value)
      flip(i);
  }
  void flip(int i) { d[i >> K] ^= 1ul << (i & M); }
  auto operator|(Self const &rhs) const -> Self {
    Self res(*this);
    for (int i = 0; i < n; i++) { res.d[i] |= rhs.d[i]; }
    return res;
  }
  auto operator&(Self const &rhs) const -> Self {
    Self res(*this);
    for (int i = 0; i < n; i++) { res.d[i] &= rhs.d[i]; }
    return res;
  }
  [[nodiscard]] auto popcount() const -> int {
    int cnt = 0;
    for (auto &x: d) { cnt += __builtin_popcountll(x); }
    return cnt;
  }
};
