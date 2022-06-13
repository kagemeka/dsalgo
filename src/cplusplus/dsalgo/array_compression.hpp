#include <algorithm>
#include <vector>

template <typename T>
class ArrayCompression {
  std::vector<T> v;

public:
  auto compress(const std::vector<T>& a) -> std::vector<int> {
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

  auto retrieve(int i) const -> T { return v[i]; }
};
