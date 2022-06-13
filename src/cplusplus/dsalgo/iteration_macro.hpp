#ifndef ROOT_DSALGO_SRC_CPLUSPLUS_DSALGO_ITERATION_MACRO_HPP
#define ROOT_DSALGO_SRC_CPLUSPLUS_DSALGO_ITERATION_MACRO_HPP

#pragma once

namespace dsalgo::iteration_macro {

#define range(i, lo, hi, step) for (int(i) = lo; (i) < (hi); (i) += (step))
#define repeat(times) for (int _ = 0; _ < (times); ++_)
#define loop while (true)

} // namespace dsalgo::iteration_macro

#endif
