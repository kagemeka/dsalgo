package combinatorics

/* cut below */



func (
	i Int,
) NxtCmb() (
	j Int,
) {
	x := i & -i
	y := i + x 
	j = i & ^y
	j /= x 
	j >>= 1 
	j |= y
	return
}