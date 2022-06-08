package topology 


/* cut below */



type Dinic struct{
	G Graph
	Level IntSlice
	Src, Sink Int
	u Int 
	e Edge
	in, out, f Int 
}


func (
	di *Dinic,
) SetGraph(
	g Graph,
) {
	di.G = g 
}


func (
	di *Dinic,
) Prepare(
	Src, Sink Int,
) {
	di.Src = Src
	di.Sink = Sink 
}


func (
	di *Dinic,
) Search() (
	flow Int,
) {
	sink := di.Sink
	src := di.Src
	const inf = 1 << 60 
	di.in = inf 
	for {
		di.updateLevel()
		if di.Level[sink] == -1 {
			return
		}
		di.u = src 
		di.out = 0
		di.flowToSink()
		flow += di.out
	}
}


func (
	di *Dinic,
) updateLevel() {
	bfs := GraphBFS{}
	bfs.SetGraph(di.G)
	bfs.Prepare(di.Src)
	bfs.Search()
	di.Level = bfs.Level
}


func (
	di *Dinic,
) flowToSink() {
	u := di.u
	if u == di.Sink {
		di.out = di.in
		return 
	}
	g := &di.G
	edges := g.Edges[u]
	g.Edges[u] = make(
		EdgeSlice,
		0,
		len(edges),
	)
	for _, e := range edges {
		di.e = e 
		di.flowToSinkSupport()
	}
}


func (
	di *Dinic,
) flowToSinkSupport() {
	if !di.checkLevel() {
		return 
	}
	di.calcSuccrFlow()
	di.updateEdges()
	di.updateFlow()
}


func (
	di *Dinic,
) updateFlow() {
	di.out += di.f
}


func (
	di *Dinic,
) updateEdges() {
	f := di.f 
	e := di.e 
	v := e.To
	e.Capacity -= f
	if e.Capacity > 0 {
		di.G.AddEdge(e)
	}
	if f == 0 {
		return 
	}
	u := di.u
	e = Edge{
		From: v,
		To: u,
		Capacity: f,
	}
	di.G.AddEdge(e)
}


func (
	di *Dinic,
) calcSuccrFlow() {
	u := di.u 
	e := di.e
	in := di.in
	out := di.out
	di.u = e.To
	di.in = Min(
		in - out,
		e.Capacity,
	).(Int)
	di.out = 0 
	di.flowToSink()
	di.f = di.out
	di.u = u
	di.e = e 
	di.in = in
	di.out = out
}


func (
	di *Dinic,
) checkLevel() (
	ok Bool,
) {
	lv := di.Level
	u := di.u 
	e := di.e 
	v := e.To 
	if lv[v] > lv[u] {
		ok = true 
		return 
	}
	di.G.AddEdge(e)
	return
}