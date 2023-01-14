package dsalgo

func Reduce[T any](f func(T, T) T, value ...T) T {
	Assert(len(value) > 0)
	res := value[0]
	for _, x := range value[1:] {
		res = f(res, x)
	}
	return res
}
