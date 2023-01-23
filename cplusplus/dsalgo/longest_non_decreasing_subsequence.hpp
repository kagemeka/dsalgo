#pragma once
#include <vector>
using namespace std;
template<typename T, typename A>
auto longest_non_decreasing_subsequence(const T &inf, const A &a) -> vector<T> {
  int n = a.size();
  vector<T> dp(n, inf);
  for (auto &x: a) *upper_bound(dp.begin(), dp.end(), x) = x;
  return vector(dp.begin(), lower_bound(dp.begin(), dp.end(), inf));
}
