package combinatorics


/* cut below */



type NChoose struct {
	Values ModSlice
}


func (
	c *NChoose,
) Init(
	n Int,
	r Modular,
) {
	ifac := r.InverseFactorial()
	l := Int(len(ifac))
	mod := r.Mod
	nChoose := c.Values.Make(
		l,
		Modular{1, mod},
	)
	for
	i := Int(0); i < l - 1; i++ {
		x := Modular{n - i, mod}
		x = nChoose[i].Mul(x)
		nChoose[i + 1] = x
	}
	for
	i := Int(0); i < l; i++ {
		nChoose[i].IMul(ifac[i])
	}
	c.Values = nChoose
}


func (
	c *NChoose,
) Get(
	i Int,
) (
	v Modular,
) {
	v = c.Values[i]
	return
}
