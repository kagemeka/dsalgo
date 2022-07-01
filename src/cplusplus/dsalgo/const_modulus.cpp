
#include "const_modulus.hpp"
#include <iostream>
auto main() -> int {
  using namespace std;
  using mod = const_modulus<int, 1000000007>;
  cout << mod::get() << endl;
}