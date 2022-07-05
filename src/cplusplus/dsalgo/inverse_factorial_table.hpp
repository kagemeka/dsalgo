#include "factorial_table.hpp"

template<typename S> auto inverse_factorial_table(int size) -> std::vector<S> {
  using namespace std;
  vector<S> a(size);
  iota(a.begin(), a.end(), 1);
  a[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  for(int i = size - 1; i > 0; --i) a[i - 1] *= a[i];
  return a;
}
