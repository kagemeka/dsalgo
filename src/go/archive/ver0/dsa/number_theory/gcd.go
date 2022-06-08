package number_theory


/* cut below */



func (
	i Int,
) GCD(
	j Int,
) (
	gcd Int,
) {
	if j == 0 {
		gcd = i.Abs().(Int)
		return
	}
	gcd = j.GCD(i % j)
	return 
}