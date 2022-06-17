package dsalgo

// commutative monoid
type FenwickTree[S any, M Monoid[S]] struct {
	m    *M
	data []S
}

func NewFenwickTree[S any, M Monoid[S]](m *M, a []S) *FenwickTree[S, M] {
	n := len(a)
	data := make([]S, n+1)
	data[0] = (*m).identity()
	for i := 0; i < n; i++ {
		data[i+1] = a[i]
	}
	for i := 1; i < n+1; i++ {
		j := i + (i & -i)
		if j < n+1 {
			data[j] = (*m).op(data[j], data[i])
		}
	}
	return &FenwickTree[S, M]{
		m,
		data,
	}
}

func (fw *FenwickTree[S, M]) Operate(i int, x S) {
	Assert(0 <= i && i < len(fw.data)-1)
	i += 1
	for i < len(fw.data) {
		fw.data[i] = (*fw.m).op(fw.data[i], x)
		i += i & -i
	}
}

func (fw *FenwickTree[S, M]) Reduce(i int) S {
	Assert(0 <= i && i < len(fw.data))
	v := (*fw.m).identity()
	for i > 0 {
		v = (*fw.m).op(v, fw.data[i])
		i -= i & -i
	}
	return v
}
