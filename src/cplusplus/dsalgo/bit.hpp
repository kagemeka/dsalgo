
template <typename T>
int bit_length(const T &n) {
  int l = 0;
  while (1LL << l <= n) l++;
  return l;
}

template <typename T>
int bit_count(T n) {
  int cnt = 0;
  while (n) {cnt += n & 1; n >>= 1;}
  return cnt; 
}