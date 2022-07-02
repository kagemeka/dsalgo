#pragma once
#include <iostream>

template <typename A> // Arithmetic
class modular_int {
  using T = typename std::decay<decltype(A::mod())>::type;

  T value;
  using Self = modular_int;
  constexpr static auto mod() -> T { return A::mod(); }

  template <typename U>
  constexpr static auto norm(const U& x) -> T {
    return (x % mod() + mod()) % mod();
  }

public:
  constexpr modular_int() : value() {}

  template <typename U>
  modular_int(const U& x) {
    value = norm(x);
  }

  auto operator()() const -> const T& { return value; }
  template <typename T>
  explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> Self { return Self(A::neg(value)); }
  auto operator+=(const Self& rhs) -> Self& {
    value = A::add(value, rhs.value);
    return *this;
  }
  auto operator-=(const Self& rhs) -> Self& { return *this += -rhs; }
  auto operator++() -> Self& { return *this += 1; }
  auto operator--() -> Self& { return *this -= 1; }
  auto operator++(int) -> Self {
    Self res(*this);
    *this += 1;
    return res;
  }
  auto operator--(int) -> Self {
    Self res(*this);
    *this -= 1;
    return res;
  }
  auto operator*=(const Self& rhs) -> Self& {
    value = A::mul(value, rhs.value);
    return *this;
  }

  [[nodiscard]] auto inv() const -> Self { return Self(A::inv(value)); }

  auto operator/=(const Self& rhs) -> Self& { return *this *= rhs.inv(); }

  friend auto operator+(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) += rhs;
  }
  friend auto operator-(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) -= rhs;
  }
  friend auto operator*(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) *= rhs;
  }
  friend auto operator/(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) /= rhs;
  }
  friend auto operator==(const Self& lhs, const Self& rhs) -> bool {
    return lhs.value == rhs.value;
  }
  friend auto operator!=(const Self& lhs, const Self& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
    T v;
    stream >> v;
    x.value = norm(v);
    return stream;
  }
  friend auto operator<<(std::ostream& stream, const Self& x) -> std::ostream& {
    return stream << x.value;
  }
};
