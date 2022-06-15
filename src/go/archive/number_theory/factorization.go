package number_theory


/* cut below */



type Factorization struct{
	primeNums IntSlice
	n, p Int
	factors, fFactors MII
}


func (
	f *Factorization,
) Init(
	n Int,
) {
	pn := new(PrimeNum)
	pn.Init(n)
	f.primeNums = pn.Values
}


func (
	f *Factorization,
) Calc(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.factors = factors
	primeNums := f.primeNums
	for _, p := range primeNums {
		if n < 2 {return}
		if p * p > n {
			break
		}
		f.n, f.p = n, p
		f.calcSupport()
		n = f.n
	}
	factors[n]++
	return
}


func (
	f *Factorization,
) calcSupport() {
	n, p := f.n, f.p
	factors := f.factors
	for n % p == 0 {
		factors[p]++
		n /= p
	}
	f.n = n
}


func (
	f *Factorization,
) Factorial(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.fFactors = factors
	for
	i := Int(1); i < n + 1; i++ {
		f.n = i
		f.factorialSupport()
	}
	return
}


func (
	f *Factorization,
) factorialSupport() {
	n := f.n
	factors := f.fFactors
	for p, c := range f.Calc(n) {
		factors[p] += c
	}
}
