//! least common multiple
use crate::gcd::int::euclidean as gcd;
// TODO: without GCD
/// with gcd
pub fn lcm(a: u64, b: u64) -> u64 {
    if a == 0 && b == 0 { 0 } else { a / gcd(a, b) * b }
}
/// with gcd
pub fn lcm_reduce<I>(iter: I) -> u64
where
    I: Iterator<Item = u64>,
{
    iter.fold(1, |a, b| lcm(a, b))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        assert_eq!(lcm(0, 0), 0);
        assert_eq!(lcm(1, 0), 0);
        assert_eq!(lcm(12, 18), 36);
    }
}
