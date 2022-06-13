#ifndef ACCUMULATE_HPP
#define ACCUMULATE_HPP

#include <vector>

template <typename S, S (*op)(S, S)>
auto accumulate(std::vector<S> v) -> std::vector<S> {
  for (int i = 0; i < (int)v.size(); ++i) {
    v[i + 1] = op(v[i], v[i + 1]);
  }
  return v;
}
#endif // ACCUMULATE_HPP
