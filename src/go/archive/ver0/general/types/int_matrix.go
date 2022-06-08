package types


/* cut below */



type IntMatrix []IntSlice


func (
	a IntMatrix,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a IntMatrix,
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
	a IntMatrix,
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
	a IntMatrix,
) Make(
	n, m Int,
	v Int,
) (
	b IntMatrix,
) {
	b = make(IntMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}


func (
	a IntMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a IntMatrix,
) Len() int {
	return len(a)
}


func (
	a IntMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a IntMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(IntMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(IntSlice))
	}
	return s
}


func (
	a IntMatrix,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a IntMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a IntMatrix,
) Reversed() (
	s IntMatrix,
) {
	s = (
		a.Clone().
		(IntMatrix))
	s.Reverse()
	return
}


func (
	a *IntMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(IntSlice),
	)
}


func (
	a IntMatrix,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(IntMatrix)
	a.Push(x)
	return a
}


func (
	a IntMatrix,
) CumSum() (
	IntMatrix,
) {
	a = a.CumSum0()
	a = a.CumSum1()
	return a
 }


func (
	a IntMatrix,
) CumSum0() (
	IntMatrix,
) {
	a = a.Clone().(IntMatrix)
	n, _ := a.Shape()
	for
	i := Int(0); i < n - 1; i++ {
		a.cumSum0Support(i)
	}
	return a
}


func (
	a IntMatrix,
) cumSum0Support(
	i Int,
) {
	_, m := a.Shape()
	for j := Int(0); j < m; j++ {
		a[i + 1][j] += a[i][j]
	}
}


func (
	a IntMatrix,
) CumSum1() (
	IntMatrix,
) {
	a.TransPose()
	a = a.CumSum0()
	a.TransPose()
	return a
}


func (
	a *IntMatrix,
) TransPose() {
	*a = (*a).TransPosed()
}


func (
	a IntMatrix,
) TransPosed() (
	b IntMatrix,
) {
	n, m := a.Shape()
	b = b.Make(
		m,
		n,
		0,
	)
	for i := Int(0); i < n; i++ {
		b.transPoseSupport(a, i)
	}
	return
}


func (
	a IntMatrix,
) transPoseSupport(
	b IntMatrix,
	j Int,
) {
	n, _ := a.Shape()
	for i := Int(0); i < n; i++ {
		a[i][j] = b[j][i]
	}
}


func (
	a IntMatrix,
) Modularize(
	mod Int,
) (
	b ModMatrix,
) {
	n, _ := a.Shape()
	b = make(ModMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = a[i].Modularize(mod)
	}
	return
}
