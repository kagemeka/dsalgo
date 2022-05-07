package bit


func BitLength(n int) int {
	l := 0
	for 1 << l <= n { l++ }
	return l
}



func Popcount(n int) int
