
#pragma once
#include "bit_array.hpp"
// because it's essentially same as bit array

// #include <vector>
// using namespace std;

// class bit_vector {
//   constexpr static int K = 6;
//   constexpr static int M = (1 << K) - 1;

//   vector<ulong> d;
//   using Self = bit_vector;

// public:
//   bit_vector(): bit_vector(0) {}

//   bit_vector(int size): d((size + M) >> K) {}

//   auto operator[](int i) -> int { return d[i >> K] >> (i & M) & 1; }

//   void set(int i, int value) {
//     if((*this)[i] != value) flip(i);
//   }

//   void flip(int i) { d[i >> K] ^= 1ul << (i & M); }

//   auto operator&(Self const& rhs) -> Self {
//     Self res(*this);
//     int n = min(res.d.size(), rhs.d.size());
//     for(int i = 0; i < n; i++) { res.d[i] &= rhs.d[i]; }
//     return res;
//   }

//   auto popcount() -> int {
//     int cnt = 0;
//     for(auto& x: d) { cnt += __builtin_popcountll(x); }
//     return cnt;
//   }
// };
