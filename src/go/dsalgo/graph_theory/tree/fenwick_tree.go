package tree


// import "algebra"

// TODO: cut below


// seg := NewFenwickTree(m Monoid, a []interface{})
type FenwickTree struct {
	m Monoid
	data []interface{}
}

func NewFenwickTree(m Monoid, a []interface{}) *FenwickTree {
	n := len(a)
	data := make([]interface{}, n + 1)
	data[0] = m.E()
	for i := 0; i < n; i++ { data[i + 1] = a[i] }
	for i := 1; i < n + 1; i++ {
		j := i + (i & -i)
		if j < n + 1 { data[j] = m.Op(data[j], data[i]) }
	}
	fw := new(FenwickTree)
	fw.m, fw.data = m, data
	return fw
}

func (fw *FenwickTree) Set(i int, x interface{}) {
	// 0 <= i < size
	i += 1
	for i < len(fw.data) {
		fw.data[i] = fw.m.Op(fw.data[i], x)
		i += i & -i
	}
}

func (fw *FenwickTree) Get(i int) interface{} {
	// 0 <= i < len(fw.data) == size + 1
	v := fw.m.E()
	for i > 0 {
		v = fw.m.Op(v, fw.data[i])
		i -= i & -i
	}
	return v
}
