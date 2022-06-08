package cp 


//


type Int int 


func (
	x Int,
) Abs() Int {
	if x < 0 { x *= -1 }
	return x
}


func (
	x Int,
) BitCnt() (
	cnt int,
) {
	n := int(x)
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


func (
	x Int,
) BitLen() (
	l int,
) {
	for x > 0 {
		x >>= 1
		l++
	}
	return 
}



func (
	x Int,
) GCD(
	y Int,
) Int {
	if y == 0 { return x.Abs() }
	return y.GCD(x % y)
}


func (
	x Int,
) LCM(
	y Int,
) Int {
	l := x / x.GCD(y) * y
	return l.Abs()
}