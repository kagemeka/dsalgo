#pragma once
#include <vector>
using namespace std;
// able to compute at most 2^k th from any node in O(k) time.
auto functional_graph_doubling_table(vector<int> const& f, int k)
  -> vector<vector<int>> {
  int n = f.size();
  vector<vector<int>> a(k + 1);
  a[0] = f;
  for(int i = 0; i < k; i++) {
    vector<int> b(n);
    for(int j = 0; j < n; j++) { b[j] = a[i][a[i][j]]; }
    a[i + 1] = b;
  }
  return a;
}
