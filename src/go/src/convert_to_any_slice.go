package dsalgo

func ToAnySlice[T any](a []T) []any {
	b := make([]any, len(a))
	for i, x := range a {
		b[i] = x
	}
	return b
}
