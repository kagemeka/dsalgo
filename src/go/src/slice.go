package dsalgo

func ToAnySlice[T any](a []T) []any {
	b := make([]any, len(a))
	for i, x := range a {
		b[i] = x
	}
	return b
}

func MakeSlice[T any](size int, value T) []T {
	a := make([]T, size)
	for i := 0; i < size; i++ {
		a[i] = value
	}
	return a
}
