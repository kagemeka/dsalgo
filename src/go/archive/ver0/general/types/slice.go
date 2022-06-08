package types 


/* cut below */



type Slice interface {
	Len() int
	Swap(int, int)
	Clone() Slice
	Sub(Int, Int) Slice
	At(Int) interface{}
	Pushed(
		x interface{},
	) Slice
}


func Reverse(
	s Slice,
) {
	n := s.Len()
	for i := 0; i < n /2; i++ {
		s.Swap(i, n - i - 1)
	}
}


func Reversed(
	s Slice,
) Slice {
	s = s.Clone()
	Reverse(s)
	return s
}