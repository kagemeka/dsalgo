use crate::modular_cumprod_i64::*;
pub fn factorial(
    m: i64,
    size: usize,
) -> Vec<i64> {
    let mut a: Vec<_> = (0..size as i64).collect();
    a[0] = 1;
    cumprod(m, a)
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let m = 1_000_000_007;
        let fact = factorial(m, 20);
        assert_eq!(
            fact,
            [
                1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
                39916800, 479001600, 227020758, 178290591, 674358851,
                789741546, 425606191, 660911389, 557316307,
            ]
        );
    }
}
