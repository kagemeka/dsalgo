struct default_id;
template<typename T, typename I = default_id> struct static_mod {
  static constexpr auto get() -> T { return value; }
  static constexpr void set(T v) {
    assert(v > 0);
    value = v;
  }

private:
  static T value;
};
template<typename T, typename I> T static_mod<T, I>::value;
