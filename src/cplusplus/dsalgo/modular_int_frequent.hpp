#include "const_modulus.hpp"
#include "default_modular_arithmetic.hpp"
#include "modular_int.hpp"

using mint1000000007 =
    modular_int<default_modular_arithmetic<const_modulus<int, 1000000007>>>;

using mint998244353 =
    modular_int<default_modular_arithmetic<const_modulus<int, 998244353>>>;
