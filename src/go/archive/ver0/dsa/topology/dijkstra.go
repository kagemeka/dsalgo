package topology 


import (
	. "kagemeka/general/types"
	"container/heap"
)

/* cut below */



type DijkstraItem struct {
	Node Int 
	Dist Int
}


func (
	x DijkstraItem,
) LT(
	other DijkstraItem,
) Bool {
	return x.Dist < other.Dist
}



type DijkstraHeap [
]DijkstraItem


func (
	h DijkstraHeap,
) Len() int {
	return len(h)
}


func (
	h DijkstraHeap,
) Less(
	i, j int,
) bool {
	return bool(h[i].LT(h[j]))
}


func (
	h DijkstraHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}


func (
	h *DijkstraHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h, 
		x.(DijkstraItem),
	)
}


func (
	h *DijkstraHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}



type Dijkstra struct {
	G Graph
	Heap DijkstraHeap
	Dist IntSlice
	Paths ModSlice
	Predecessor IntMatrix
	src Int
	inf Int
	mod Int
	x DijkstraItem
	e Edge 
}


func (
	di *Dijkstra,
) SetGraph(
	g Graph,
) {
	di.G = g
}


func (
	di *Dijkstra,
) Prepare(
	src Int,
	inf Int,
	mod Int,
) {
	di.src = src 
	di.inf = inf
	di.mod = mod 
	di.InitDist()
	di.InitHeap()
	di.InitPaths()
	di.InitPredecessor()
}


func (
	di *Dijkstra,
) InitHeap() {
	src := di.src
	dist := di.Dist
	h := DijkstraHeap{}
	heap.Init(&h)
	x := DijkstraItem{
		Node: src,
		Dist: dist[src],
	}
	heap.Push(&h, x)
	di.Heap = h
}


func (
	di *Dijkstra,
) InitDist() {
	n := di.G.Size() 
	src := di.src 
	inf := di.inf
	dist := di.Dist.Make(
		n,
		inf,
	)
	dist[src] = 0
	di.Dist = dist
}


func (
	di *Dijkstra,
) InitPaths() {
	n := di.G.Size()
	src := di.src 
	mod := di.mod 
	paths := di.Paths.Make(
		n, 
		Modular{0, mod},
	)
	paths[src] = Modular{1, mod}
	di.Paths = paths
}


func (
	di *Dijkstra,
) InitPredecessor() {
	n := di.G.Size()
	pred := di.Predecessor.Make(
		n,
		0,
		0,
	)
	di.Predecessor = pred
}


func (
	di *Dijkstra,
) Search() {
	h := &di.Heap 
	for h.Len() > 0 {
		di.Open()
		if di.Searched() {
			continue
		}
		di.Explore()
	}
}


func (
	di *Dijkstra,
) Open() {
	h := &di.Heap
	x := (
		heap.Pop(h).
		(DijkstraItem))
	di.x = x
}


func (
	di *Dijkstra,
) Searched() (
	Bool,
) {
	x := di.x 
	i, d := x.Node, x.Dist
	return d > di.Dist[i]
}


func (
	di *Dijkstra,
) Explore() {
	u := di.x.Node
	edges := di.G.Edges
	for _, e := range edges[u] {
		di.e = e 
		di.exploreSupport()
	}
}


func (
	di *Dijkstra,
) exploreSupport() {
	x := di.x
	u, d := x.Node, x.Dist 
	e := di.e 
	v := e.To 
	d += e.Weight
	dist := di.Dist
	paths := di.Paths 
	pred := di.Predecessor
	if d > dist[v] {
		return 
	}
	if d == dist[v] {
		pred[v].Push(u)
		paths[v].IAdd(paths[u])
		return 
	}
	pred[v] = IntSlice{u}
	paths[v] = paths[u]
	dist[v] = d
	x = DijkstraItem{
		Node: v,
		Dist: d,
	}
	heap.Push(&di.Heap, x)
}