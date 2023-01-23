#pragma once
#include <set>
using namespace std;
template<typename T> class median_queue {
  multiset<T> lo, hi;
  auto balance() -> int { return (int)lo.size() - (int)hi.size(); }
  auto rebalance() {
    int b = balance();
    if (b == 2) {
      auto p = --lo.end();
      hi.insert(*p);
      lo.erase(p);
    } else if (b == -1) {
      auto p = hi.begin();
      lo.insert(*p);
      hi.erase(p);
    }
  }

public:
  median_queue() = default;
  auto size() -> int { return lo.size() + hi.size(); }
  auto count(T &x) -> int { return lo.count(x) + hi.count(x); }
  auto insert(T x) {
    if (balance() == 1)
      lo.insert(x);
    else
      hi.insert(x);
    rebalance();
  }
  auto low() -> T { return *lo.rbegin(); }
  auto high() -> T { return balance() == 1 ? low() : *hi.begin(); }
  auto remove(T &x) {
    assert(count(x));
    auto p = lo.find(x);
    if (p != lo.end())
      lo.erase(p);
    else
      hi.erase(hi.find(x));
    rebalance();
  }
};
