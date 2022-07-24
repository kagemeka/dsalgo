pub fn log(base: u64, x: u64) -> u8 {
    if x >= base { 1 + log(base, x / base) } else { 0 }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        for b in 2u64..1000 {
            for x in 1u64..10000 {
                assert_eq!(log(b, x) as u32, x.log(b));
            }
        }
    }
}
