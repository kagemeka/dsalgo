pub fn gcd(a: i64, b: i64) -> i64 { if b == 0 { a } else { gcd(b, a % b) } }
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {}
}
