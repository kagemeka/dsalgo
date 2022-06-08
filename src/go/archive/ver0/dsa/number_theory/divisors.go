package number_theory


/* cut below */



func (
	n Int,
) Divisors() (
	divs IntSlice,
) {
	for 
	i := Int(1); 
	i * i <= n; 
	i++ {
		if n % i != 0 {
			continue
		}
		divs = append(divs, i)
		j := n / i 
		if j == i {
			continue
		}
		divs = append(divs, j)
	}
	divs.Sort()
	return 
}