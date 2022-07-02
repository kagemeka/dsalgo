#include "const_modulus.hpp"
#include "default_modular_arithmetic.hpp"
#include "modular_int.hpp"

using mint1_000_000_007 =
    modular_int<default_modular_arithmetic<const_modulus<int, 1'000'000'007>>>;

using mint998_244_353 =
    modular_int<default_modular_arithmetic<const_modulus<int, 998'244'353>>>;
