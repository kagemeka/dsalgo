#include "iteration_macro.hpp"
#include "types.hpp"
auto sa_is(vec<int> a) -> vec<int> {
  int mn = *min_element(a.begin(), a.end());
  int n = a.size();
  range(i, n) a[i] = a[i] - mn + 1;
  a.push_back(0);
  ++n;
  int m = *max_element(a.begin(), a.end()) + 1;
  vec<bool> is_s(n, true), is_lms(n);
  vec<int> lms;
  lms.reserve(n);
  range_rev(i, n - 1) {
    is_s[i] = a[i] != a[i + 1] ? a[i] < a[i + 1] : is_s[i + 1];
    is_lms[i + 1] = !is_s[i] && is_s[i + 1];
    if(is_lms[i + 1]) lms.push_back(i + 1);
  }
  reverse(lms.begin(), lms.end());
  vec<int> bucket(m);
  iter(x, a) bucket[x]++;
  auto induce = [&]() -> vec<int> {
    vec<int> sa(n, -1);
    vec<int> sa_idx(m);
    copy(bucket.begin(), bucket.end(), sa_idx.begin());
    range(i, m - 1) sa_idx[i + 1] += sa_idx[i];
    range_rev(i, lms.size()) sa[--sa_idx[a[lms[i]]]] = lms[i];
    copy(bucket.begin(), bucket.end(), sa_idx.begin());
    int s = 0;
    range(i, m) {
      sa_idx[i] += s;
      swap(s, sa_idx[i]);
    }
    range(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && !is_s[i]) sa[sa_idx[a[i]]++] = i;
    }
    copy(bucket.begin(), bucket.end(), sa_idx.begin());
    range(i, m - 1) sa_idx[i + 1] += sa_idx[i];
    range_rev(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && is_s[i]) sa[--sa_idx[a[i]]] = i;
    }
    return sa;
  };
  vec<int> sa = induce(), lms_idx, rank(n, -1);
  lms_idx.reserve(n);
  iter(i, sa) if(is_lms[i]) lms_idx.push_back(i);
  int l = lms_idx.size();
  int r = 0;
  rank[n - 1] = r;
  range(i, l - 1) {
    int j = lms_idx[i], k = lms_idx[i + 1];
    range(d, n) {
      if(a[j + d] != a[k + d]) {
        ++r;
        break;
      }
      if(d > 0 && is_lms[j + d]) {
        r += !is_lms[k + d];
        break;
      }
    }
    rank[k] = r;
  }
  rank.erase(
    remove_if(rank.begin(), rank.end(), [](int x) { return x < 0; }), rank.end()
  );
  vec<int> lms_order;
  if(r == l - 1) {
    lms_order.resize(l);
    range(i, l) lms_order[rank[i]] = i;
  } else {
    lms_order = sa_is(rank);
  }
  range(i, l) lms_idx[i] = lms[lms_order[i]];
  swap(lms, lms_idx);
  sa = induce();
  return {sa.begin() + 1, sa.end()};
}
