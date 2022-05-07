package fenwick
// query with fenwick tree


import "kagemeka/dsa/tree/fenwick"
import "kagemeka/dsa/algebra/abstract"

// TODO: cut below.


// query := new(PointOperateXorRangeGetXor)
// query.Init(a []int)
type PointOperateXorRangeGetXor struct { 
	fw *FenwickTree
}

func (q *PointOperateXorRangeGetXor) op(a, b interface{}) interface{} {
	return a.(int) ^ b.(int)
}

func (q *PointOperateXorRangeGetXor) e() interface{} { return 0 }

func (q *PointOperateXorRangeGetXor) inverse(a interface{}) interface{} { 
	return a
}

func (q *PointOperateXorRangeGetXor) Init(a []int) {
	n := len(a)
	b := make([]interface{}, n)
	for i := 0; i < n; i++ { b[i] = a[i] }
	q.fw = NewFenwickTree(Monoid{Op: q.op, E: q.e, commutative: true}, b)
}

func (q *PointOperateXorRangeGetXor) Get(i int) int {
	return q.fw.Get(i).(int)
}

func (q *PointOperateXorRangeGetXor) Set(i int, x int) { 
	q.fw.Set(i, x)
}

func (q *PointOperateXorRangeGetXor) GetRange(l, r int) int {
	return q.op(q.inverse(q.Get(l)), q.Get(r)).(int)
}