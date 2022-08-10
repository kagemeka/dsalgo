use crate::sieve_of_eratosthenes_least_prime_factor_table_direct_usize_optim::*;
pub struct PrimeFactorize(Vec<usize>);
impl PrimeFactorize {
    pub fn new(size: usize) -> Self { Self(least_prime_factor(size)) }

    pub fn factorize(&self, mut n: usize) -> Vec<(usize, usize)> {
        assert!(n < self.0.len());
        let mut factors = vec![];
        let mut prime = 0;
        let mut cnt = 0;
        while n > 1 {
            let p = self.0[n];
            n /= p;
            if p == prime {
                cnt += 1;
                continue;
            }
            if cnt > 0 {
                factors.push((prime, cnt));
            }
            prime = p;
            cnt = 1;
        }
        if cnt > 0 {
            factors.push((prime, cnt));
        }
        factors
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        use crate::prime_factorize_trial_division_usize::prime_factorize;
        let f = PrimeFactorize::new(1 << 10);
        for i in 1..1 << 10 {
            assert_eq!(f.factorize(i), prime_factorize(i));
        }
    }
}
