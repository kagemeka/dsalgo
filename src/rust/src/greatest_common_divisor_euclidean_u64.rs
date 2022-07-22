pub fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b > 0 {
        (a, b) = (b, a % b);
    }
    a
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {}
}
