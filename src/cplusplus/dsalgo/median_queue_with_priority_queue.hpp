#pragma once
#include <queue>
using namespace std;

template<typename T> class median_queue {
  using Self = median_queue;
  priority_queue<T> lo_que;
  priority_queue<T, vector<T>, greater<T>> hi_que;

public:
  median_queue() = default;

  [[nodiscard]] auto size() const -> int {
    return lo_que.size() + hi_que.size();
  }

  auto top() -> T { return lo_que.top(); }

  auto push(T x) {
    if(size() & 1) {
      lo_que.push(x);
      hi_que.push(lo_que.top());
      lo_que.pop();
    } else {
      hi_que.push(x);
      lo_que.push(hi_que.top());
      hi_que.pop();
    }
  }

  auto pop() {
    lo_que.pop();
    if(size() & 1) {
      lo_que.push(hi_que.top());
      hi_que.pop();
    }
  }
};
