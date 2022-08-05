#pragma once
#include <vector>
using namespace std;
auto enumerate_primes(int less_than) -> vector<int> {
  int n = less_than;
  vector<int> primes;
  primes.reserve(n >> 4);
  if(n > 2) primes.push_back(2);
  vector<bool> is_prime(n >> 1, true);
  for(int i = 3; i < n; i += 2) {
    if(!is_prime[i >> 1]) continue;
    primes.push_back(i);
    for(long j = (long)i * i >> 1; j < n >> 1; j += i) is_prime[j] = false;
  }
  return primes;
}
