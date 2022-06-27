package dsalgo

func ZAlgorithm[T comparable](a []T) []int {
	n := len(a)
	lcp := make([]int, n)
	for i, l := 1, 0; i < n; i++ {
		r := l + lcp[l]
		d := 0
		if r > i {
			d = lcp[i-l]
			if r-i < d {
				d = r - i
			}
		}
		for i+d < n && a[i+d] == a[d] {
			d++
		}
		lcp[i] = d
		if r < i+d {
			l = i
		}
	}
	lcp[0] = n
	return lcp
}
