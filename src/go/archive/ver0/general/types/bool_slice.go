package types


/* cut below */



type BoolSlice []Bool


func (
	a BoolSlice,
) Make(
	n Int,
	v Bool,
) (
	b BoolSlice,
) {
	b = make(BoolSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
}


func (
	a BoolSlice,
) Any() (
	Bool,
) {
	for _, x := range a {
		if !x {
			continue
		}
		return true
	}
	return false
}


func (
	a BoolSlice,
) All() (
	Bool,
) {
	for _, x := range a {
		if x {
			continue
		}
		return false
	}
	return true
}
