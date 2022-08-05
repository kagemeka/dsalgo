#pragma once
#include "replace_assign.hpp"
#include <algorithm>
using namespace std;
template<typename T> auto chmin(T& a, const T& b) -> void {
  replace([](T a, T b) -> T { return min(a, b); }, a, b);
}
