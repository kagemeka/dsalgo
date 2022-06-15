package types


/* cut below */



type Float float64


func (
	x Float,
) Abs() (
	Numeric,
) {
	if x < 0 {
		return -x
	}
	return x
}


func (
	x *Float,
) IAdd(
	other Numeric,
) {
	var y Float
	switch other.(type) {
	case Int:
		y = Float(other.(Int))
	case Float:
		y = other.(Float)
	}
	*x += y
}


func (
	x Float,
) Add(
	other Numeric,
) (
	Numeric,
) {
	x.IAdd(other)
	return x
}


func (
	x Float,
) Neg() (
	Numeric,
) {
	return -x
}


func (
	x *Float,
) ISub(
	other Numeric,
) {
	x.IAdd(other.Neg())
}


func (
	x Float,
) Sub(
	other Numeric,
) (
	Numeric,
) {
	x.ISub(other)
	return x
}


func (
	x *Float,
) IMul(
	other Numeric,
) {
	var y Float
	switch other.(type) {
	case Int:
		y = Float(other.(Int))
	case Float:
		y = other.(Float)
	}
	*x *= y
}


func (
	x Float,
) Mul(
	other Numeric,
) (
	Numeric,
) {
	x.IMul(other)
	return x
}


func (
	x Float,
) Pow(n Int) (
	Numeric,
){
	if n == 0 {
		return Float(1)
	}
	a := x.Pow(n >> 1).(Float)
	a *= a
	if n & 1 == 1 {
		a *= x
	}
	return a
}


func (
	x Float,
) Root(
	n Int,
) (
	root Float,
) {
	y := x
	f := func(
		x Float,
	) (Float) {
		return x.Pow(n).(Float) - y
	}
	const x0 = 1e13
	root = Newton(f, x0)
	return
}


func (
	x Float,
) LT(
	other Comparable,
) Bool {
	return x < other.(Float)
}


func (
	x Float,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Float)
}


func (
	x Float,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Float,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}
