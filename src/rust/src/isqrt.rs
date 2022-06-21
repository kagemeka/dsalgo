//! integer sqrt

pub fn naive(n: u64) -> u64 {
    (1..1 << 32).find(|&x| x * x > n).unwrap_or(1 << 32) - 1
}

// linear with addition
pub fn add(n: u64) -> u64 {
    let mut x = 0;
    let mut x2 = 0; // x^2
    let mut delta = 1; // x2 + delta = (x + 1)^2
    while x2 <= n {
        x += 1;
        x2 += delta;
        delta += 2;
    }
    x - 1
}

/// linear with subtraction
/// reference
/// https://en.wikipedia.org/wiki/Integer_square_root
pub fn sub(n: u64) -> u64 {
    let mut a = 5 * n;
    let mut b = 5;
    while a >= b {
        a -= b;
        b += 10;
    }
    b / 10
}

/// binary search
pub fn binsrch(n: u64) -> u64 {
    let mut lo = 0;
    let mut hi = std::cmp::min(n + 1, 1 << 32);
    while hi - lo > 1 {
        let x = (lo + hi) >> 1;
        if x * x <= n {
            lo = x;
        } else {
            hi = x;
        }
    }
    lo
}

// digit by digit
pub fn dbd(n: u64) -> u64 {
    if n < 2 {
        return n;
    }
    let x = dbd(n >> 2) << 1;
    if (x + 1).pow(2) <= n { x + 1 } else { x }
}

/// newton's method
pub fn newton(n: u64) -> u64 {
    let mut x0 = n >> 1;
    if x0 == 0 {
        return n;
    }
    loop {
        let x1 = (x0 + n / x0) >> 1;
        if x1 >= x0 {
            break;
        }
        x0 = x1;
    }
    x0
}

pub fn floor(n: u64) -> u64 { binsrch(n) }

pub fn ceil(n: u64) -> u64 {
    let x = binsrch(n);
    if x * x == n { x } else { x + 1 }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_naive() {
        let res = (0..10).map(|x| naive(x)).collect::<Vec<_>>();
        assert_eq!(
            res,
            [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
        );
    }

    #[test]
    fn test_add() {
        for i in 0..1000 {
            assert_eq!(add(i), naive(i));
        }
    }

    #[test]
    fn test_sub() {
        for i in 0..1000 {
            assert_eq!(sub(i), naive(i));
        }
    }

    #[test]
    fn test_binsrch() {
        for i in 0..1000 {
            assert_eq!(binsrch(i), naive(i));
        }
        assert_eq!(binsrch(0), 0);
        assert_eq!(binsrch(1), 1);
        assert_eq!(binsrch(3), 1);
        assert_eq!(binsrch(4), 2);
        assert_eq!(binsrch(99), 9);
        assert_eq!(binsrch(100), 10);
        assert_eq!(binsrch(120), 10);
    }
    #[test]
    fn test_dd() {
        for i in 0..1000 {
            assert_eq!(dbd(i), naive(i));
        }
    }
    #[test]
    fn test_newton() {
        for i in 0..1000 {
            assert_eq!(newton(i), naive(i));
        }
    }
}
