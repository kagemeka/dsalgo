#pragma once
#include <algorithm>
#include <vector>
using namespace std;
template<typename A> auto z_algorithm(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lcp(n, 0);
  for(int i = 1, l = 0; i < n; ++i) {
    auto r = l + lcp[l];
    auto d = r <= i ? 0 : min(lcp[i - l], r - i);
    while(i + d < n && a[i + d] == a[d]) ++d;
    lcp[i] = d;
    if(r < i + d) l = i;
  }
  lcp[0] = n;
  return lcp;
}
