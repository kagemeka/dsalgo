#include "fenwick_tree_additive.hpp"
class fw_multiset {
  fenwick<int> fw;

public:
  fw_multiset(int less_than): fw(less_than) {}
  auto size() -> int { return fw.get(fw.size()); }
  auto count(int x) -> int { return fw.get(x + 1) - fw.get(x); }
  auto insert(int x, int count = 1) { fw.operate(x, count); }
  auto remove(int x, int count = 1) { fw.operate(x, -count); }
  auto lower_bound(int x) -> int { return fw.get(x); }
  auto upper_bound(int x) -> int { return fw.get(x + 1); }
  auto operator[](int i) -> int {
    return fw.max_right([&](int x) { return x <= i; });
  }
};
