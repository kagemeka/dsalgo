#include <bits/stdc++.h>
using namespace std; 


namespace NumberTheory {


template<typename T>
vector<T> find_divisors(T n) {
  vector<T> d(0);
  for (T i = 1; i*i <= n; i++)
  {
    if (n%i) {continue;} 
    d.push_back(i);
    if (i*i != n) {
      d.push_back(n/i);
    }
  }
  sort(d.begin(), d.end());
  return d;
}

}

using namespace NumberTheory;