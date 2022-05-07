package arithemetic


func Max(a ...int) int {
	// len(a) > 0
	mx := a[0]
	for _, x := range a { if x > mx { mx = x } }
	return mx
}


func Min(a ...int) int {
	// len(a) > 0 
	mn := a[0]
	for _, x := range a { if x < mn { mn = x } }
	return mn 
}


func Sum(a ...int) int {
	s := 0
	for _, x := range a { s += x }
	return s
}
