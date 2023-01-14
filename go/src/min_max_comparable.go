package dsalgo

func ComparableMax[T Comparable](values ...T) T {
	return Reduce(func(a, b T) T {
		if a.Lt(b) {
			return b
		}
		return a
	}, values...)
}

func ComparableMin[T Comparable](values ...T) T {
	return Reduce(func(a, b T) T {
		if b.Lt(a) {
			return b
		} else {
			return a
		}
	}, values...)
}
