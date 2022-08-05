template<typename A, typename F> auto binary_search(const A& a, F f) -> int {
  int ng = -1, ok = a.size();
  while(ok - ng > 1) {
    int i = (ng + ok) >> 1;
    if(f(a[i])) ok = i;
    else ng = i;
  }
  return ok;
}
