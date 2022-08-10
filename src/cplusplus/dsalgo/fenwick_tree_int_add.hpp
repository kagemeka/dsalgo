#include <vector>
using namespace std;
struct fenwick {
  vector<int> node;
  fenwick(int size): node(size + 1) {}
  auto size() -> int { return node.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) node[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) { v += node[i]; }
    return v;
  }
};
