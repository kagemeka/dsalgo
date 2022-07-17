#pragma once
#include <vector>
using namespace std;
template<typename T> auto prime_factorize(T n) -> vector<pair<int, int>> {
  vector<pair<int, int>> factors;
  for(int i = 2; i < n; i++) {
    if(i * i > n) break;
    if(n % i) continue;
    int cnt = 0;
    while(n % i == 0) {
      cnt++;
      n /= i;
    }
    factors.emplace_back(i, cnt);
  }
  if(n != 1) factors.emplace_back(n, 1);
  return factors;
}