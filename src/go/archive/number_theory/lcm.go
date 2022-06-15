package number_theory


/* cut below */



func (
	i Int,
) LCM(
	j Int,
) (
	lcm Int,
) {
	gcd := i.GCD(j)
	lcm = i / gcd * j
	lcm = lcm.Abs().(Int)
	return
}
