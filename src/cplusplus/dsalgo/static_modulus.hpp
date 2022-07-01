struct default_id;
template <typename T, typename I = default_id>
struct static_modulus {
  static constexpr auto get() -> T { return value; }
  static constexpr void set(T v) {
    assert(1 <= v);
    value = v;
  }

private:
  static T value;
};
template <typename T, typename I>
T static_modulus<T, I>::value;
