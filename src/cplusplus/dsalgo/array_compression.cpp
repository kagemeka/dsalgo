#include "array_compression.hpp"
#include <iostream>

void _test_compress() {
  using namespace std;
  auto a = vector<int>{1, 4, 3, 4, 5, 6, 7, 8, 9, 10};
  auto f = array_compression<int>(a);

  auto i = f(7);
  cout << i << endl;
  cout << f[i] << endl;
  // print(compress<u32>::once(a));
}

auto main() -> int { _test_compress(); }
