package euclid



func GCD(x, y int) int {
	if y == 0 { return x }
	return GCD(y, x % y)
}


func LCM(x, y int) int { return x / GCD(x, y) * y }