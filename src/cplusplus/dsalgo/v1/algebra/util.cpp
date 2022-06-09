#include <bits/stdc++.h>
using namespace std;


namespace Algebra {

template<typename T>
T pow(const T& x, const T& n) {
  if (!n) {return 1;}
  T y = pow(x, n>>1);
  y *= y;
  if (n&1) y *= x;
  return y;
}

template<typename T>
int bit_length(T n) {
  int length = 0;
  while (n) {
    n >>= 1;
    length++;
  };
  return length;
}

template<typename T>
int bit_count(T n) {
  int cnt = 0;
  int l = bit_length(n);
  for (int i = 0; i < l; i++) {
    cnt += n & 1;
    n >>= 1;
  };
  return cnt;
}

}
using namespace Algebra;
