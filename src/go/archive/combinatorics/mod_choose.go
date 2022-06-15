package combinatorics


import (
	. "kagemeka/general/types"
	. "kagemeka/dsa/algebra/modular"
)


/* cut below */



type ModChoose struct {
	Fact ModSlice
	InvFact ModSlice
	Mod Int
}


func (
	c *ModChoose,
) Init(n Modular) {
	c.Fact, c.InvFact =
		n.Factorial(),
		n.InverseFactorial()
	c.Mod = n.Mod
}


func (
	c *ModChoose,
) Calc(n, r Int) (
	Modular,
) {
	if r < 0 || r > n {
		return Modular{0, c.Mod}
	}
	return c.Fact[n].Mul(
		c.InvFact[r],
	).Mul(
		c.InvFact[n - r],
	)
}


func (
	c *ModChoose,
) Calculator() (
	choose func(
		n, r Int,
	) (
		Modular,
	),
) {
	return c.Calc
}
