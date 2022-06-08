#ifndef MODULAR_HPP
#define MODULAR_HPP

#include "./extgcd_modinv.hpp"
#include "./modulus.hpp"
#include <iostream>
#include <optional>

template <typename M> class modular {
  uint32_t value;
  constexpr static uint32_t mod() { return M::get(); }
  static uint32_t normalize(const int64_t& x) { return (x % mod() + mod()) % mod(); }

public:
  constexpr modular() : value() {}
  modular(const uint64_t& x) { value = normalize(x); }
  const uint32_t& operator()() const { return value; }
  template <typename T> explicit operator T() const { return static_cast<T>(value); }

  modular operator-() const { return modular(mod() - value); }
  modular& operator+=(const modular& rhs) {
    uint64_t v = (uint64_t)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  modular& operator-=(const modular& rhs) {
    uint64_t v = value;
    if (v < rhs.value) v += mod();
    value = v - rhs.value;
    return *this;
  }
  modular& operator++() { return *this += 1; }
  modular& operator--() { return *this -= 1; }
  modular operator++(int) {
    modular res(*this);
    *this += 1;
    return res;
  }
  modular operator--(int) {
    modular res(*this);
    *this -= 1;
    return res;
  }
  modular& operator*=(const modular& rhs) {
    value = (uint64_t)value * rhs.value % mod();
    return *this;
  }

  std::optional<modular> mul_inv() const {
    auto [g, inv] = extgcd_modinv(mod(), value);
    if (g != 1) return std::nullopt;
    return inv;
  }

  modular& operator/=(const modular& rhs) {
    if (auto inv = rhs.mul_inv()) {
      return *this *= *inv;
    } else {
      throw;
    }
  }

  friend modular operator+(const modular& lhs, const modular& rhs) { return modular(lhs) += rhs; }
  friend modular operator-(const modular& lhs, const modular& rhs) { return modular(lhs) -= rhs; }
  friend modular operator*(const modular& lhs, const modular& rhs) { return modular(lhs) *= rhs; }
  friend modular operator/(const modular& lhs, const modular& rhs) { return modular(lhs) /= rhs; }
  friend bool operator==(const modular& lhs, const modular& rhs) { return lhs.value == rhs.value; }
  friend bool operator!=(const modular& lhs, const modular& rhs) { return lhs.value != rhs.value; }

  friend std::istream& operator>>(std::istream& is, modular& x) {
    int64_t v;
    is >> v;
    x.value = normalize(v);
    return is;
  }
  friend std::ostream& operator<<(std::ostream& os, const modular& x) { return os << x.value; }
};

using mint1000000007 = modular<static_mod<1000000007>>;
using mint998244353 = modular<static_mod<998244353>>;

#endif // MODULAR_HPP
