package dsalgo

func SieveOfEratosthenesLowMemoryGenerator(lo, hi int) chan int {
	ch := make(chan int, 1<<16)
	if lo < 2 {
		lo = 2
	}
	if hi < 2 {
		hi = 2
	}
	go func() {
		defer close(ch)
		query := RangeSieveOfEratosthenes(hi)
		range_size := FloorSqrt(hi) << 3
		for i := lo; i < hi; i += range_size {
			for _, p := range query(i, Min(hi, i+range_size)) {
				ch <- p
			}
		}
	}()
	return ch
}
