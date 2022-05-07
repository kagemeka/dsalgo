package bisect


import (
	"sort"
)

func BisectLeft(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] >= x })
}



func BisectRight(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] > x })
}
