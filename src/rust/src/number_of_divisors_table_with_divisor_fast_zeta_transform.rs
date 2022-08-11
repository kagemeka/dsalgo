use crate::sieve_of_eratosthenes_enumerate_primes_usize::enumerate_primes;
/// d(n) table. d(0) := 0 here.
/// O(N\log{\log{N}})
pub fn number_of_divisors(size: usize) -> Vec<u64> {
    let mut cnt = vec![1; size];
    cnt[0] = 0;
    for p in enumerate_primes(size) {
        for i in 1..(size - 1) / p + 1 {
            cnt[i * p] += cnt[i];
        }
    }
    cnt
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::*;
        assert_eq!(number_of_divisors(10), [0, 1, 2, 2, 3, 2, 4, 2, 4, 3]);
    }
}
