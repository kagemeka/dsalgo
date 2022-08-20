use crate::extended_euclidean_modular_gcd_inverse_usize_with_extgcd::*;
/// avoid overflows unless lcm(m0, m1) overflows.
pub fn safe_crt(
    mut m0: usize, mut r0: usize, mut m1: usize, mut r1: usize,
) -> Option<(usize, usize)> {
    use std::mem::swap;
    assert!(0 < m0 && 0 < m1);
    r0 %= m0;
    r1 %= m1;
    if r0 > r1 {
        swap(&mut r0, &mut r1);
        swap(&mut m0, &mut m1);
    }
    if m0 % m1 == 0 {
        // ((m1|m0 -> r1 <= r0) \land r0 <= r1) -> r0 = r1.
        return if r0 == r1 { Some((m0, r0)) } else { None };
    }
    let (g, inv_u0) = mod_gcd_inv(m1, m0 % m1);
    if (r1 - r0) % g != 0 {
        return None;
    }
    let u1 = m1 / g;
    let x = (r1 - r0) / g * inv_u0 % u1;
    let r = r0 + x * m0;
    let lcm = m0 * u1;
    debug_assert!(r1 <= r && r < lcm);
    Some((lcm, r))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        use crate::least_common_multiple_with_gcd_usize::lcm;
        let cases = vec![
            ((10, 3, 14, 7), 63),
            ((10, 3, 14, 6), -1),
            ((15, 2, 17, 8), 212),
            ((5, 3, 7, 4), 18),
            ((1, 0, 2, 0), 0),
            ((2, 0, 1, 0), 0),
        ];
        for ((m0, r0, m1, r1), r) in cases {
            let ans =
                if r < 0 { None } else { Some((lcm(m0, m1), r as usize)) };
            assert_eq!(safe_crt(m0, r0, m1, r1), ans);
        }
    }
}
