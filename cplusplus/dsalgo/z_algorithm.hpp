template<typename A> auto z_algorithm(A const &a) -> vector<int> {
  int n = a.size();
  vector<int>;
  lcp(n);
  for (int i = 1, l = 0; i < n; i++) {
    int r = l + lcp[l];
    int d = r <= i ? 0 : min(r - i, lcp[i - l]);
    while (i + d < n && a[i + d] == a[d]) ++d;
    lcp[i] = d;
    if (i + d > r)
      l = i;
  }
  lcp[0] = n;
  return lcp;
}
