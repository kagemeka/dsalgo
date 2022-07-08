#include "iteration_macro.hpp"
#include "types.hpp"
template<typename A> auto lc_substr_dp(const A& a, const A& b)
  -> vec<vec<int>> {
  int n = a.size(), m = b.size();
  vec<vec<int>> dp(n + 1, vec<int>(m + 1));
  range(i, n) range(j, m) dp[i + 1][j + 1] = a[i] == a[j] ? dp[i][j] + 1 : 0;
  return dp;
}