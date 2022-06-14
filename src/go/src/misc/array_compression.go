package dsa

import "sort"


// ac := new(ArrayCompression)
// ac.Compress(a []int)
// ac.Retrieve(i int)
type ArrayCompression struct { v []int }

func (ac *ArrayCompression) Compress(a []int) []int {
	buf := make(map[int]bool)
	for _, x := range a { buf[x] = true }
	v := make([]int, 0, len(buf))
	for k := range buf { v = append(v, k) }
	sort.Ints(v)
	n := len(a)
	rank := make([]int, n)
	for i := 0; i < n; i++ { rank[i] = sort.SearchInts(v, a[i]) }
	ac.v = v
	return rank
}

func (ac *ArrayCompression) Retrieve(i int) int { return ac.v[i] }
