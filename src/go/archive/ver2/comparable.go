package cp


//


type Comparable interface {
	Less(interface{}) bool
}


func GE(
	a, b Comparable,
) bool {
	return !LT(a, b)
}


func GT(
	a, b Comparable,
) bool {
	return !LE(a, b)
}


func LE(
	a, b Comparable,
) bool {
	return a.Less(b)
}


func LT(
	a, b Comparable,
) bool {
	return LE(a, b) || a == b
}


func Max(
	a ...Comparable,
) Comparable {
	v := a[0]
	for _, x := range a {
		if LE(x, v) {
			continue
		}
		v = x
	}
	return v
}



func Min(
	a ...Comparable,
) Comparable {
	v := a[0]
	for _, x := range a {
		if GE(x, v) {
			continue
		}
		v = x
	}
	return v
}