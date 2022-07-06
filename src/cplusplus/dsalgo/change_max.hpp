#pragma once
#include "replace_assign.hpp"

#include <algorithm>
using namespace std;

template<typename T> auto chmax(T& a, const T& b) -> void {
  replace([](T a, T b) -> T { return max(a, b); }, a, b);
}
