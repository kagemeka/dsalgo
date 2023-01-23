/// number of a prime factor in factorial.

pub fn legendre(
    n: usize,
    p: usize,
) -> usize {
    if n == 0 {
        0
    } else {
        n / p + legendre(n / p, p)
    }
}

#[cfg(test)]

mod tests {

    use super::*;

    #[test]

    fn test() {
        use crate::sieve_of_eratosthenes_prime_factorize_factorial::*;

        let n = 100_000;

        let factors = factorize_factorial(n);

        for (p, e) in factors {
            assert_eq!(legendre(n, p), e);
        }
    }
}
