#pragma once
#include <vector>

using std::vector;

template<typename A> auto kmp_table(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> f(n, 0); // failure function
  for(int i = 1, d = 0; i < n; ++i) {
    while(d != 0 && a[d] != a[i]) d = f[d - 1];
    if(a[d] == a[i]) ++d;
    f[i] = d > 0 && i + 1 < n && a[d] == a[i + 1] ? f[d - 1] : d;
  }
  return f;
}
