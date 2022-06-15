package dsalgo

func RangeSieveOfEratosthenes(less_than int) func(int, int) []int {
	primes := SieveOfEratosthenes(FloorSqrt(less_than) + 1)

	query := func(lo, hi int) []int {
		Assert(lo <= hi && hi <= less_than)
		res := make([]int, 0)
		if hi <= 2 {
			return res
		}
		if lo < 2 {
			lo = 2
		}
		if lo&1 == 0 {
			if lo == 2 {
				res = append(res, 2)
			}
			lo += 1
		}
		if lo == hi {
			return res
		}
		size := (hi - lo + 1) >> 1
		is_prime := MakeSlice(size, true)
		for _, i := range primes[1:] {
			mn := i * i
			if mn >= hi {
				break
			}
			mn = Max(mn, (lo+i-1)/i*i)
			if mn&1 == 0 {
				mn += i
			}
			for j := (mn - lo) >> 1; j < size; j += i {
				is_prime[j] = false
			}
		}
		for i, is_prime := range is_prime {
			if is_prime {
				res = append(res, lo+(i<<1))
			}
		}
		return res
	}

	return query
}
