
#include <algorithm>
#include <vector>

template <typename A>
auto unique(A a) -> A {
  sort(a.begin(), a.end());
  a.erase(std::unique(entire(a)), a.end());
  return a;
}

template <typename T>
class compress {
  vec<T> v; // unique values

public:
  template <typename A>
  compress(A a) {
    v = unique(vec<T>(entire(a)));
  }

  auto operator()(T x) -> usize {
    usize i = lower(v, x);
    assert(i < v.size() && v[i] == x);
    return i;
  }

  [[nodiscard]] auto inv(usize i) const -> T { return v[i]; }

  template <typename A>
  auto static once(A a) -> vec<usize> {
    auto f = compress(a);
    vec<usize> i(a.size());
    for (usize j = 0; j < a.size(); ++j) i[j] = f(a[j]);
    return i;
  }
};

template <typename S, typename F, typename A>
auto accum(F f, A a) -> A {
  for (usize i = 0; i < a.size(); ++i) {
    a[i + 1] = f(a[i], a[i + 1]);
  }
  return a;
}

template <typename S, S (*f)(S, S), typename A>
auto accum(A a) -> A {
  return accum<S>(f, a);
}

auto _test_accum() {
  auto f = [](int a, int b) { return a * b; };
  vec<int> a{1, 1, 2, 3};
  a = accum<int>(f, a);
  print(a);
}

auto _test_compress() {
  using namespace std;
  auto a = vec<u32>{1, 4, 3, 4, 5, 6, 7, 8, 9, 10};
  auto f = compress<u32>(a);

  auto i = f(7);
  cout << i << endl;
  cout << f.inv(i) << endl;
  print(compress<u32>::once(a));
}
