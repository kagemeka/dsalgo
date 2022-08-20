use crate::extended_euclidean_gcd_i64_recurse::extgcd;
pub fn crt(mr: &[(i64, i64)]) -> Option<(i64, i64)> {
    let (mut m, mut r) = (1, 0);
    for &(m1, mut r1) in mr.iter() {
        assert!(m1 > 0);
        r1 %= m1;
        let (g, inv_u, _) = extgcd(m, m1);
        if (r1 - r) % g != 0 {
            return None;
        }
        let u1 = m1 / g;
        let x = (r1 - r) / g * inv_u % u1;
        r += x * m;
        m *= u1;
    }
    if r < 0 {
        r += m;
    }
    debug_assert!(0 <= r && r < m);
    Some((m, r))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![(vec![(5, 3), (7, 4), (8, 3)], Some((280, 123)))];
        for (mr, ans) in cases {
            assert_eq!(crt(&mr), ans);
        }
    }
}
