package main

import (
	"fmt"

	. "github.com/kagemeka/dsalgo/src/go/src/primitive_min_max"
)

func MakeSlice[T any](size int, value T) []T {
	a := make([]T, size)
	for i := 0; i < size; i++ {
		a[i] = value
	}
	return a
}

func SieveOfEratosthenes(size int) []int {
	primes := make([]int, 0, size>>4)
	if size <= 2 {
		return primes
	}
	primes = append(primes, 2)
	is_prime := MakeSlice(size>>1, true)
	for i := 3; i < size; i += 2 {
		if !is_prime[i>>1] {
			continue
		}
		primes = append(primes, i)
		for j := i * i >> 1; j < size>>1; j += i {
			is_prime[j] = false
		}
	}
	return primes
}

func IntSqrtBinarySearch(n int) int {
	lo, hi := 0, Min(n, 1<<32)
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

func FloorSqrt(n int) int {
	return IntSqrtBinarySearch(n)
}

func Assert(ok bool) {
	if !ok {
		panic("assertion failed")
	}
}

func RangeSieveOfEratosthenes(less_than int) func(int, int) []int {
	primes := SieveOfEratosthenes(FloorSqrt(less_than))

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

func main() {
	gen := SieveOfEratosthenesLowMemoryGenerator(1, 1<<29)
	s := 0
	for p := range gen {
		// fmt.Println(p)
		s += p
	}
	fmt.Println(s)

}
