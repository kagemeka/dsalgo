package types 


import (
	"sort"
)


/* cut below */



type RuneSlice []Rune


func (
	a RuneSlice,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a RuneSlice,
) Standard() (
	b []rune,
) {
	n := len(a)
	b = make(
		[]rune,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = rune(a[i])
	}
	return
}


func (
	a RuneSlice,
) Make(
	n Int, 
	v Rune,
) (
	b RuneSlice,
) {
	b = make(RuneSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}


func (
	a RuneSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(RuneSlice, n)
	copy(s, a)
	return s
}


func (
	a RuneSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(IS, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a RuneSlice,
) CompSlice() (
	b CompSlice,
) {
	n := len(a)
	b = make(CompSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a RuneSlice,
) String() (
	string,
) {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "), 
		a.IS()...,
	)
}


func (
	a RuneSlice,
) Str() (
	Str,
) {
	b := a.Standard()
	return Str(b)
}


func (
	a RuneSlice,
) Max() (
	Rune,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Rune)
}


func (
	a RuneSlice,
) Min() (
	Rune,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Rune)
}


func (
	a RuneSlice,
) Len() int {
	return len(a)
}


func (
	a RuneSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
} 


func (
	a RuneSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
} 


func (
	a RuneSlice,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a RuneSlice,
) Reverse() {
	Reverse(a)
}


func (
	a RuneSlice,
) Reversed() (
	s RuneSlice,
) { 
	s = a.Clone().(RuneSlice)
	s.Reverse()
	return
}


func (
	a RuneSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a RuneSlice,
) Sorted() (
	RuneSlice,
) {
	a = a.Clone().(RuneSlice)
	a.Sort()
	return a
}


func (
	a RuneSlice,
) BisectLeft(
	x Rune,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	i = Int(sort.Search(n, f))
	return 
}


func (
	a RuneSlice,
) BisectRight(
	x Rune,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	i = Int(sort.Search(n, f))
	return 
}


func (
	a RuneSlice,
) LIS(
	inf Rune,
) (
	lis RuneSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.RuneSlice()
	return
}


func (
	a *RuneSlice,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(Rune),
	)
}


func (
	a RuneSlice,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(RuneSlice)
	a.Push(x)
	return a 
}