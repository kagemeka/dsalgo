package dsalgo

// query with segment tree

// query := new(PointSetRangeGetXor)
// query.Init(a []int)
type PointSetRangeGetXor struct {
	seg *SegmentTree
}

func (q *PointSetRangeGetXor) op(a, b interface{}) interface{} {
	return a.(int) ^ b.(int)
}

func (q *PointSetRangeGetXor) e() interface{} { return 0 }

func (q *PointSetRangeGetXor) Init(a []int) {
	n := len(a)
	b := make([]interface{}, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	q.seg = NewSegmentTree(Monoid{Op: q.op, E: q.e}, b)
}

func (q *PointSetRangeGetXor) Get(l, r int) int {
	return q.seg.Get(l, r).(int)
}

func (q *PointSetRangeGetXor) Set(i int, x int) {
	q.seg.Set(i, x)
}

// type PointOperateXorRangeGetXor struct{ PointSetRangeGetXor }

// func (q *PointOperateXorRangeGetXor) Set(i int, x int) {
// 	q.seg.Set(i, q.op(q.Get(i, i+1), x))
// }
