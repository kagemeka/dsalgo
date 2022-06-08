package topology 


/* cut below */



type Tree Graph


func (
	g *Tree,
) Init(n Int) {
	nodes := make(NodeSlice, n)
	edges := make(EdgeMatrix, n)
	for i := Int(0); i < n; i++ {
		e :=  make(
			EdgeSlice,
			0,
		)
		edges[i] = e
	}
	g.Nodes = nodes 
	g.Edges = edges 
}


func (
	g *Tree,
) AddEdge(e Edge) {
	u := e.From 
	g.Edges[u].Push(e)
}


func (
	g *Tree,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}


func (
	g *Tree,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v 
}


func (
	g *Tree,
) Size() (
	n Int,
) {
	n = Int(len(g.Nodes))
	return
}