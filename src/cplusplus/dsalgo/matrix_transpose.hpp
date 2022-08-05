#pragma once
#include <vector>
using namespace std;
template<typename T, typename A> auto transpose(A const& a)
  -> vector<vector<T>> {
  int n = a.size(), m = a[0].size();
  vector<vector<T>> b(m, vector<T>(n));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) b[j][i] = a[i][j];
  }
  return b;
}
