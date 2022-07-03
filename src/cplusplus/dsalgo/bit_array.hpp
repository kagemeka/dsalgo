#pragma once

#include <vector>
using namespace std;

class bit_array {
  constexpr static int K = 6;
  constexpr static int M = (1 << K) - 1;

  vector<ulong> d;
  using Self = bit_array;

public:
  bit_array() : bit_array(0) {}

  bit_array(int size) : d((size + M) >> K) {}

  auto operator[](int i) -> int { return d[i >> K] >> (i & M) & 1; }

  void set(int i, int value) {
    if ((*this)[i] != value) flip(i);
  }

  void flip(int i) { d[i >> K] ^= 1ul << (i & M); }

  auto operator&(const Self& rhs) -> Self {
    Self res(*this);
    int n = min(res.d.size(), rhs.d.size());
    for (int i = 0; i < n; i++) {
      res.d[i] &= rhs.d[i];
    }
    return res;
  }

  auto popcount() -> int {
    int cnt = 0;
    for (auto& x : d) {
      cnt += __builtin_popcountll(x);
    }
    return cnt;
  }
};
