#pragma once
#include <set>
using namespace std;
template<typename T> class median_queue {
  using Self = median_queue;
  multiset<T> lo_set, hi_set;

public:
  median_queue() = default;
  [[nodiscard]] auto size() const -> int {
    return lo_set.size() + hi_set.size();
  }
  auto top() -> T { return *lo_set.rbegin(); }
  auto insert(T x) {
    if(size() & 1) {
      lo_set.insert(x);
      auto ptr = --lo_set.end();
      x = *ptr;
      lo_set.erase(ptr);
      hi_set.insert(x);
    } else {
      hi_set.insert(x);
      auto ptr = hi_set.begin();
      x = *ptr;
      hi_set.erase(ptr);
      lo_set.insert(x);
    }
  }
};
