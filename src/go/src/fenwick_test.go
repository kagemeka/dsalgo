package dsalgo

type M struct{}

func (M) op(a, b int) int {
	return a + b
}

func (M) identity() int {
	return 0
}

func (M) invert(a int) int {
	return -a
}

// TODO:
