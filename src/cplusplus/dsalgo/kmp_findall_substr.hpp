#pragma once
#include "kmp_table_0_indexed.hpp"
using namespace std;

template <typename A>
auto kmp_findall(const A& a, const A& pattern) -> vector<int> {
  const auto& p = pattern;
  int n = a.size(), m = p.size();
  auto f = kmp_table(p);
  vector<int> indices;
  for (int i = 0, j = 0; i < n; ++i) {
    while (j != 0 && p[j] != a[i]) j = f[j - 1];
    if (p[j] == a[i]) ++j;
    if (j == m) {
      indices.push_back(i + 1 - m);
      j = f[m - 1];
    }
  }
  return indices;
}
