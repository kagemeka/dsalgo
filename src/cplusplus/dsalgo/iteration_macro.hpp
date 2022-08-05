#pragma once
#define loop while(1)
#define repeat(t) for(int __ = 0; __ < t; ++__)
#define range(i, n) for(int i = 0; i < n; ++i)
#define range_rev(i, n) for(int i = n - 1; i >= 0; --i)
#define range_detail(i, l, h, s) for(int i = l; i < h; i += s)
#define iter(x, a) for(auto const& x: a)
#define iter_mut(x, a) for(auto&& x: a)
