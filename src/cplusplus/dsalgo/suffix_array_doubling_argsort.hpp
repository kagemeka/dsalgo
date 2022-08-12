#pragma once
#include "iteration_macro.hpp"
#include <numeric>
#include <vector>
using namespace std;
auto suffix_array(vector<int> const& s) -> vector<int> {
  int n = s.size();
  vector<long> a(n);
  rep(i, n) a[i] = s[i];
  vector<int> sa(n);
  iota(sa.begin(), sa.end(), 0);
  int d = 1;
  while(true) {
    rep(i, n) a[i] = a[i] << 30 | (i + d < n ? 1 + a[i + d] : 0);
    sort(sa.begin(), sa.end(), [&](int i, int j) { return a[i] < a[j]; });
    d <<= 1;
    if(d >= n) break;
    int rank = 0;
    long prev = a[sa[0]];
    for(auto& i: sa) {
      if(a[i] > prev) {
        rank++;
        prev = a[i];
      }
      a[i] = rank;
    }
    if(rank == n) break;
  }
  return sa;
}
