#pragma once

namespace dsalgo {
namespace iteration_macro {

#define range(i, lo, hi, step) for (int i = lo; i < hi; i += step)
#define repeat(times) for (int _ = 0; _ < times; ++_)
#define loop while (true)

} // namespace iteration_macro
} // namespace dsalgo