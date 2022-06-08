package topology


/* cut below */



type AStarItem struct {
	Node Int
	C, H, S Int
	Dist Int
}


func (
	x AStarItem,
) LT(
	other AStarItem,
) Bool {
	if x.S != other.S {
		return x.S < other.S 
	}
	return x.H < other.H
}



type AStarHeap []AStarItem


func (
	h AStarHeap,
) Len() int {
	return len(h)
}


func (
	h AStarHeap,
) Less(
	i, j int,
) bool {
	return bool(h[i].LT(h[j]))
}


func (
	h AStarHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}


func (
	h *AStarHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h, 
		x.(AStarItem),
	)
}


func (
	h *AStarHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}



type HeuristicFunc func(
	Int,
) (
	Int,
)



type AStar struct {
	G Graph
	Heap AStarHeap
	Cost IntSlice
	F HeuristicFunc
	src, dst Int
	inf Int
	x AStarItem
	e Edge 
}


func (
	a *AStar,
) SetGraph(
	g Graph,
) {
	a.G = g
}


func (
	a *AStar,
) SetHeuristicFunc(
	f HeuristicFunc,
) {
	a.F = f
}


func (
	a *AStar,
) Prepare(
	src Int,
	dst Int,
	inf Int,
) {
	a.src, a.dst = src, dst 
	a.inf = inf
	a.InitCost()
	a.InitHeap()
}


func (
	a *AStar,
) InitCost() {
	n := a.G.Size() 
	src := a.src
	inf := a.inf
	cost := a.Cost.Make(
		n,
		inf,
	)
	cost[src] = 0
	a.Cost = cost
}


func (
	a *AStar,
) InitHeap() {
	cost := a.Cost
	src := a.src
	h := AStarHeap{}
	heap.Init(&h)
	c := cost[src]
	hc := a.F(src)
	s := c + hc
	x := AStarItem{
		Node: src,
		C: c,
		H: hc,
		S: s,
	}
	heap.Push(&h, x)
	a.Heap = h
}


func (
	a *AStar,
) Search() {
	h := &a.Heap 
	for h.Len() > 0 {
		a.Open()
		if a.isDst() {
			return 
		}
		if a.Searched() {
			continue
		}
		a.Explore()
	}
}


func (
	a *AStar,
) Open() {
	h := &a.Heap
	x := (
		heap.Pop(h).
		(AStarItem))
	a.x = x
}


func (
	a *AStar,
) isDst() (
	Bool,
) {
	x := a.x 
	i := x.Node
	return i == a.dst
}


func (
	a *AStar,
) Searched() (
	Bool,
) {
	x := a.x 
	i, c := x.Node, x.C
	return c > a.Cost[i]
}


func (
	a *AStar,
) Explore() {
	u := a.x.Node
	edges := a.G.Edges
	for _, e := range edges[u] {
		a.e = e 
		a.exploreSupport()
	}
}


func (
	a *AStar,
) exploreSupport() {
	c := a.x.C
	e := a.e 
	v := e.To 
	c += e.Weight
	cost := a.Cost 
	if c >= cost[v] {
		return 
	}
	cost[v] = c 
	h := a.F(c)
	s := c + h
	x := AStarItem{
		Node: v,
		C: c,
		H: h,
		S: s,
	}
	heap.Push(&a.Heap, x)
}