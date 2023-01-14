package combinatorics


/* cut below */



type Binom map[PII]Modular



type Choose struct {
	cache Binom
	mod Int
}


func (
	c *Choose,
) Init(
	mod Int,
) {
	c.cache = make(Binom)
	c.mod = mod
}


func (
	c *Choose,
) Calc(
	n, r Int,
) (
	v Modular,
) {
	mod := c.mod
	if r > n || r < 0 {
		return Modular{0, mod}
	}
	if r == 0 {
		return Modular{1, mod}
	}
	i := PII{n, r}
	cache := c.cache
	if v, ok := cache[i]; ok {
		return v
	}
	v = c.Calc(n - 1, r)
	v.IAdd(c.Calc(n - 1, r - 1))
	cache[i] = v
	return
}


func (
	c *Choose,
) Calculator() (
	func(
		Int,
		Int,
	) Modular,
) {
	return c.Calc
}
