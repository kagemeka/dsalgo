package types


/* cur below */



type Int int


func (
	x Int,
) Str() (
	Str,
) {
	s := strconv.Itoa(
		int(x),
	)
	return Str(s)
}


func (
	n Int,
) BitLen() (
	l Int,
){
	for n > 0 {
		l++
		n >>= 1
	}
	return
}


func (
	n Int,
) BitCnt() (
	cnt Int,
){
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


func (
	x Int,
) Pow(n Int) (
	Numeric,
){
	return Int(
		Float(x).Pow(n).
		(Float))
}


func (
	x Int,
) Abs() (
	Numeric,
) {
	return Int(
		Float(x).Abs().
		(Float),
	)
}


func (
	x Int,
) Add(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Add(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Neg() (
	Numeric,
) {
	return -x
}


func (
	x Int,
) Sub(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Sub(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Mul(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Mul(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Divmod(
	other Int,
) (
	q Int, r Int,
) {
	q = x / other
	r = x % other
	if r * other >= 0 {
		return
	}
	q--
	r += other
	return
}


func (
	x Int,
) Root(
	n Int,
) (
	root Float,
) {
	return Float(x).Root(n)
}


func (
	x Int,
) LT(
	other Comparable,
) Bool {
	return x < other.(Int)
}


func (
	x Int,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Int)
}


func (
	x Int,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Int,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}
