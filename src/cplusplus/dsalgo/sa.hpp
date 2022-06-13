// TODO:

#include "kagemeka/std/array_compression.cpp"
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>

std::vector<int> sa_is(std::vector<int> a) {
  int mn = *std::min_element(a.begin(), a.end());
  int n = a.size();
  for (int i = 0; i < n; i++) a[i] = a[i] - mn + 1;
  a.push_back(0);
  ++n;
  int m = *std::max_element(a.begin(), a.end()) + 1;
  std::vector<bool> is_s(n, true), is_lms(n);
  std::vector<int> lms;
  lms.reserve(n);
  for (int i = n - 1; i > 0; i--) {
    is_s[i - 1] = a[i - 1] == a[i] ? is_s[i] : a[i - 1] < a[i];
    is_lms[i] = !is_s[i - 1] && is_s[i];
    if (is_lms[i]) lms.push_back(i);
  }
  std::reverse(lms.begin(), lms.end());
  std::vector<int> bucket(m);
  for (const int& x : a) bucket[x]++;

  std::function<std::vector<int>()> induce = [&]() -> std::vector<int> {
    std::vector<int> sa(n, -1);
    std::vector<int> sa_idx(m);
    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    for (int i = 0; i < m - 1; i++) sa_idx[i + 1] += sa_idx[i];
    for (int i = lms.size() - 1; i > -1; i--) sa[--sa_idx[a[lms[i]]]] = lms[i];

    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    int s = 0;
    for (int i = 0; i < m; i++) {
      sa_idx[i] += s;
      std::swap(s, sa_idx[i]);
    }
    for (int j = 0; j < n; j++) {
      int i = sa[j] - 1;
      if (i >= 0 && !is_s[i]) sa[sa_idx[a[i]]++] = i;
    }

    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    for (int i = 0; i < m - 1; i++) sa_idx[i + 1] += sa_idx[i];
    for (int j = n - 1; j > -1; j--) {
      int i = sa[j] - 1;
      if (i >= 0 && is_s[i]) sa[--sa_idx[a[i]]] = i;
    }
    return sa;
  };

  std::vector<int> sa = induce(), lms_idx, rank(n, -1);
  lms_idx.reserve(n);
  for (const int& i : sa)
    if (is_lms[i]) lms_idx.push_back(i);
  int l = lms_idx.size();
  int r = 0;
  rank[n - 1] = r;
  for (int i = 0; i < l - 1; i++) {
    int j = lms_idx[i], k = lms_idx[i + 1];
    for (int d = 0; d < n; d++) {
      bool j_is_lms = is_lms[j + d], k_is_lms = is_lms[k + d];
      if (a[j + d] != a[k + d] || j_is_lms ^ k_is_lms) {
        ++r;
        break;
      }
      if (d > 0 && j_is_lms | k_is_lms) break;
    }
    rank[k] = r;
  }
  rank.erase(
      std::remove_if(rank.begin(), rank.end(), [](int x) { return x < 0; }),
      rank.end());
  std::vector<int> lms_order;
  if (r == l - 1) {
    lms_order.resize(l);
    for (int i = 0; i < l; i++) lms_order[rank[i]] = i;
  } else {
    lms_order = sa_is(rank);
  }
  std::vector<int> buf(l);
  for (int i = 0; i < l; i++) buf[i] = lms[lms_order[i]];
  swap(lms, buf);
  sa = induce();
  return std::vector<int>(sa.begin() + 1, sa.end());
}

std::vector<int> sa_doubling(std::vector<int> a) {
  int n = a.size();
  ArrayCompression<int> ac;
  std::vector<int> rank = ac.compress(a);
  int k = 1;
  std::vector<long long> key(n);
  std::vector<int> sa(n);
  while (true) {
    for (int i = 0; i < n; i++) {
      key[i] = (long long)rank[i] << 30;
      if (i + k < n) key[i] |= 1 + rank[i + k];
    }
    std::iota(sa.begin(), sa.end(), 0);
    std::sort(sa.begin(), sa.end(),
              [&](int i, int j) { return key[i] < key[j]; });
    rank[sa[0]] = 0;
    for (int i = 0; i < n - 1; i++) {
      rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]]);
    }
    k <<= 1;
    if (k >= n) break;
  }
  return sa;
}

std::vector<int> sa_doubling_countsort(std::vector<int> a) {
  int n = a.size();
  std::vector<int> cnt(n + 2);
  std::function<std::vector<int>(std::vector<int>)> counting_sort_key;
  counting_sort_key = [&](const std::vector<int>& a) -> std::vector<int> {
    std::fill(cnt.begin(), cnt.end(), 0);
    for (const int& x : a) cnt[x + 1]++;
    for (int i = 0; i < n; i++) cnt[i + 1] += cnt[i];
    std::vector<int> key(n);
    for (int i = 0; i < n; i++) key[cnt[a[i]]++] = i;
    return key;
  };
  std::vector<int> rank, first(n), second(n), sa(n);
  ArrayCompression<int> ac;
  rank = ac.compress(a);
  int k = 1;
  std::vector<long long> key(n);
  while (true) {
    for (int i = 0; i < n; i++) second[i] = i + k < n ? 1 + rank[i + k] : 0;
    std::vector<int> rank_second = counting_sort_key(second);
    for (int i = 0; i < n; i++) first[i] = rank[rank_second[i]];
    std::vector<int> rank_first = counting_sort_key(first);
    for (int i = 0; i < n; i++) sa[i] = rank_second[rank_first[i]];
    for (int i = 0; i < n; i++) {
      key[i] = (long long)first[rank_first[i]] << 30 | second[sa[i]];
    }
    rank[sa[0]] = 0;
    for (int i = 0; i < n - 1; i++) {
      rank[sa[i + 1]] = rank[sa[i]] + (key[i + 1] > key[i]);
    }
    k <<= 1;
    if (k >= n) break;
  }
  return sa;
}
