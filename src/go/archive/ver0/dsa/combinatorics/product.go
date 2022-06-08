package combinatorics


/* cut below */



type Product struct {
	S Slice
	Ch chan Slice
	bufSize Int 
	r Int
	a Slice
}


func (
	p *Product,
) Set(
	s Slice,
) {
	p.S = s
	const bufSize = 1 << 0
	p.Ch = make(
		chan Slice, 
		bufSize,
	)
	p.a = s.Clone().Sub(0, 0)
}


func (
	p *Product,
) Gen(
	r Int,
) {
	p.r = r
	p.genSupport()
	close(p.Ch)
}


func (
	p *Product,
) genSupport() {
	r := p.r
	a := p.a
	n := Int(a.Len())
	if n == r {
		var ch chan<- Slice = p.Ch
		ch <- a
		return
	}
	s := p.S
	n = Int(s.Len())
	for i := Int(0); i < n; i++ {
		p.a = a.Pushed(s.At(i))
		p.genSupport()
	}
}



func Prod(
	s Slice,
	r Int,
) (
	ch <-chan Slice,
) {
	p := new(Product)
	p.Set(s)
	go p.Gen(r)
	ch = p.Ch 
	return
}



func (
	a IntSlice,
) Prod(
	r Int,
) (
	ch <-chan IntSlice,
) {
	p := Prod(a, r)
	ch = a.ChTransPort(p)
	return 
}



func (
	n Int,
) Prod(
	r Int,
) (
	ch <-chan IntSlice,
) {
	a := make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		a[i] = i
	}
	ch = a.Prod(r)
	return
}