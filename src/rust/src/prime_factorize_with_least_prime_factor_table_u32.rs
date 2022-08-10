use crate::least_prime_factor_table_with_sieve_of_eratosthenes_u32::*;
pub struct PrimeFactorize {
    lpf: Vec<Option<u32>>,
}
impl PrimeFactorize {
    pub fn new(size: usize) -> Self { Self { lpf: least_prime_factor(size) } }

    pub fn factorize(&self, mut n: u32) -> Vec<(u32, u32)> {
        assert!((n as usize) < self.lpf.len());
        let mut factors = vec![];
        let mut prime = 0;
        let mut cnt = 0;
        while n > 1 {
            let p = self.lpf[n as usize].unwrap();
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
    #[test]
    fn test() {}
}
