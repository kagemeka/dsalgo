//! Analysis Root Finding Algorithm
//! for given f(x), find x such that f(x) = 0
pub mod newton {
    //! Newton's Method
    //! f(x) must be differentiabl and f'(x) != 0
    //! example
    //! f(x) = x^2 - 10.
    //! f'(x) = 2x
    //! x = 3.16227...
    //! TODO: use generic instead of f64 accepting int, big-rational, etc.
    /// tol:  absolute tolerance
    /// rtol: relative tolerance
    #[derive(Default)]
    pub struct Options {
        pub tol: Option<f64>,
        pub rtol: Option<f64>,
        pub max_iter: Option<u8>,
    }
    impl Options {
        pub fn new(
            tol: Option<f64>, rtol: Option<f64>, max_iter: Option<u8>,
        ) -> Self {
            Self { tol, rtol, max_iter }
        }
    }
    /// f := f(x)
    /// fp := f'(x)
    /// x0 := initial guess
    /// Err(x) if not terminated in max iterations.
    pub fn root<F, D>(
        f: &F, fp: &D, x0: f64, opts: Option<Options>,
    ) -> Result<f64, f64>
    where
        F: Fn(f64) -> f64,
        D: Fn(f64) -> f64,
    {
        const MAX_ITER: u8 = 1 << 6;
        let opts = opts.unwrap_or_default();
        let tol = opts.tol.unwrap_or_default();
        let rtol = opts.rtol.unwrap_or_default();
        let max_iter = opts.max_iter.unwrap_or(MAX_ITER);
        assert!(0. <= tol);
        assert!(0. <= rtol && rtol < 1.);
        let mut x = x0;
        for _ in 0..max_iter {
            let d = f(x) / fp(x);
            x -= d;
            if d.abs() < tol && (d / x).abs() < rtol {
                return Ok(x);
            }
        }
        Err(x)
    }
    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {
            use super::*;
            let n = 51628730198202384.;
            let f = |x: f64| x * x - n;
            let fp = |x: f64| 2. * x;
            let x = root(&f, &fp, 100_000_000., None);
            let x = x.unwrap_err();
            assert_eq!(x as u64, 227219563); // 227219563.854...
        }
    }
    // TODO:
    /// newton's method for 2D function
    pub fn newton2d() {}
}
pub mod isqrt {
    //! integer sqrt
    pub fn naive(n: u64) -> u64 {
        (1..1 << 32).find(|&x| x * x > n).unwrap_or(1 << 32) - 1
    }
    // linear with addition
    pub fn linear_with_addition(n: u64) -> u64 {
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
    pub fn linear_with_subtraction(n: u64) -> u64 {
        let mut a = 5 * n;
        let mut b = 5;
        while a >= b {
            a -= b;
            b += 10;
        }
        b / 10
    }
    /// binary search
    pub fn binary_search(n: u64) -> u64 {
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
    pub fn digit_by_digit_recurse(n: u64) -> u64 {
        if n < 2 {
            return n;
        }
        let x = digit_by_digit_recurse(n >> 2) << 1;
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
    pub fn floor(n: u64) -> u64 { binary_search(n) }
    pub fn ceil(n: u64) -> u64 {
        let x = binary_search(n);
        if x * x == n { x } else { x + 1 }
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_naive() {
            let res = (0..10).map(|x| naive(x)).collect::<Vec<_>>();
            assert_eq!(res, [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]);
        }
        #[test]
        fn test_add() {
            for i in 0..1000 {
                assert_eq!(linear_with_addition(i), naive(i));
            }
        }
        #[test]
        fn test_sub() {
            for i in 0..1000 {
                assert_eq!(linear_with_subtraction(i), naive(i));
            }
        }
        #[test]
        fn test_binary_search() {
            for i in 0..1000 {
                assert_eq!(binary_search(i), naive(i));
            }
            assert_eq!(binary_search(0), 0);
            assert_eq!(binary_search(1), 1);
            assert_eq!(binary_search(3), 1);
            assert_eq!(binary_search(4), 2);
            assert_eq!(binary_search(99), 9);
            assert_eq!(binary_search(100), 10);
            assert_eq!(binary_search(120), 10);
        }
        #[test]
        fn test_dd() {
            for i in 0..1000 {
                assert_eq!(digit_by_digit_recurse(i), naive(i));
            }
        }
        #[test]
        fn test_newton() {
            for i in 0..1000 {
                assert_eq!(newton(i), naive(i));
            }
        }
    }
}
pub mod ikthrt {
    //! integer kth root
}
