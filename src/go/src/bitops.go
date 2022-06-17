package dsalgo
// import "math"

func BitLengthNaive(n int) int {
	l := 0
	for n > 0 {
		l += 1
		n >>= 1
	}
	return l
}

func PopCount(n int) int
