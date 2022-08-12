#include "bit_length_32.hpp"
#include <cassert>
#include <vector>
using namespace std;
template<typename G> class dual_segtree {
  using T = typename G::T;
  G g;
  vector<T> node;
  auto operate_node(int i, T x) { node[i] = g.op(node[i], x); }
  auto propagate(int i) {
    operate_node(i << 1, node[i]);
    operate_node(i << 1 | 1, node[i]);
    node[i] = g.e();
  }
  auto n() -> int { return node.size() >> 1; }
  auto height() -> int { return bit_length(n()); }
  void pull(int i) {
    for(int j = height() - 1; j > 0; j--) propagate(i >> j);
  }

public:
  int size;
  dual_segtree(G g, int size): g(g), size(size) {
    assert(size > 0);
    int n = 1 << bit_length(size - 1);
    node.resize(n << 1, g.e());
  }
  auto operator[](int i) -> T& {
    assert(0 <= i && i < size);
    i += n();
    pull(i);
    return node[i];
  }
  auto operate(int l, int r, T x) {
    assert(0 <= l && l <= r && r <= size);
    int n = this->n();
    l += n, r += n;
    pull(l / (l & -l)), pull(r / (r & -r) - 1);
    while(l < r) {
      if(l & 1) operate_node(l++, x);
      if(r & 1) operate_node(--r, x);
      l >>= 1, r >>= 1;
    }
  }
};
// example monoid range update query)
struct M {
  using T = long;
  static constexpr long none = 1l << 60;
  auto op(const T& a, const T& b) -> T { return b == e() ? a : b; }
  auto e() -> T { return none; }
};