package combinatorics


/* cut below */



type Permutations struct {
	S Slice
	Ch chan Slice
	bufSize Int
	r Int 
	i int
}


func (
	p *Permutations,
) Set(
	s Slice,
) {
	p.S = s
	const bufSize = 1 << 0
	p.Ch = make(
		chan Slice, 
		bufSize,
	)
}


func (
	p *Permutations,
) Gen(
	r Int,
) {
	p.r = r
	p.i = 0
	p.genSupport()
	close(p.Ch)
}


func (
	p *Permutations,
) genSupport() {
	s := p.S
	r := p.r
	i := p.i
	if Int(i) == r {
		var ch chan<- Slice = p.Ch
		ch <- s.Sub(0, r)
		return 
	}
	n := s.Len()
	for j := i; j < n; j++ {
		s.Swap(i, j)
		p.S = s.Clone()
		p.i = i + 1
		p.genSupport()
	}
}



func Permute(
	s Slice,
	r Int,
) (
	ch <-chan Slice,
) {
	p := new(Permutations)
	p.Set(s)
	go p.Gen(r)
	ch = p.Ch
	return
}



func (
	a IntSlice,
) Perm(
	r Int,
) (
	ch <-chan IntSlice,
) {
	p := Permute(a, r)
	ch = a.ChTransPort(p)
	return 
}



func (
	n Int,
) Perm(
	r Int,
) (
	ch <-chan IntSlice,
) {
	a := make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		a[i] = i
	}
	ch = a.Perm(r)
	return 
}