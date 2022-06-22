#ifndef MODULAR_HPP
#define MODULAR_HPP

#include "./extgcd_modinv.hpp"
#include "./modulus.hpp"
#include <iostream>
#include <optional>

#include <cassert>
#include <cstdint>
#include <type_traits>

template <typename T, T v, std::enable_if_t<2 <= v>* = nullptr>
struct const_mod {
  static constexpr auto get() -> T { return v; }
};

template <typename T, typename I>
struct static_mod {
  static constexpr auto get() -> T { return value; }
  static constexpr void set(T v) {
    assert(2 <= v);
    value = v;
  }

private:
  static T value;
};
template <typename T, typename I>
T static_mod<T, I>::value;

template <typename M> // impl modulus get
class default_arith {
  using T = typename std::decay<decltype(M::get())>::type;

public:
  constexpr auto static m() -> T { return M::get(); }

  template <typename U>
  constexpr auto static norm(U x) -> T {
    if (x < 0) {
      U m = static_cast<U>(default_arith::m());
      if (x < -m) x %= m;
      x += m;
    }
    T v = static_cast<T>(x);
    if (v >= m()) v %= m();
    return v;
  }

  template <typename U>
  constexpr auto static add(U a, U b) -> T {
    return norm(a + b);
  }

  template <typename U>
  constexpr auto static neg(U a) -> T {
    T v = norm(a);
    return v == 0 ? 0 : m() - v;
  }

  template <typename U>
  constexpr auto static sub(U a, U b) -> T {
    return add(norm(a), neg(b));
  }

  template <typename U>
  constexpr auto static mul(U a, U b) -> T {
    return norm(a) * norm(b) % m();
  }

  template <typename U>
  constexpr auto static inv(U a) -> T {
    using ext_euclid::mgi;
    return mgi(m(), norm(a)).se;
  }

  template <typename U>
  constexpr auto static div(U a, U b) -> T {
    return mul(norm(a), inv(b));
  }
};
template <typename M>
class modular {
  u32 value;
  constexpr static auto mod() -> u32 { return M::get(); }
  static auto normalize(const int64_t& x) -> u32 {
    return (x % mod() + mod()) % mod();
  }

public:
  constexpr modular() : value() {}
  modular(const u64& x) { value = normalize(x); }
  auto operator()() const -> const u32& { return value; }
  template <typename T>
  explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> modular { return modular(mod() - value); }
  auto operator+=(const modular& rhs) -> modular& {
    u64 v = (u64)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  auto operator-=(const modular& rhs) -> modular& {
    u64 v = value;
    if (v < rhs.value) v += mod();
    value = v - rhs.value;
    return *this;
  }
  auto operator++() -> modular& { return *this += 1; }
  auto operator--() -> modular& { return *this -= 1; }
  auto operator++(int) -> modular {
    modular res(*this);
    *this += 1;
    return res;
  }
  auto operator--(int) -> modular {
    modular res(*this);
    *this -= 1;
    return res;
  }
  auto operator*=(const modular& rhs) -> modular& {
    value = (u64)value * rhs.value % mod();
    return *this;
  }

  auto mul_inv() const -> std::optional<modular> {
    using ext_euclid::mgi;
    if (value == 0) return std::nullopt;
    auto [g, inv] = mgi(mod(), value);
    if (g != 1) return std::nullopt;
    return inv;
  }

  auto operator/=(const modular& rhs) -> modular& {
    if (auto inv = rhs.mul_inv()) {
      return *this *= *inv;
    } else {
      throw;
    }
  }

  friend auto operator+(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) += rhs;
  }
  friend auto operator-(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) -= rhs;
  }
  friend auto operator*(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) *= rhs;
  }
  friend auto operator/(const modular& lhs, const modular& rhs) -> modular {
    return modular(lhs) /= rhs;
  }
  friend auto operator==(const modular& lhs, const modular& rhs) -> bool {
    return lhs.value == rhs.value;
  }
  friend auto operator!=(const modular& lhs, const modular& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& is, modular& x) -> std::istream& {
    int64_t v;
    is >> v;
    x.value = normalize(v);
    return is;
  }
  friend auto operator<<(std::ostream& os, const modular& x) -> std::ostream& {
    return os << x.value;
  }
};

using const_modulus::const_mod;
using mint1000000007 = modular<const_mod<u32, 1000000007>>;
using mint998244353 = modular<const_mod<u32, 998244353>>;

#endif // MODULAR_HPP
