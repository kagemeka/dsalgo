/// modular division
pub fn divmod(a: i64, b: i64) -> (i64, i64) {
    assert!(b != 0);
    let (mut q, mut r) = (a / b, a % b);
    if b.signum() * r.signum() == -1 {
        q -= 1;
        r += b;
    }
    (q, r)
}

/// euclid division
pub fn divrem_euclid(a: i64, b: i64) -> (i64, i64) {
    (
        a.div_euclid(b),
        a.rem_euclid(b),
    )
}

pub fn ceil_div(mut a: i64, mut b: i64) -> i64 {
    if b < 0 {
        a = -a;
        b = -b;
    }
    divmod(a + b - 1, b).0
}

pub fn floor_div(mut a: i64, mut b: i64) -> i64 {
    if b < 0 {
        a = -a;
        b = -b;
    }
    divmod(a, b).0
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_divrem() {
        assert_eq!(divrem_euclid(10, 3), (3, 1));
        assert_eq!(divrem_euclid(10, -3), (-3, 1));
        assert_eq!(divrem_euclid(-10, 3), (-4, 2));
        assert_eq!(divrem_euclid(-10, -3), (4, 2));
    }

    #[test]
    fn test_divmod() {
        assert_eq!(divmod(10, 3), (3, 1));
        assert_eq!(divmod(10, -3), (-4, -2));
        assert_eq!(divmod(-10, 3), (-4, 2));
        assert_eq!(divmod(-10, -3), (3, -1));
    }

    #[test]
    fn test_ceil_div() {
        assert_eq!(ceil_div(10, 3), 4);
        assert_eq!(ceil_div(10, -3), -3);
        assert_eq!(ceil_div(-10, 3), -3);
        assert_eq!(ceil_div(-10, -3), 4);
    }

    #[test]
    fn test_floor_div() {
        assert_eq!(floor_div(10, 3), 3);
        assert_eq!(floor_div(10, -3), -4);
        assert_eq!(floor_div(-10, 3), -4);
        assert_eq!(floor_div(-10, -3), 3);
    }
}
