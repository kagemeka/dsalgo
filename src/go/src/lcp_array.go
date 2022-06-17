package dsalgo

func LCPKasai(a, sa []int) (lcp []int) {
	n := len(a)
	// n > 0 && len(sa) == n
	rank := make([]int, n)
	for i, j := range sa {
		rank[j] = i
	}
	lcp = make([]int, n-1)
	h := 0
	for i := 0; i < n; i++ {
		if h > 0 {
			h--
		}
		r := rank[i]
		if r == n-1 {
			continue
		}
		j := sa[r+1]
		for i+h < n && j+h < n && a[i+h] == a[j+h] {
			h++
		}
		lcp[r] = h
	}
	return
}
