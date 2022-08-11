#include "iteration_macro.hpp"
#include "types.hpp"
auto sa_is(vector<int> a) -> vector<int> {
  int mn = *min_element(a.begin(), a.end());
  int n = a.size();
  rep(i, n) a[i] = a[i] - mn + 1;
  a.push_back(0);
  ++n;
  int m = *max_element(a.begin(), a.end()) + 1;
  vector<bool> is_s(n, true), is_lms(n);
  vector<int> lms;
  lms.reserve(n);
  rep_rev(i, n - 1) {
    is_s[i] = a[i] != a[i + 1] ? a[i] < a[i + 1] : is_s[i + 1];
    is_lms[i + 1] = !is_s[i] && is_s[i + 1];
    if(is_lms[i + 1]) lms.push_back(i + 1);
  }
  reverse(lms.begin(), lms.end());
  vector<int> arg_l(m + 1), arg_r(m);
  iter(x, a) {
    arg_r[x]++;
    arg_l[x + 1]++;
  }
  rep(i, m - 1) {
    arg_l[i + 1] += arg_l[i];
    arg_r[i + 1] += arg_r[i];
  }
  auto induce = [&]() -> vector<int> {
    vector<int> sa(n, -1);
    auto arg = arg_r;
    rep_rev(i, lms.size()) sa[--arg[a[lms[i]]]] = lms[i];
    arg = arg_l;
    rep(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && !is_s[i]) sa[arg[a[i]]++] = i;
    }
    arg = arg_r;
    rep_rev(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && is_s[i]) sa[--arg[a[i]]] = i;
    }
    return sa;
  };
  vector<int> sa = induce(), lms_idx, rank(n, -1);
  lms_idx.reserve(n);
  iter(i, sa) if(is_lms[i]) lms_idx.push_back(i);
  int l = lms_idx.size();
  int r = 0;
  rank[n - 1] = r;
  rep(i, l - 1) {
    int j = lms_idx[i], k = lms_idx[i + 1];
    rep(d, n) {
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
  vector<int> lms_order;
  if(r == l - 1) {
    lms_order.resize(l);
    rep(i, l) lms_order[rank[i]] = i;
  } else {
    lms_order = sa_is(rank);
  }
  rep(i, l) lms_idx[i] = lms[lms_order[i]];
  swap(lms, lms_idx);
  sa = induce();
  return {sa.begin() + 1, sa.end()};
}
