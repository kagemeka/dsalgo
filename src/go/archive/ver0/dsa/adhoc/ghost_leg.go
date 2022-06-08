package adhoc

/* cut below */



type GhostLeg IntSlice


func (
	gl GhostLeg,
) Identity(
	n Int,
) (
	e GhostLeg,
) {
	e = make(
		GhostLeg,
		n,
	)
	for i := Int(0); i < n; i++ {
		e[i] = i
	}
	return
}


func (
	a GhostLeg,
) Dot(
	b GhostLeg,
) (
	c GhostLeg,
) {
	n := len(b)
	c = make(
		GhostLeg,
		n,		
	)
	for i := 0; i < n; i++ {
		c[i] = a[b[i]]
	}
	return
}


func (
	a GhostLeg,
) Pow(
	n Int,
) (
	b GhostLeg,
) {
	if n == 0 {
		m := Int(len(a))
		e := a.Identity(m)
		return e
	}
	b = a.Pow(n >> 1)
	b = b.Dot(b)
	if n & 1 == 1 {
		b = b.Dot(a)
	}
	return 
}