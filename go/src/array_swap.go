package dsalgo

func Swap[T any](a []T, i, j int) {
	a[i], a[j] = a[j], a[i]
}
