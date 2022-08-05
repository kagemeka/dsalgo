use crate::{
    legendre_function::legendre_function,
    sieve_of_eratosthenes_enumerate_primes::enumerate_primes,
};
pub fn prime_factorize_factorial_legendre(n: u32) -> Vec<(u32, u32)> {
    enumerate_primes(n + 1)
        .into_iter()
        .map(|p| (p, legendre_function(n as u64, p as u64) as u32))
        .collect()
}
// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
