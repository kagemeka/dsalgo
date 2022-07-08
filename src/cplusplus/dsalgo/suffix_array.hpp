// TODO:
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
std::vector<int> sa_doubling(std::vector<int> a) {
  int n = a.size();
  ArrayCompression<int> ac;
  std::vector<int> rank = ac.compress(a);
  int k = 1;
  std::vector<long long> key(n);
  std::vector<int> sa(n);
  while(true) {
    for(int i = 0; i < n; i++) {
      key[i] = (long long)rank[i] << 30;
      if(i + k < n) key[i] |= 1 + rank[i + k];
    }
    std::iota(sa.begin(), sa.end(), 0);
    std::sort(sa.begin(), sa.end(), [&](int i, int j) {
      return key[i] < key[j];
    });
    rank[sa[0]] = 0;
    for(int i = 0; i < n - 1; i++) {
      rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]]);
    }
    k <<= 1;
    if(k >= n) break;
  }
  return sa;
}
std::vector<int> sa_doubling_countsort(std::vector<int> a) {
  int n = a.size();
  std::vector<int> cnt(n + 2);
  std::function<std::vector<int>(std::vector<int>)> counting_sort_key;
  counting_sort_key = [&](std::vector<int> const& a) -> std::vector<int> {
    std::fill(cnt.begin(), cnt.end(), 0);
    for(const int& x: a) cnt[x + 1]++;
    for(int i = 0; i < n; i++) cnt[i + 1] += cnt[i];
    std::vector<int> key(n);
    for(int i = 0; i < n; i++) key[cnt[a[i]]++] = i;
    return key;
  };
  std::vector<int> rank, first(n), second(n), sa(n);
  ArrayCompression<int> ac;
  rank = ac.compress(a);
  int k = 1;
  std::vector<long long> key(n);
  while(true) {
    for(int i = 0; i < n; i++) second[i] = i + k < n ? 1 + rank[i + k] : 0;
    std::vector<int> rank_second = counting_sort_key(second);
    for(int i = 0; i < n; i++) first[i] = rank[rank_second[i]];
    std::vector<int> rank_first = counting_sort_key(first);
    for(int i = 0; i < n; i++) sa[i] = rank_second[rank_first[i]];
    for(int i = 0; i < n; i++) {
      key[i] = (long long)first[rank_first[i]] << 30 | second[sa[i]];
    }
    rank[sa[0]] = 0;
    for(int i = 0; i < n - 1; i++) {
      rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i]);
    }
    k <<= 1;
    if(k >= n) break;
  }
  return sa;
}
