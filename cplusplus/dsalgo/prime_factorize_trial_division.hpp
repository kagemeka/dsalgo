#pragma once
#include <vector>
using namespace std;
template<typename T> auto prime_factorize(T n) -> vector<pair<T, int>> {
  vector<pair<T, int>> factors;
  for (T i = 2; i * i <= n; i++) {
    if (n % i)
      continue;
    int cnt = 0;
    while (n % i == 0) {
      cnt++;
      n /= i;
    }
    factors.emplace_back(i, cnt);
  }
  if (n != 1)
    factors.emplace_back(n, 1);
  return factors;
}
