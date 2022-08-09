#include "iteration_macro.hpp"
#include <array>
#include <cassert>
using namespace std;
template<typename T, int n> struct matrix {
  using Self = matrix;
  array<array<T, n>, n> data;
  matrix() { rep(i, n) data[i].fill(0); }
  matrix(int x) {
    assert(x == 0 || x == 1);
    if(x) { rep(i, n) data[i][i] = 1; }
  }
  auto operator[](int i) -> array<T, n>& { return data[i]; }
  auto operator*(Self& rhs) -> Self {
    Self a;
    rep(i, n) rep(k, n) rep(j, n) a[i][j] += data[i][k] * rhs[k][j];
    return a;
  }
  auto operator*=(Self& rhs) { *this = *this * rhs; }
  auto operator+(Self& rhs) -> Self {
    Self a(*this);
    rep(i, n) rep(j, n) a[i][j] += rhs[i][j];
    return a;
  }
  auto operator+=(Self& rhs) { *this = *this + rhs; }
};
