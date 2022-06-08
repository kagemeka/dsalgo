#include <cassert>
#include <cstdint>
#include <type_traits>

template <uint32_t v, std::enable_if_t<2 <= v>* = nullptr> struct static_mod {
  static constexpr uint32_t get() { return value; }

private:
  static constexpr uint32_t value = v;
};

template <typename I> struct dynamic_mod {
  static constexpr uint32_t get() { return value; }
  static constexpr void set(uint32_t v) {
    assert(2 <= v);
    value = v;
  }

private:
  static uint32_t value;
};
template <typename I> uint32_t dynamic_mod<I>::value;