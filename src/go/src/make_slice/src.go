package make_slice

func MakeSlice[T any](size int, value T) []T {
	a := make([]T, size)
	for i := 0; i < size; i++ {
		a[i] = value
	}
	return a
}
