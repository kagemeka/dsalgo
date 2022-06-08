package topology


/* cut below */



type TreeBFS struct {
	G Tree
	Root Int
	Depth IntSlice
	Dist IntSlice
	Parent IntSlice
	Que IntSlice
}


func (
	bfs *TreeBFS,
) SetGraph(
	g Tree,
) {
	bfs.G = g
}


func (
	bfs *TreeBFS,
) Prepare(
	root Int,
) {
	n := bfs.G.Size()
	depth := bfs.Depth.Make(
		n,
		-1,
	)
	depth[root] = 0
	dist := bfs.Dist.Make(
		n,
		-1,
	)
	dist[root] = 0
	parent := bfs.Parent.Make(
		n,
		-1,
	)
	parent[root] = root
	que := make(
		IntSlice,
		0,
	)
	que.Push(root)
	bfs.Depth = depth
	bfs.Dist = dist
	bfs.Parent = parent
	bfs.Que = que
}


func (
	bfs *TreeBFS,
) Search() {
	que := &bfs.Que
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}


func (
	bfs *TreeBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	depth := bfs.Depth
	dist := bfs.Dist
	parent := bfs.Parent
	for
	_, e := range g.Edges[u] {
		v := e.To
		d := e.Weight
		if depth[v] != -1 {
			continue
		}
		depth[v] = depth[u] + 1
		dist[v] = dist[u] + d
		parent[v] = u
		que.Push(v)
	}
}
