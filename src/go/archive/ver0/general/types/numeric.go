package types


/* cut below */



type Numeric interface {
	Add(Numeric) Numeric
	Neg() Numeric
	Sub(Numeric) Numeric
	Mul(Numeric) Numeric
	Pow(Int) Numeric
	Root(Int) Float
	Abs() Numeric
}


func Sum(
	a ...Numeric,
) (
	s Numeric,
) {
	s = Int(0)
	for  _, x := range a {
		s = s.Add(x)
	}
	return
}
