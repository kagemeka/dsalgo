package modular


func TestModular() {
	var mod Int = 1_000_000_007

	var n int = 100
	a := make([]Modular, n)
	for i := 0; i < n; i++ {
		a[i] = Modular{
			Int(i),
			mod,
	}
	}
	a[0] = Modular{1, mod}
	for i := 0; i < n-1; i++ {
		a[i+1].IAdd(a[i])
	}
	for _, v := range a {
		fmt.Println(v)
	}
	fmt.Println(a)

	m := Modular{
		Int(n),
		mod,
	}
	f := m.Factorial()
	fmt.Println(f)
	invF := m.InverseFactorial()
	fmt.Println(invF)

	g := f[0].Div(f[2])
	fmt.Println(g)
	g = f[0].Neg()
	fmt.Println(g)
	g = Modular{2, mod}
	fmt.Println(g.Pow(100))
	g.IPow(100)
	fmt.Println(g)
}
