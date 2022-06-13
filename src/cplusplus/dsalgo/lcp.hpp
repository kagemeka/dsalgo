#include <cassert>
#include <vector>

auto lcp_array_kasai(std::vector<int> a, std::vector<int> sa)
    -> std::vector<int> {
  int n = a.size();
  assert(n > 0 && (int)sa.size() == n);
  std::vector<int> rank(n), lcp(n - 1);
  for (int i = 0; i < n; i++) rank[sa[i]] = i;
  int h = 0;
  for (int i = 0; i < n; i++) {
    if (h > 0) --h;
    int r = rank[i];
    if (r == n - 1) continue;
    int j = sa[r + 1];
    while (i + h < n && j + h < n && a[i + h] == a[j + h]) ++h;
    lcp[r] = h;
  }
  return lcp;
}
