package types


import (
	"sort"
)


/* cut below */



type IntSlice []Int


func (
	a IntSlice,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a IntSlice,
) Standard() (
	b []int,
) {
	n := len(a)
	b = make(
		[]int,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = int(a[i])
	}
	return
}


func (
	a IntSlice,
) Make(
	n Int, 
	v Int,
) (
	b IntSlice,
) {
	b = make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}


func (
	a IntSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(IntSlice, n)
	copy(s, a)
	return s
} 


func (
	a IntSlice,
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
	a IntSlice,
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
	a IntSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "), 
		a.IS()...,
	)
}


func (
	a IntSlice,
) Max() (
	Int,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Int)
}


func (
	a IntSlice,
) Min() (
	Int,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Int)
}


func (
	a IntSlice,
) Sum() (
	Int,
) {
	b := make(
		[]Numeric,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Sum(b...).(Int)
}


func (
	a IntSlice,
) Len() int {
	return len(a)
}


func (
	a IntSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
} 


func (
	a IntSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a IntSlice,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a IntSlice,
) Reverse() {
	Reverse(a)
}


func (
	a IntSlice,
) Reversed() (
	s IntSlice,
) { 
	s = a.Clone().(IntSlice)
	s.Reverse()
	return
}


func (
	a IntSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a IntSlice,
) Sorted() (
	IntSlice,
) {
	a = a.Clone().(IntSlice)
	a.Sort()
	return a
}


func (
	a IntSlice,
) CumSum() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i + 1] += b[i]
	}
	return 
}


func (
	a IntSlice,
) CumProd() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i + 1] *= b[i]
	}
	return 
}


func (
	a IntSlice,
) CumMax() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i + 1] = Max(
			b[i + 1],
			b[i],
		).(Int)
	}
	return 
}


func (
	a IntSlice,
) BisectLeft(
	x Int,
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
	a IntSlice,
) BisectRight(
	x Int,
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
	a IntSlice,
) LIS(
	inf Int,
) (
	lis IntSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.IntSlice()
	return
}


func (
	a *IntSlice,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(Int),
	)
}


func (
	a IntSlice,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(IntSlice)
	a.Push(x)
	return a 
}


func (
	a *IntSlice,
) PopFront() (
	x Int,
) {
	x = (*a)[0]
	*a = (*a)[1:]
	return
}


func (
	a IntSlice,
) BitMatrix() (
	b BitMatrix,
) {
	n := len(a)
	b = make(BitMatrix, n)
	for i := 0; i < n; i++ {
		b[i] = IntSlice{a[i]}		
	}
	return
}


func (
	a IntSlice,
) Modularize(
	mod Int,
) (
	b ModSlice,
) {
	n := len(a)
	b = make(ModSlice, n)
	for i := 0; i < n; i++ {
		v := Modular{a[i], mod}
		v.Init()
		b[i] = v
	}
	return 
}


func (
	a IntSlice,
) Channel() (
	ch chan IntSlice,
) {
	const bufSize = 1
	ch = make(
		chan IntSlice, 
		bufSize,
	)
	return
}


func (
	a IntSlice,
) ChTransPort(
	from <-chan Slice,
) (
	<-chan IntSlice,
) {
	ch := a.Channel()
	go a.chTransSupport(ch, from)
	return ch
}


func (
	a IntSlice,
) chTransSupport(
	ch chan IntSlice,
	p <-chan Slice,
) {
	for i := range p {
		ch <- i.(IntSlice)
	}
	close(ch)
}