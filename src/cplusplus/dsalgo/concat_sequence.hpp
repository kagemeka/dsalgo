#pragma once

namespace concat_sequence {
  template<typename A> auto concat(const A& a, const A& b) -> A {
    A c;
    c.reserve(a.size() + b.size());
    c.insert(c.end(), a.begin(), a.end());
    c.insert(c.end(), b.begin(), b.end());
    return c;
  }
} // namespace concat_sequence
