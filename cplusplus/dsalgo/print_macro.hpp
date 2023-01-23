#pragma once
#include <array>
#include <iostream>
#include <vector>
using namespace std;
template<typename T> void print(vector<T> v) {
  for (int i = 0; i < (int)v.size(); ++i) {
    cout << v[i] << " \n"[i == (int)v.size() - 1];
  }
}
template<typename T, unsigned long N> void print(array<T, N> v) {
  for (unsigned long i = 0; i < N; ++i) { cout << v[i] << " \n"[i == N - 1]; }
}
template<typename T> void print(const T &v) { cout << v << '\n'; }
template<typename T, typename... U> void print(const T &t, const U &...args) {
  cout << t << ' ';
  print(args...);
}
template<typename T, typename... U>
void print(char sep, const T &t, const U &...args) {
  if (sizeof...(args) > 0) {
    cout << t << sep;
    print(sep, args...);
  } else {
    print(t);
  }
}
