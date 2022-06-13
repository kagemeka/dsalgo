#ifndef MODULAR_HPP
#define MODULAR_HPP

#include "./extgcd_modinv.hpp"
#include "./modulus.hpp"
#include <iostream>
#include <optional>

template <typename M>
class modular {
  uint32_t value;
  constexpr static auto mod() -> uint32_t { return M::get(); }
  static auto normalize(const int64_t& x) -> uint32_t {
    return (x % mod() + mod()) % mod();
  }

public:
  constexpr modular() : value() {}
  modular(const uint64_t& x) { value = normalize(x); }
  auto operator()() const -> const uint32_t& { return value; }
  template <typename T>
  explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> modular { return modular(mod() - value); }
  auto operator+=(const modular& rhs) -> modular& {
    uint64_t v = (uint64_t)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  auto operator-=(const modular& rhs) -> modular& {
    uint64_t v = value;
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
    value = (uint64_t)value * rhs.value % mod();
    return *this;
  }

  auto mul_inv() const -> std::optional<modular> {
    auto [g, inv] = extgcd_modinv(mod(), value);
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

using mint1000000007 = modular<static_mod<1000000007>>;
using mint998244353 = modular<static_mod<998244353>>;

#endif // MODULAR_HPP
