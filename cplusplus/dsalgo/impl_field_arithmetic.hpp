#pragma once
template<typename T> auto operator+(T& a, T& b) -> T { return T(a) += b; }
template<typename T> auto operator-(T& a, T& b) -> T { return T(a) -= b; }
template<typename T> auto operator*(T& a, T& b) -> T { return T(a) *= b; }
template<typename T> auto operator/(T& a, T& b) -> T { return T(a) /= b; }
