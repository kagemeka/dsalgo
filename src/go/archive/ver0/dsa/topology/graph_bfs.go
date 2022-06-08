package topology 


/* cut below */



type GraphBFS struct {
	G Graph
	Level IntSlice
	Que IntSlice
}


func (
	bfs *GraphBFS,
) SetGraph(
	g Graph,
) {
	bfs.G = g
}


func (
	bfs *GraphBFS,
) Prepare(
	src Int,
) {
	n := bfs.G.Size()
	level := new(IntSlice).Make(
		n,
		-1,
	)
	level[src] = 0
	que := make(
		IntSlice,
		0,
	)
	que.Push(src)
	bfs.Level = level
	bfs.Que = que
}


func (
	bfs *GraphBFS,
) Search() {
	que := &bfs.Que 
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}


func (
	bfs *GraphBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	lv := &bfs.Level
	for 
	_, e := range g.Edges[u] {
		v := e.To
		if (*lv)[v] != -1 {
			continue
		}
		(*lv)[v] = (*lv)[u] + 1
		que.Push(v)
	}
}