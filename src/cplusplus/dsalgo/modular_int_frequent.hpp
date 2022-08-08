#include "const_modulus.hpp"
#include "modular_int.hpp"
#include "static_modulus.hpp"
using mint1_000_000_007 = modint<const_mod<long, 1'000'000'007>>;
using mint998_244_353 = modint<const_mod<long, 998'244'353>>;
using default_static_mod = static_mod<long, default_id>;
using static_mint = modint<default_static_mod>;
