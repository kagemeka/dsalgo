package modular


/* cut below */



type ModMatrix []ModSlice


func (
	a ModMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a ModMatrix,
) Make(
	n, m Int,
	v Modular,
) (
	b ModMatrix,
) {
	b = make(
		ModMatrix,
		n,
	)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}


func (
	a ModMatrix,
) Identity(
	n Int,
) (
	e ModMatrix,
) {
	mod := a[0][0].Mod
	v := Modular{0, mod}
	e = e.Make(n, n, v)
	for i := Int(0); i < n; i++ {
		v := Modular{1, mod}
		e[i][i] = v
	}
	return
}


func (
	a ModMatrix,
) Dot(
	b ModMatrix,
) (
	c ModMatrix,
) {
	n, _ := a.Shape()
	_, m := b.Shape()
	mod := a[0][0].Mod
	v := Modular{0, mod}
	c = c.Make(n, m, v)
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
	c ModMatrix,
) dotSupport(
	a, b ModMatrix,
	i, j Int,
) {
	l := len(b)
	for k := 0; k < l; k++ {
		c[i][j].IAdd(
			a[i][k].Mul(b[k][j]),
		)
	}
}


func (
	a ModMatrix,
) Pow(
	n Int,
) (
	ModMatrix,
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
