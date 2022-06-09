#include <bits/stdc++.h>
using namespace std;


template<typename T>
class Modular {

public:

using Type = typename decay<
  decltype(T::value)
>::type;

constexpr Modular() : value(
) {
}

template<typename U>
Modular(const U& x) {
  value = normalize(x);
}

template<typename U>
static Type normalize(
  const U& x
) {
  Type v =
    static_cast<Type>(x);
  v %= mod();
  v += mod();
  v %= mod();
  return v;
}

const Type& operator() (
) const {
  return value;
}

template<typename U>
explicit operator U() const {
  return static_cast<U>(value);
}

constexpr static Type mod() {
  return T::value;
}

Modular& operator+=(
  const Modular& other
) {
  value += other.value;
  if (value >= mod()) {
    value -= mod();
  }
  return *this;
}

Modular operator+(
  const Modular& other
) const {
  Modular res(*this);
  return res += other;
}

Modular& operator-=(
  const Modular& other
) {
  value -= other.value;
  if (value < 0) {
    value += mod();
  }
  return *this;
}

Modular operator-(
  const Modular& other
) const {
  Modular res(*this);
  return res -= other;
}

template<typename U>
Modular& operator+=(
  const U& other
) {
  *this += Modular(other);
  return *this;
}

template<typename U>
Modular& operator-=(
  const U& other
) {
  *this -= Modular(other);
  return *this;
}

Modular& operator++() {
  return *this += 1;
}

Modular& operator--() {
  return *this -= 1;
}

Modular operator++(int) {
  Modular res(*this);
  *this += 1;
  return res;
}

Modular operator--(int) {
  Modular res(*this);
  *this -= 1;
  return res;
}

Modular operator-() const {
  return Modular(-value);
}

Modular& operator*=(
  const Modular& other
) {
  value *= other.value;
  value %= mod();
  return *this;
}

Modular operator*(
  const Modular& other
) const {
  Modular res(*this);
  return res *= other;
}


template<typename U>
Modular pow(const U& n) const {
  if (!n) return 1;
  Modular a = pow(n>>1);
  a *= a;
  if (n&1) a *= *this;
  return a;
}

Modular invert() const {
  return pow(mod() - 2);
}

Modular& operator/=(
  const Modular& other
) {
  *this *= other.invert();
  return *this;
}

Modular operator/(
  const Modular& other
) const {
  Modular res(*this);
  return res /= other;
}

template<typename U>
friend istream& operator>>(
  istream& is,
  Modular<U>& number
) {
  return is >> number.value;
}

friend ostream& operator<<(
  ostream& os,
  const Modular& number
) {
  return os << number.value;
}


private:

Type value;

};


constexpr long long MOD
  = (long long)1e9 + 7;


using Mint = Modular<
  integral_constant<
    decay<decltype(MOD)>::type,
    MOD
  >
>;
