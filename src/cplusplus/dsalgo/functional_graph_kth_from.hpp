#pragma once
#include <vector>
using namespace std;
class functional_graph_kth_from {
  vector<int> path;
  int cycle_size;
  int cycle_start_idx;

public:
  functional_graph_kth_from(vector<int> const& f, int src) {
    int n = f.size();
    vector<int> order(n, -1);
    for(int i = src, j = 0;; j++) {
      if(order[i] != -1) {
        cycle_size = j - order[i];
        cycle_start_idx = order[i];
        break;
      }
      order[i] = j;
      path.push_back(i);
      i = f[i];
    }
  }
  auto operator()(long k) -> int const& {
    if(k >= cycle_start_idx)
      k = (k - cycle_start_idx) % cycle_size + cycle_start_idx;
    return path[k];
  }
};
