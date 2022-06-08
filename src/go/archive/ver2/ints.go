package cp 

import (
	"sort"
)
//


type Ints []int





func (
	a Ints,
) BisectLeft(
	x int,
) int {
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	n := len(a)
	return sort.Search(n, f)
}
	


func (
	a Ints,
) BisectRight(
	x int,
) int {
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	n := len(a)
	return sort.Search(n, f)
}


func (
	a Ints,
) Max() int {
	v := a[0]
	for _, x := range a {
		if x > v { v = x }
	}
	return v
}



func (
	a Ints,
) Min() int {
	v := a[0]
	for _, x := range a {
		if x < v { v = x }
	}
	return v
}


func (
	a Ints,
) Sum() (
	s int,
) {
	for _, x := range a { 
		s += x
	}
	return s	
}	