//! extended euclidean algorithms

pub fn extgcd_recurse(a: i64, b: i64) -> (u64, i64, i64) {
    if b == 0 {
        return if a < 0 { ((-a) as u64, -1, 0) } else { (a as u64, 1, 0) };
    }
    let (g, s, t) = extgcd_recurse(b, a % b);
    (g, t, s - a / b * t)
}

pub fn extgcd(mut a: i64, mut b: i64) -> (u64, i64, i64) {
    let (mut x00, mut x01, mut x10, mut x11) = (1, 0, 0, 1);
    while b != 0 {
        let q = a / b;
        // (x00, x01) = (x01, x00 - q * x01);
        // (x10, x11) = (x11, x10 - q * x11);
        // (a, b) = (b, a % b);
        x00 -= q * x01;
        std::mem::swap(&mut x00, &mut x01);
        x10 -= q * x11;
        std::mem::swap(&mut x10, &mut x11);
        a %= b;
        std::mem::swap(&mut a, &mut b);
    }
    if a < 0 {
        a = -a;
        x00 = -x00;
        x10 = -x10;
    }
    (a as u64, x00, x10)
}

/// compute g := \gcd(modulus, n),
/// and modular inverse of n/g in Z_{modulus/g}.
/// we convert parameters to i64 internally.
/// so be careful not to pass modulus > 2^63 because it overflows.
/// it's `trivial` that inverse of 0 is undefined, so if n = 0, it panics.
pub fn mod_gcd_inv(modulus: u64, n: u64) -> (u64, u64) {
    assert!(0 < n && n < modulus);
    let (mut a, mut b) = (n as i64, modulus as i64);
    let (mut x00, mut x01) = (1, 0);
    while b != 0 {
        // (x00, x01) = (x01, x00 - a / b * x01);
        // (a, b) = (b, a % b);

        x00 -= a / b * x01;
        std::mem::swap(&mut x00, &mut x01);
        a %= b;
        std::mem::swap(&mut a, &mut b);
    }
    let gcd = a as u64;
    let u = (modulus / gcd) as i64;
    if x00 < 0 {
        x00 += u;
    }
    debug_assert!(0 <= x00 && x00 < u);
    (gcd, x00 as u64)
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_mod_gcd_inv() {
        // euclidean_mod_gcd_inv(10, 0); // runtime error.
        assert_eq!(mod_gcd_inv(5, 2), (1, 3));
        assert_eq!(mod_gcd_inv(18, 12), (6, 2));
        assert_eq!(mod_gcd_inv(111, 30), (3, 26));
        // gcd(111, 30) = 3
        // 111 / 3 = 37, 30 / 3 = 10, 10^{-1} \equiv 26 \mod 37
    }

    #[test]
    fn test_extgcd() {
        assert_eq!(
            extgcd_recurse(-30, 111),
            (3, 11, 3)
        );
        assert_eq!(extgcd_recurse(0, 0), (0, 1, 0));
        assert_eq!(extgcd(-30, 111), (3, 11, 3));
        assert_eq!(extgcd(111, 30), (3, 3, -11));
        assert_eq!(extgcd(0, 0), (0, 1, 0));
    }
}
