package types


import (
	"sort"
)


/* cut below */



type FloatSlice []Float


func (
	a FloatSlice,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a FloatSlice,
) Standard() (
	b []float64,
) {
	n := len(a)
	b = make(
		[]float64,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = float64(a[i])
	}
	return
}


func (
	a FloatSlice,
) Make(
	n Int, 
	v Float,
) (
	b FloatSlice,
) {
	b = make(FloatSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}


func (
	a FloatSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(FloatSlice, n)
	copy(s, a)
	return s
} 


func (
	a FloatSlice,
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
	a FloatSlice,
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
	a FloatSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "), 
		a.IS()...,
	)
}


func (
	a FloatSlice,
) Max() (
	Float,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Float)
}


func (
	a FloatSlice,
) Min() (
	Float,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Float)
}


func (
	a FloatSlice,
) Sum() (
	Float,
) {
	b := make(
		[]Numeric,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Sum(b...).(Float)
}


func (
	a FloatSlice,
) Len() int {
	return len(a)
}


func (
	a FloatSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
} 


func (
	a FloatSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a FloatSlice,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a FloatSlice,
) Reverse() {
	Reverse(a)
}


func (
	a FloatSlice,
) Reversed() (
	s FloatSlice,
) { 
	s = a.Clone().(FloatSlice)
	s.Reverse()
	return
}


func (
	a FloatSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a FloatSlice,
) Sorted() (
	FloatSlice,
) {
	a = a.Clone().(FloatSlice)
	a.Sort()
	return a
}


func (
	a FloatSlice,
) BisectLeft(
	x Float,
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
	a FloatSlice,
) BisectRight(
	x Float,
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
	a FloatSlice,
) LIS(
	inf Float,
) (
	lis FloatSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.FloatSlice()
	return
}


func (
	a *FloatSlice,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(Float),
	)
}


func (
	a FloatSlice,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(FloatSlice)
	a.Push(x)
	return a 
}