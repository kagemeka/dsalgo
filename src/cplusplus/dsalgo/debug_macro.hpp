#pragma once
#include "print_macro.hpp"

#ifdef CPP_DEBUG // g++ -DCPP_DEBUG ...
#define debug(...) print(__VA_ARGS__);
#else
#define debug(...) nullptr
#endif
