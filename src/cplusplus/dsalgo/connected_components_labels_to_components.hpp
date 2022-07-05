#pragma once
#include <vector>
using namespace std;

auto labels_to_components(vector<int> const& labels) -> vector<vector<int>> {
  int n = labels.size();
  int k = *max_element(labels.begin(), labels.end()) + 1;
  vector<vector<int>> comp(k);
  for(int i = 0; i < n; i++) comp[labels[i]].push_back(i);
  return comp;
}
