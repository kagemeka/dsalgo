package topology 

/* cut below */



type FloydWarshall struct {
	G Graph
	Dist IntMatrix
	src, mid, dst int
}


func (
	fw *FloydWarshall,
) SetGraph(
	g Graph,
) {
	fw.G = g
}


func (
	fw *FloydWarshall,
) Prepare(
	inf Int,
) {
	n := fw.G.Size()
	dist := fw.Dist.Make(
		n,
		n,
		inf,
	)
	fw.Dist = dist 
	for i := Int(0); i < n; i++ {
		fw.prepareSupport(i)
	}
	for i := Int(0); i < n; i++ {
		dist[i][i] = 0
	}
}


func (
	fw *FloydWarshall,
) prepareSupport(
	i Int,
) {
	g := &fw.G
	dist := fw.Dist
	for 
	_, e := range g.Edges[i] {
		j := e.To 
		d := e.Weight
		dist[i][j] = Min(
			dist[i][j],
			d,
		).(Int)
	}
}


func (
	fw *FloydWarshall,
) Search() {
	n := len(fw.Dist)
	for k := 0; k < n; k++ {
		fw.mid = k
		fw.searchSupport0()
	}	
}


func (
	fw *FloydWarshall,
) searchSupport0() {
	n := len(fw.Dist)
	for i := 0; i < n; i++ {
		fw.src = i
		fw.searchSupport1()
	}
}


func (
	fw *FloydWarshall,
) searchSupport1() {
	n := len(fw.Dist)
	k, i := fw.mid, fw.src
	d := fw.Dist 
	for j := 0; j < n; j++ {
		d[i][j] = Min(
			d[i][j],
			d[i][k] + d[k][j],
		).(Int)
	}
}