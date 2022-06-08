package topology


/* cut below */



type Node struct {
	ID Int
}


func (
	v Node,
) String() (
	string,
) {
	return fmt.Sprint(v.ID)
}



type NodeSlice []Node



type Edge struct {
	ID Int
	From, To Int
	Weight Int
	Capacity Int
}



type EdgeSlice []Edge


func (
	edges *EdgeSlice,
) Push(
	e interface{},
) {
	*edges = append(
		*edges,
		e.(Edge),
	)
}



type EdgeMatrix []EdgeSlice



type Graph struct {
	Nodes NodeSlice
	Edges EdgeMatrix
}


func (
	g *Graph,
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
	g *Graph,
) AddEdge(e Edge) {
	u := e.From
	g.Edges[u].Push(e)
}


func (
	g *Graph,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}


func (
	g *Graph,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v
}


func (
	g *Graph,
) Size() (
	n Int,
) {
	n = Int(len(g.Nodes))
	return
}
