#pragma once
#include <vector>
using namespace std;

template<typename T> auto find_divisors(T n) -> vector<T> {
  vector<T> d(0);
  for(T i = 1; i * i <= n; i++) {
    if(n % i) { continue; }
    d.push_back(i);
    if(i * i != n) { d.push_back(n / i); }
  }
  sort(d.begin(), d.end());
  return d;
}
