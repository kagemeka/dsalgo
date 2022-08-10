#include <algorithm>
using namespace std;
template<typename T, typename A> auto lower_bound(A& a, T& x) -> int {
  return lower_bound(a.begin(), a.end(), x) - a.begin();
}
template<typename T, typename A> auto upper_bound(A& a, T& x) -> int {
  return upper_bound(a.begin(), a.end(), x) - a.begin();
}
