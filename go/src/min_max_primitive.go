package dsalgo

func Max[T PrimitiveOrd](a ...T) T {
	// len(a) > 0
	mx := a[0]

	for _, x := range a {
		if x > mx {
			mx = x
		}
	}
	return mx
}

func Min[T PrimitiveOrd](a ...T) T {
	// len(a) > 0
	mn := a[0]

	for _, x := range a {
		if x < mn {
			mn = x
		}
	}
	return mn
}
