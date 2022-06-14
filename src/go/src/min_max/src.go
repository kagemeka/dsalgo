package min_max

func Max[T Comparable](values ...T) T {
	max := values[0]
	for _, v := range values {
		if !(v.Lt(max) || v == max) {
			max = v
		}
	}
	return max
}
