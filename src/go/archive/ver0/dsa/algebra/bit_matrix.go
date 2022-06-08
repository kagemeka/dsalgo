package algebra

import (
	. "kagemeka/general/types"
)

/* cut below */



type BitMatrix IntMatrix


func (
	a BitMatrix,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a BitMatrix,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(
		IS,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a BitMatrix,
) String() (
	string,
) {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, "\n"),
		a.IS()...,
	)
}


func (
	a BitMatrix,
) Make(n, m Int) (
	b BitMatrix,
) {
	b = make(BitMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = make(IntSlice, m)
	}
	return
}


func (
	a BitMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a BitMatrix,
) Len() int {
	return len(a)
}


func (
	a BitMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a BitMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(BitMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(IntSlice))
	}
	return s
}


func (
	a BitMatrix,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a BitMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a BitMatrix,
) Reversed() (
	s BitMatrix,
) {
	s = (
		a.Clone().
		(BitMatrix))
	s.Reverse()
	return
}


func (
	a *BitMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(IntSlice),
	)
}


func (
	a BitMatrix,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(BitMatrix)
	a.Push(x)
	return a
}


func (
	a BitMatrix,
) Identity(
	n Int,
) (
	e BitMatrix,
) {
	e = a.Make(n, n)
	for i := Int(0); i < n; i++ {
		e[i][i] = ^0
	}
	return
}


func (
	a BitMatrix,
) Dot(
	b BitMatrix,
) (
	c BitMatrix,
) {
	n, _ := a.Shape()
	_, m := b.Shape()
	c = a.Make(n, m)
	for i := Int(0); i < n; i++ {
		for
		j := Int(0);
		j < m;
		j++ {
			c.dotSupport(a, b, i, j)
		}
	}
	return
}


func (
	c BitMatrix,
) dotSupport(
	a, b BitMatrix,
	i, j Int,
) {
	l := len(b)
	for k := 0; k < l; k++ {
		p := a[i][k] & b[k][j]
		c[i][j] ^= p
	}
}


func (
	a BitMatrix,
) Pow(
	n Int,
) (
	BitMatrix,
) {
	m, _ := a.Shape()
	if n == 0 {
		return a.Identity(m)
	}
	b := a.Pow(n >> 1)
	b = b.Dot(b)
	if n & 1 == 1 {
		b = b.Dot(a)
	}
	return b
}
