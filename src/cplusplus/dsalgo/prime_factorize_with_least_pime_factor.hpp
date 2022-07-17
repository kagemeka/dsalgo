#include "least_prime_factor_with_sieve_of_eratosthenes.hpp"
struct prime_factorize_with_lpf {
  vector<int> lpf;
  prime_factorize_with_lpf(int size): lpf(least_prime_factor(size)) {}
  auto factorize(int n) -> vector<pair<int, int>> {
    vector<pair<int, int>> factors;
    int prime = 0, cnt = 0;
    while(n > 1) {
      int p = lpf[n];
      n /= p;
      if(p == prime) {
        cnt++;
        continue;
      }
      if(cnt > 0) factors.emplace_back(prime, cnt);
      prime = p, cnt = 1;
    }
    if(cnt > 0) factors.emplace_back(prime, cnt);
    return factors;
  }
};