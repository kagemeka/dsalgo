#include <tuple>
using namespace std;
template<typename T> auto extgcd(T a, T b) -> tuple<T, T, T> {
  if (b == 0) {
    return {a, 1, 0};
  }
  auto [g, x, y] = extgcd(b, a % b);
  return {g, y, x - a / b * y};
}
