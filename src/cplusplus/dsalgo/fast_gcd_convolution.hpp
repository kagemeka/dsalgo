#pragma once
#include "sieve_of_eratosthenes_enumerate_primes.hpp"
#include <vector>
using namespace std;
template<typename T> auto zeta(vector<T> f) -> vector<T> {
  int n = f.size() - 1;
  for(auto& p: enumerate_primes(n + 1)) {
    for(int i = n / p; i >= 1; i--) { f[i] += f[i * p]; }
  }
  return f;
};
template<typename T> auto mobius(vector<T> f) -> vector<T> {
  int n = f.size() - 1;
  for(auto& p: enumerate_primes(n + 1)) {
    for(int i = 1; i <= n / p; i++) { f[i] -= f[i * p]; }
  }
  return f;
};
template<typename T> auto convolve(vector<T> f, vector<T> g) -> vector<T> {
  f = zeta(f);
  g = zeta(g);
  for(int i = 0; i < (int)f.size(); i++) { f[i] *= g[i]; }
  return mobius(f);
};