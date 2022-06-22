
namespace erat {
  // sieve of eratosthenes

  auto ps(usize sz) -> vec<u32> {
    vec<u32> p;
    p.reserve(sz >> 4);
    if (sz > 2) p.push_back(2);
    vec<bool> is_p(sz >> 1, true);
    for (usize i = 3; i < sz; i += 2) {
      if (!is_p[i >> 1]) continue;
      p.emplace_back(i);
      for (usize j = i * i >> 1; j < sz >> 1; j += i) is_p[j] = false;
    }
    return p;
  }

} // namespace erat
