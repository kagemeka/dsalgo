#include <bits/stdc++.h>
using namespace std;


namespace Algebra {

template<typename T>
vector<vector<T>> identity(
  int n
) {
  vector<vector<T>> e(
    n,
    vector<T>(n)
  );
  for (int i = 0; i < n; i++) {
    e[i][i] = 1;
  }
  return e;
}


template<typename T>
vector<vector<T>> matrix_dot(
  const vector<vector<T>>& a,
  const vector<vector<T>>& b
) {
  int h0 = (int)a.size();
  int w0 = (int)a[0].size();
  int h1 = (int)b.size();
  int w1 = (int)b[0].size();
  assert(w0 == h1);
  vector<vector<T>> c(
    h0,
    vector<T>(w1)
  );
  for (int i = 0; i < h0; i++)
  {
    for (
      int j = 0; j < w1; j++
    ) {
      for (
        int k = 0; k < h1; k++
      ) {
        c[i][j] +=
          a[i][k] * b[k][j];
      }
    }
  }
  return c;
}


template<typename T>
vector<vector<T>> matrix_pow(
  const vector<vector<T>>& a,
  long long n
) {
  if (!n) {
    int m = (int)a.size();
    return identity<T>(m);
  }
  auto b = matrix_pow(a, n>>1);
  b = matrix_dot(b, b);
  if (n&1) b = matrix_dot(b, a);
  return b;
}

}
