#include "sieve_of_eratosthenes_enumerate_primes.hpp"
auto least_prime_factor(int size) -> vector<int> {
  vector<int> lpf(size);
  for(auto p: enumerate_primes(size)) lpf[p] = p;
  for(int i = 4; i < size; i += 2) lpf[i] = 2;
  for(int i = 3; i * i < size; i += 2) {
    if(lpf[i] != i) continue;
    for(int j = i * i; j < size; j += i << 1) {
      if(lpf[j] == 0) lpf[j] = i;
    }
  }
  return lpf;
}
