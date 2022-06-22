template <typename T, typename A>
auto lower(A a, T x) -> usize {
  return std::lower_bound(entire(a), x) - a.begin();
}

template <typename T, typename A>
auto upper(A a, T x) -> usize {
  return std::upper_bound(entire(a), x) - a.begin();
}
