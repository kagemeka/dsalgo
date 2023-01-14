package dsalgo

func IntSqrtBinarySearch(n int) int {
	lo, hi := 0, Min(n+1, 1<<32)
	for hi-lo > 1 {
		x := (lo + hi) >> 1
		if x*x <= n {
			lo = x
		} else {
			hi = x
		}
	}
	return lo
}
