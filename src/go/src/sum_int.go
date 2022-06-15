package dsalgo

func SumInt(a ...int) int {
	s := 0
	for _, x := range a {
		s += x
	}
	return s
}
