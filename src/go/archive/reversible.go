package cp

//


type Reversible interface {
	Len() int
	Swap(i, j int)
}


func Reverse(
	a Reversible,
) {
	n := a.Len()
	for i := 0; i < n / 2; i++ {
		a.Swap(i, n - i - 1)
	}
}
