
template <typename T>
auto bit_length(const T& n) -> int {
  int l = 0;
  while (1LL << l <= n) l++;
  return l;
}

template <typename T>
auto bit_count(T n) -> int {
  int cnt = 0;
  while (n) {
    cnt += n & 1;
    n >>= 1;
  }
  return cnt;
}
