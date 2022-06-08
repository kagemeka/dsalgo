#include <vector>
#include <algorithm>


template <typename T>
class ArrayCompression {
  std::vector<T> v;

public:
  std::vector<int> compress(const std::vector<T> &a) {
    v = a;
    std::sort(v.begin(), v.end());
    v.erase(std::unique(v.begin(), v.end()), v.end());
    int n = a.size();
    std::vector<int> idx(n);
    for (int i = 0; i < n; i++) {
      idx[i] = std::lower_bound(v.begin(), v.end(), a[i]) - v.begin();
    }
    return idx;
  }

  T retrieve(int i) const { return v[i]; }
};
