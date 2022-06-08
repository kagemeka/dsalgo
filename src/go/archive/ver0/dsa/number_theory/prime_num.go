package number_theory


/* cut below */



type PrimeNum struct {
	Values IntSlice
	IsPrime BoolSlice
	n, i Int
}


func (
	pn *PrimeNum,
) Init(
	n Int,
) {
	pn.n = n
	pn.SieveOfEratosthenes()
	pn.Sparse()
}


func (
	pn *PrimeNum,
) SieveOfEratosthenes() {
	n := pn.n
	isPrime := pn.IsPrime.Make(
		n,
		true,
	)
	isPrime[0] = false
	isPrime[1] = false
	pn.IsPrime = isPrime
	for
	i := Int(0);
	i * i < n;
	i++ {
		if !isPrime[i] {
			continue
		}
		pn.i = i
		pn.sieveSupport()
	}
}


func (
	pn *PrimeNum,
) sieveSupport() {
	n, i := pn.n, pn.i
	isPrime := pn.IsPrime
	for
	j := Int(i * 2);
	j < n;
	j += i {
		isPrime[j] = false
	}
}


func (
	pn *PrimeNum,
) Sparse() {
	primeNums := pn.Values.Make(
		0,
		0,
	)
	isPrime := pn.IsPrime
	for i, ok := range isPrime {
		if !ok {
			continue
		}
		primeNums = append(
			primeNums,
			Int(i),
		)
	}
	pn.Values = primeNums
}


func (
	pn *PrimeNum,
) Get(
	i Int,
) (
	v Int,
) {
	v = pn.Values[i]
	return
}
