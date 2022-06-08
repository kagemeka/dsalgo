package types


import (
	"sort"
)


/* cut below */



type StrSlice []Str


func (
	a StrSlice,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a StrSlice,
) Standard() (
	b []string,
) {
	n := len(a)
	b = make(
		[]string,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = string(a[i])
	}
	return
}


func (
	a StrSlice,
) Make(
	n Int, 
	v Str,
) (
	b StrSlice,
) {
	b = make(StrSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}


func (
	s StrSlice,
) Join(
	sep Str,
) (
	Str,
) {
	t := strings.Join(
		s.Standard(),
		string(sep),
	)
	return Str(t)
}


func (
	a StrSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StrSlice, n)
	copy(s, a)
	return s
} 


func (
	a StrSlice,
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
	a StrSlice,
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
	a StrSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "), 
		a.IS()...,
	)
}


func (
	a StrSlice,
) Max() (
	Str,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Str)
}


func (
	a StrSlice,
) Min() (
	Str,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Str)
}


func (
	a StrSlice,
) Len() int {
	return len(a)
}


func (
	a StrSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
} 


func (
	a StrSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a StrSlice,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a StrSlice,
) Reverse() {
	Reverse(a)
}


func (
	a StrSlice,
) Reversed() (
	s StrSlice,
) { 
	s = a.Clone().(StrSlice)
	s.Reverse()
	return
}


func (
	a StrSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a StrSlice,
) Sorted() (
	StrSlice,
) {
	a = a.Clone().(StrSlice)
	a.Sort()
	return a
}


func (
	a StrSlice,
) BisectLeft(
	x Str,
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
	a StrSlice,
) BisectRight(
	x Str,
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
	a StrSlice,
) LIS(
	inf Str,
) (
	lis StrSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.StrSlice()
	return
}


func (
	a *StrSlice,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(Str),
	)
}


func (
	a StrSlice,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(StrSlice)
	a.Push(x)
	return a 
}