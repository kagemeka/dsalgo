package dsalgo

// seg := NewSegmentTree(m Monoid, a []interface{})
type SegmentTree struct {
	m       Monoid
	size, n int
	data    []interface{}
}

func NewSegmentTree(m Monoid, a []interface{}) *SegmentTree {
	size := len(a)
	n := 1 << BitLength(size-1)
	data := make([]interface{}, n<<1)
	for i := 0; i < n<<1; i++ {
		data[i] = m.E()
	}
	for i := 0; i < size; i++ {
		data[n+i] = a[i]
	}
	seg := &SegmentTree{m, size, n, data}
	for i := n - 1; i > 0; i-- {
		seg.merge(i)
	}
	return seg
}

func (seg *SegmentTree) merge(i int) {
	seg.data[i] = seg.m.Op(seg.data[i<<1], seg.data[i<<1|1])
}

func (seg *SegmentTree) Set(i int, x interface{}) {
	// 0 <= i < size
	i += seg.n
	seg.data[i] = x
	for i > 1 {
		i >>= 1
		seg.merge(i)
	}
}

func (seg *SegmentTree) Get(l, r int) interface{} {
	// 0 <= l <= r <= size
	l += seg.n
	r += seg.n
	vl, vr := seg.m.E(), seg.m.E()
	for l < r {
		if l&1 == 1 {
			vl = seg.m.Op(vl, seg.data[l])
			l++
		}
		if r&1 == 1 {
			r--
			vr = seg.m.Op(seg.data[r], vr)
		}
		l >>= 1
		r >>= 1
	}
	return seg.m.Op(vl, vr)
}

func (seg *SegmentTree) MaxRight(is_ok func(interface{}) bool, l int) int {
	// 0 <= l < size
	v, i := seg.m.E(), seg.n+l
	for {
		i /= i & -i
		if is_ok(seg.m.Op(v, seg.data[i])) {
			v = seg.m.Op(v, seg.data[i])
			i++
			if i&-i == i {
				return seg.size
			}
			continue
		}
		for i < seg.n {
			i <<= 1
			if !is_ok(seg.m.Op(v, seg.data[i])) {
				continue
			}
			i++
			v = seg.m.Op(v, seg.data[i])
		}
		return i - seg.n
	}
}

type SegmentTreeLazyConfig struct {
	S, F Monoid
	Map  func(f, x interface{}) (y interface{})
}

type SegmentTreeLazy struct {
	c          *SegmentTreeLazyConfig
	size, n, h int
	data, lazy []interface{}
}

func NewSegmentTreeLazy(
	c *SegmentTreeLazyConfig,
	a []interface{},
) *SegmentTreeLazy {
	size := len(a)
	n := 1 << BitLength(size-1)
	h := BitLength(n)
	data := make([]interface{}, n<<1)
	for i := 0; i < n<<1; i++ {
		data[i] = c.S.E()
	}
	for i := 0; i < size; i++ {
		data[n+i] = a[i]
	}
	lazy := make([]interface{}, n)
	for i := 0; i < n; i++ {
		lazy[i] = c.F.E()
	}
	seg := &SegmentTreeLazy{c, size, n, h, data, lazy}
	for i := n - 1; i > 0; i-- {
		seg.merge(i)
	}
	return seg
}

func (seg *SegmentTreeLazy) merge(i int) {
	seg.data[i] = seg.c.S.Op(seg.data[i<<1], seg.data[i<<1|1])
}

func (seg *SegmentTreeLazy) apply(i int, f interface{}) {
	seg.data[i] = seg.c.Map(f, seg.data[i])
	if i < seg.n {
		seg.lazy[i] = seg.c.F.Op(f, seg.lazy[i])
	}
}

func (seg *SegmentTreeLazy) propagate(i int) {
	seg.apply(i<<1, seg.lazy[i])
	seg.apply(i<<1|1, seg.lazy[i])
	seg.lazy[i] = seg.c.F.E()
}

func (seg *SegmentTreeLazy) Set(l, r int, f interface{}) {
	// 0 <= l && l <= r && r <= size
	l += seg.n
	r += seg.n
	for i := seg.h; i > -1; i-- {
		if (l>>i)<<i != l {
			seg.propagate(l >> i)
		}
		if (r>>i)<<i != r {
			seg.propagate((r - 1) >> i)
		}
	}
	l0, r0 := l, r
	for l < r {
		if l&1 == 1 {
			seg.apply(l, f)
			l++
		}
		if r&1 == 1 {
			r--
			seg.apply(r, f)
		}
		l >>= 1
		r >>= 1
	}
	l, r = l0, r0
	for i := 1; i < seg.h+1; i++ {
		if (l>>i)<<i != l {
			seg.merge(l >> i)
		}
		if (r>>i)<<i != r {
			seg.merge((r - 1) >> i)
		}
	}
}

func (seg *SegmentTreeLazy) Get(l, r int) interface{} {
	// 0 <= l && l <= r && r <= size
	l += seg.n
	r += seg.n
	for i := seg.h; i > -1; i-- {
		if (l>>i)<<i != l {
			seg.propagate(l >> i)
		}
		if (r>>i)<<i != r {
			seg.propagate((r - 1) >> i)
		}
	}
	vl, vr := seg.c.S.E(), seg.c.S.E()
	for l < r {
		if l&1 == 1 {
			vl = seg.c.S.Op(vl, seg.data[l])
			l++
		}
		if r&1 == 1 {
			r--
			vr = seg.c.S.Op(seg.data[r], vr)
		}
		l >>= 1
		r >>= 1
	}
	return seg.c.S.Op(vl, vr)
}

func (seg *SegmentTreeLazy) Update(i int, x interface{}) {
	// 0 <= i && i < size
	i += seg.n
	for j := seg.h; j > -1; j-- {
		seg.propagate(i >> j)
	}
	seg.data[i] = x
	for j := 1; j < seg.h+1; j++ {
		seg.merge(i >> j)
	}
}
