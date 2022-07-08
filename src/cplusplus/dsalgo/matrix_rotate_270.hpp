#include "matrix_transpose.hpp"
template<typename A> auto rot270(A a) -> A {
  a = transpose(a);
  reverse(a.begin(), a.end());
  return a;
}