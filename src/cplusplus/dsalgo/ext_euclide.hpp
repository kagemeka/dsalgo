
template <typename T>
auto mgi(T m, T n) -> std::pair<T, T> {
  // extended euclidean modular-gcd and inverse
  // return pair(g: gcd(m, n), x: inverse(n / g) \mod (m / g))
  assert(0 < n && n < m);
  i64 a = n, b = m;
  i64 x00 = 1, x01 = 0;
  while (b) {
    x00 -= a / b * x01;
    std::swap(x00, x01);
    a %= b;
    std::swap(a, b);
  }
  T u = m / a;
  if (x00 < 0) x00 += u;
  assert(0 <= x00 && (T)x00 < u);
  return {a, x00};
}