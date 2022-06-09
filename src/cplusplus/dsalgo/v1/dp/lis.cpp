#include <bits/stdc++.h>
using namespace std;


template<typename T>
vector<T>
longest_increasing_seq(
  const vector<T>& a
) {
  vector<T> lis(
    a.size(),
    numeric_limits<T>::max()
  );
  for (const T& x: a) {
    *lower_bound(
      lis.begin(),
      lis.end(),
      x
    ) = x;
  }
  return lis;
}
