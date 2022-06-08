package types 

import (
	"sort"
)

/* cut below */



type CompSlice []Comparable


func (
	a CompSlice,
) Make(
	n Int, 
	v Comparable,
) (
	b CompSlice,
) {
	b = make(CompSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}
 

func (
	a CompSlice,
) IntSlice() (
	b IntSlice,
) {
	n := len(a)
	b = make(IntSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Int)
	}
	return 
}


func (
	a CompSlice,
) FloatSlice() (
	b FloatSlice,
) {
	n := len(a)
	b = make(FloatSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Float)
	}
	return 
}


func (
	a CompSlice,
) StrSlice() (
	b StrSlice,
) {
	n := len(a)
	b = make(StrSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Str)
	}
	return 
}


func (
	a CompSlice,
) RuneSlice() (
	b RuneSlice,
) {
	n := len(a)
	b = make(RuneSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Rune)
	}
	return 
}


func BisectLeft(
	a CompSlice,
	x Comparable,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return bool(
			a[i].GE(x),
		)
	}
	i = Int(sort.Search(n, f))
	return
}


func BisectRight(
	a CompSlice,
	x Comparable,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return bool(
			a[i].GT(x),
		)
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a CompSlice,
) LIS(
	inf Comparable,
) (
	lis CompSlice,
) {
	n := Int(len(a))
	lis = lis.Make(n, inf)
	for _, x := range a {
		i := BisectLeft(lis, x)
		lis[i] = x
	}
	i := BisectLeft(lis, inf)
	lis = lis[:i]
	return 
}