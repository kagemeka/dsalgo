package types


/* cut below */



type FloatMatrix []FloatSlice


func (
	a FloatMatrix,
) At(
	i Int,
) (
	v interface{},
) {
	v = a[i]
	return
}


func (
	a FloatMatrix,
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
	a FloatMatrix,
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
	a FloatMatrix,
) Make(
	n, m Int,
	v Float,
) (
	b FloatMatrix,
) {
	b = make(FloatMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}


func (
	a FloatMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a FloatMatrix,
) Len() int {
	return len(a)
}


func (
	a FloatMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a FloatMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(FloatMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(FloatSlice))
	}
	return s
}


func (
	a FloatMatrix,
) Sub(
	i, j Int,
) (
	Slice,
) {
	return a[i:j]
}


func (
	a FloatMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a FloatMatrix,
) Reversed() (
	s FloatMatrix,
) {
	s = (
		a.Clone().
		(FloatMatrix))
	s.Reverse()
	return
}


func (
	a *FloatMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(FloatSlice),
	)
}


func (
	a FloatMatrix,
) Pushed(
	x interface{},
) (
	Slice,
) {
	a = a.Clone().(FloatMatrix)
	a.Push(x)
	return a
}


func (
	a FloatMatrix,
) CumSum() (
	FloatMatrix,
) {
	a = a.CumSum0()
	a = a.CumSum1()
	return a
 }


func (
	a FloatMatrix,
) CumSum0() (
	FloatMatrix,
) {
	a = a.Clone().(FloatMatrix)
	n, _ := a.Shape()
	for
	i := Int(0); i < n - 1; i++ {
		a.cumSum0Support(i)
	}
	return a
}


func (
	a FloatMatrix,
) cumSum0Support(
	i Int,
) {
	_, m := a.Shape()
	for j := Int(0); j < m; j++ {
		a[i + 1][j] += a[i][j]
	}
}


func (
	a FloatMatrix,
) CumSum1() (
	FloatMatrix,
) {
	a.TransPose()
	a = a.CumSum0()
	a.TransPose()
	return a
}


func (
	a *FloatMatrix,
) TransPose() {
	*a = (*a).TransPosed()
}


func (
	a FloatMatrix,
) TransPosed() (
	b FloatMatrix,
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
	a FloatMatrix,
) transPoseSupport(
	b FloatMatrix,
	j Int,
) {
	n, _ := a.Shape()
	for i := Int(0); i < n; i++ {
		a[i][j] = b[j][i]
	}
}
