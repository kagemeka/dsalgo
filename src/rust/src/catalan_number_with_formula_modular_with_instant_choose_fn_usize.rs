pub fn catalan_number<F, G>(p: usize, choose: F, inv: G, n: usize) -> usize
where
    F: Fn(usize, usize, usize) -> usize,
    G: Fn(usize, usize) -> usize,
{
    inv(p, n) * choose(p, n << 1, n)
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() { let p = 1_000_000_007; }
}
