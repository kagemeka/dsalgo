package topology


/* cut below */



type LCA struct {
	G Tree
	Parent IntSlice
	Ancestors IntMatrix
	Dist IntSlice
	Depth IntSlice
}


func (
	l *LCA,
) SetTree(
	g Tree,
) {
	l.G = g
}


func (
	l *LCA,
) Prepare(
	root Int,
) {
	bfs := TreeBFS{}
	bfs.SetGraph(l.G)
	bfs.Prepare(root)
	bfs.Search()
	l.Parent = bfs.Parent 
	l.Depth = bfs.Depth
	l.Dist = bfs.Dist 
}


func (
	l *LCA,
) FindAncestors() {
	n := Int(len(l.G.Nodes))
	ancestors := l.Ancestors 
	m := l.Depth.Max().BitLen()
	ancestors = ancestors.Make(
		m,
		n,
		-1,
	)
	ancestors[0] = l.Parent
	l.Ancestors = ancestors
	for 
	i := Int(0); i < m - 1; i++ {
		l.nxtAncestor(i)
	}
}


func (
	l *LCA,
) nxtAncestor(
	i Int,
) {
	n := Int(len(l.G.Nodes))
	x := l.Ancestors[i]
	y := make(
		IntSlice,
		n,
	)
	for i := Int(0); i < n; i++ {
		y[i] = x[x[i]]
	}
	l.Ancestors[i + 1] = y
}


func (
	l *LCA,
) FindDist(
	u, v Int,
) (
	d Int,
) {
	du := l.Dist[u]
	dv := l.Dist[v]
	lca := l.FindLCA(u, v)
	dLCA := l.Dist[lca]
	d = du + dv - 2 * dLCA
	return
}


func (
	l *LCA,
) FindLCA(
	u, v Int,
) (
	lca Int,
) {
	u, v = l.sort(u, v)
	du := l.Depth[u]
	dv := l.Depth[v]
	v = l.upStream(
		v, 
		dv - du,
	)
	if v == u {
		lca = u 
		return
	}
	lca = l.findLCASupport(
		du,
		u, 
		v,
	)
	return
}


func (
	l *LCA,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	du := l.Depth[u]
	dv := l.Depth[v]
	if du > dv {
		u, v = v, u
	}
	return u, v
}


func (
	l *LCA,
) upStream(
	v Int,
	d Int,
) (
	Int,
){
	n := d.BitLen()
	for i := Int(0); i < n; i++ {
		if ^d >> i & 1 == 1 {
			continue
		}
		v = l.Ancestors[i][v]
	}
	return v
}


func (
	l *LCA,
) findLCASupport(
	dep Int,
	u, v Int,
) (
	lca Int,
) {
	n := dep.BitLen()
	ancs := l.Ancestors
	for 
	i := n - 1; i > -1; i-- {
		anc := ancs[i]
		nu, nv := anc[u], anc[v]
		if nu == nv {
			continue
		}
		u, v = nu, nv 
	}
	lca = l.Parent[u]
	return	
}