package cp


/* cut below */



type Solver interface{
	Init()
	Prepare()
	Solve()
}


func Run(s Solver) {
	s.Init()
	s.Prepare()
	s.Solve()
}



type Problem struct {
	io *IO
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	const bufSize = 1 << 7
	io.SetScanBuf(bufSize)
	p.io = io
}


func (
	p *Problem,
) Prepare() {
	io := p.io
}


func (
	p *Problem,
) Solve() {
	io := p.io
}
