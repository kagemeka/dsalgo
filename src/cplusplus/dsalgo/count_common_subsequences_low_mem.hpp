#pragma once
#include <vector>
using namespace std;

template<typename T, typename A>
auto count_common_subsequences(const A& a, const A& b) -> T {
  int n = a.size(), m = b.size();
  vector<T> dp(m + 1, 1);
  for(int i = 0; i < n; i++) {
    for(int j = m - 1; j >= 0; j--) { dp[j + 1] -= dp[j] * (a[i] != b[j]); }
    for(int j = 0; j < m; j++) { dp[j + 1] += dp[j]; }
  }
  return dp[m];
}
