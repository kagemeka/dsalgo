package modular


/* cut below */



type ModSlice []Modular


func (
	a ModSlice,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a ModSlice,
) Make(
	n Int, 
	v Modular,
) (
	b ModSlice,
) {
	b = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v 
	}
	return 
}


func (
	a ModSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(ModSlice, n)
	copy(s, a)
	return s
} 


func (
	a ModSlice,
) Len() int {
	return len(a)
}


func (
	a ModSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a ModSlice,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a ModSlice,
) Reverse() {
	Reverse(a)
}


func (
	a ModSlice,
) Reversed() (
	s ModSlice,
) { 
	s = a.Clone().(ModSlice)
	s.Reverse()
	return
}


func (
	a *ModSlice,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(Modular),
	)
}


func (
	a ModSlice,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(ModSlice)
	a.Push(x)
	return a 
}


func (
	a ModSlice,
) CumSum() (
	b ModSlice,
) {
	b = a.Clone().(ModSlice)
	n := len(a)
	for i := 0; i < n - 1; i++ {
		b[i + 1].IAdd(b[i])
	}
	return 
}


func (
	a ModSlice,
) CumProd() (
	b ModSlice,
) {
	b = a.Clone().(ModSlice)
	n := len(a)
	for i := 0; i < n - 1; i++ {
		b[i + 1].IMul(b[i])
	}
	return 
}


func (
	a ModSlice,
) Matrix() (
	b ModMatrix,
) {
	n := len(a)
	b = make(ModMatrix, n)
	for i := 0; i < n; i++ {
		b[i] = ModSlice{a[i]}		
	}
	return
}