package topology


/* cut below */



type DisjointSet struct {
	Parent IntSlice 
	Rank IntSlice 
	Size IntSlice
}


func (
	ds *DisjointSet,
) Init(
	n Int,
) {
	parent := make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		parent[i] = i
	}
	rank := ds.Rank.Make(n, 0)
	size := ds.Size.Make(n, 1)
	ds.Parent = parent
	ds.Rank = rank 
	ds.Size = size
}


func (
	ds *DisjointSet,
) Find(
	u Int,
) (
	root Int,
) {
	parent := ds.Parent 
	v := parent[u]
	if v == u {
		root = u 
		return
	}
	root = ds.Find(v)
	parent[u] = root 
	return
}


func (
	ds *DisjointSet,
) Unite(
	u, v Int,
) {
	u = ds.Find(u)
	v = ds.Find(v)
	if u == v {
		return
	}
	u, v = ds.sort(u, v)
	rank := ds.Rank
	parent := ds.Parent 
	size := ds.Size 
	parent[v] = u 
	size[u] += size[v]
	rank[u] = Max(
		rank[u],
		rank[v] + 1,
	).(Int)
}


func (
	ds *DisjointSet,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	rank := ds.Rank
	if rank[u] < rank[v] {
		u, v = v, u 
	}
	return u, v 	
}


func (
	ds *DisjointSet,
) Same(
	u, v Int,
) (
	Bool,
) {
	u = ds.Find(u)
	v = ds.Find(v)
	return u == v 
}