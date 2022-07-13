#include <cassert>
#include <vector>
using namespace std;
auto lcp_array(vector<int> a, vector<int> sa) -> vector<int> {
  int n = a.size();
  assert(n > 0 && (int)sa.size() == n);
  vector<int> rank(n), lcp(n - 1);
  for(int i = 0; i < n; i++) rank[sa[i]] = i;
  int h = 0;
  for(int i = 0; i < n; i++) {
    if(h > 0) --h;
    int r = rank[i];
    if(r == n - 1) continue;
    for(int j = sa[r + 1]; max(i, j) + h < n && a[i + h] == a[j + h]; ++h)
      ;
    lcp[r] = h;
  }
  return lcp;
}