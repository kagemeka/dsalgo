package dsalgo

func SieveOfEratosthenes(size int) []int {
	primes := make([]int, 0, size>>4)
	if size <= 2 {
		return primes
	}
	primes = append(primes, 2)
	is_prime := MakeSlice(size>>1, true)
	for i := 3; i < size; i += 2 {
		if !is_prime[i>>1] {
			continue
		}
		primes = append(primes, i)
		for j := i * i >> 1; j < size>>1; j += i {
			is_prime[j] = false
		}
	}
	return primes
}
