package types

/* cut below */



type RuneMatrix []RuneSlice


func (
	a RuneMatrix,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a RuneMatrix,
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
	a RuneMatrix,
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
	a RuneMatrix,
) Make(
	n, m Int,
	v Rune,
) (
	b RuneMatrix,
) {
	b = make(RuneMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}


func (
	a RuneMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a RuneMatrix,
) Len() int {
	return len(a)
}


func (
	a RuneMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a RuneMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(RuneMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(RuneSlice))
	}
	return s
}


func (
	a RuneMatrix,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a RuneMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a RuneMatrix,
) Reversed() (
	s RuneMatrix,
) {
	s = (
		a.Clone().
		(RuneMatrix))
	s.Reverse()
	return
}


func (
	a *RuneMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(RuneSlice),
	)
}


func (
	a RuneMatrix,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(RuneMatrix)
	a.Push(x)
	return a
}


func (
	a RuneMatrix,
) Flatten() (
	b RuneSlice,
) {
	a = a.Clone().(RuneMatrix)
	n, m := a.Shape()
	b = make(RuneSlice, 0, n * m)
	for i := Int(0); i < n; i++ {
		b = append(b, a[i]...)
	}
	return
}
