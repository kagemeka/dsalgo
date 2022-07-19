#pragma once
#include <vector>
using namespace std;
auto find_divisors(long n) -> vector<long> {
  vector<long> d(0);
  for(long i = 1; i * i <= n; i++) {
    if(n % i) { continue; }
    d.push_back(i);
    if(i * i != n) { d.push_back(n / i); }
  }
  sort(d.begin(), d.end());
  return d;
}
