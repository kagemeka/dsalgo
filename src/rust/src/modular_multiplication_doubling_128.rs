/// a*b = a + a + ... (k count of a) -> doubling
pub fn mod_mul_doubling_128(mut a: u128, mut b: u128, m: u128) -> u128 {
    let mut res = 0;
    while b > 0 {
        if b & 1 == 1 {
            res = (res + a) % m;
        }
        a = (a << 1) % m;
        b >>= 1;
    }
    res
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::*;
        let a = 1234567890123456789u128;
        let m = 1u128 << 100;
        assert_eq!(
            mod_mul_doubling_128(a, a, m),
            a * a % m,
        );
    }
}
