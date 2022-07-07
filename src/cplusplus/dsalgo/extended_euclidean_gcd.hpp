#include <tuple>
using namespace std;
template<typename T> auto extgcd(T a, T b) -> tuple<T, T, T> {
  T x00 = 1, x01 = 0, x10 = 0, x11 = 1;
  while(b != 0) {
    T q = a / b;
    a %= b, swap(a, b);
    x00 -= q * x01, swap(x00, x01);
    x10 -= q * x11, swap(x10, x11);
  }
  return {a, x00, x10};
}
