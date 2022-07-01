
template <typename F, typename A>
auto accumulate(F f, A a) -> A {
  for (int i = 0; i < (int)a.size(); ++i) {
    a[i + 1] = f(a[i], a[i + 1]);
  }
  return a;
}

template <typename S, S (*f)(S, S), typename A>
auto accumulate(A a) -> A {
  return accumulate(f, a);
}
