#pragma once
#include <vector>
using namespace std;
constexpr long mod = 1000000007;
auto mod_pow(long n, long k) -> long {
  if(k == 0) return 1;
  long y = mod_pow(n, k >> 1);
  y = y * y % mod;
  if(k & 1) y = y * n % mod;
  return y;
}
auto inv(long n) -> long { return mod_pow(n, mod - 2); }
vector<long> fact{1};
vector<long> ifact{1};
auto choose(int n, int k) -> long {
  if(k < 0 || n < k) return 0;
  while((int)fact.size() <= n) {
    fact.push_back(*(fact.end() - 1) * (long)fact.size() % mod);
    ifact.push_back(inv(*(fact.end() - 1)));
  }
  return fact[n] * ifact[n - k] % mod * ifact[k] % mod;
}
