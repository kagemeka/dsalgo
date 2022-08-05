#include "matrix_transpose.hpp"
template<typename A> auto rot90(A a) -> A {
  reverse(a.begin(), a.end());
  return transpose(a);
}
