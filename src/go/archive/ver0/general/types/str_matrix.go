package types 



/* cut below */



type StrMatrix []StrSlice


func (
	a StrMatrix,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a StrMatrix,
) Len() int {
	return len(a)
}


func (
	a StrMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a StrMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StrMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(StrSlice))
	}
	return s
} 


func (
	a StrMatrix,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a StrMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a StrMatrix,
) Reversed() (
	s StrMatrix,
) { 
	s = (
		a.Clone().
		(StrMatrix))
	s.Reverse()
	return
}


func (
	a *StrMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a, 
		x.(StrSlice),
	)
}


func (
	a StrMatrix,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(StrMatrix)
	a.Push(x)
	return a 
}