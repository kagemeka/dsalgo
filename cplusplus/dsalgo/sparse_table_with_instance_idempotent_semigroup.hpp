
#pragma once
#include "bit_length_32.hpp"
#include <functional>
#include <vector>
using namespace std;
template<typename T, class F = function<T(const T&, const T&)>>
class sparse_table {
  vector<vector<T>> data;
  F f;

public:
  sparse_table(vector<T> const& a, const F& f): f(f) {
    int n = a.size();
    if(!n) return;
    int height = bit_length(n - 1);
    data.resize(height);
    data[0] = a;
    for(int i = 1; i < height; i++) {
      int w = n - (1 << i) + 1;
      data[i].resize(w);
      for(int j = 0; j < w; j++) {
        data[i][j] = f(data[i - 1][j], data[i - 1][j + (1 << (i - 1))]);
      }
    }
  }
  auto size() -> int { return data[0].size(); }
  auto get(int l, int r) -> T {
    assert(0 <= l && l < r && r <= size());
    if(r - l == 1) return data[0][l];
    int i = bit_length(r - l - 1) - 1;
    return f(data[i][l], data[i][r - (1 << i)]);
  }
};
