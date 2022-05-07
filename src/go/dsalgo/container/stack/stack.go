package stack


// st := make(Stack, 0)
type Stack []interface{}

func (st *Stack) Push(x interface{}) { *st = append(*st, x) }

func (st *Stack) Pop() interface{} {
	n := len(*st)
	x := (*st)[n - 1]
	(*st)[n - 1] = nil
	*st = (*st)[:n - 1]
	return x
}