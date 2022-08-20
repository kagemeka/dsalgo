use crate::chinese_remainder_theorem_extended_euclidean_gcd_safe_usize::*;
pub fn crt_reduce(mr: &[(usize, usize)]) -> Option<(usize, usize)> {
    let (mut m0, mut r0) = (1, 0);
    for &(m1, r1) in mr.iter() {
        let (lcm, ans) = safe_crt(m0, r0, m1, r1)?;
        m0 = lcm;
        r0 = ans;
        debug_assert!(r0 < m0);
    }
    Some((m0, r0))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![(vec![(5, 3), (7, 4), (8, 3)], Some((280, 123)))];
        for (mr, ans) in cases {
            assert_eq!(crt_reduce(&mr), ans);
        }
    }
}
