package cp


//

type Problem struct {
	io *IO
}


func (
	p *Problem,
) Init() {
	p.io := new(IO)
	p.io.Init()
	p.io = io
}


func (
	p *Problem,
) Prepare() {
}


func (
	p *Problem,
) Solve() {
}



func main() {
	p := new(Problem)
	p.Init()
	t := 1
	// t = p.io.Int()
	for i := 0; i < t; i++ {
		Run(p)
	}
}
