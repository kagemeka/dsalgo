#pragma once
#include <vector>
using namespace std;
template<typename A> auto morris_pratt(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lb(n); // longest border
  for(int i = 1, d = 0; i < n; i++) {
    while(d != 0 && a[d] != a[i]) d = lb[d - 1];
    d += a[d] == a[i];
    lb[i] = d;
  }
  return lb;
}
