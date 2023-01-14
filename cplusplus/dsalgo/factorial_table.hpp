
#include <vector>
using namespace std;
template<typename S> auto factorial_table(int size) -> vector<S> {
  vector<S> a(size);
  iota(a.begin(), a.end(), 0);
  a[0] = 1;
  for(int i = 1; i < size - 1; ++i) a[i + 1] *= a[i];
  return a;
}
