/// generalized greatest common divisor on commutative ring R.
/// gcd(a, b) might not be unique neither exist.
/// if R does not have Order property.
pub trait GCD {
    type T;
    fn gcd(_: Self::T, _: Self::T) -> Self::T;
}
pub mod int {
    //! greatest common divisor on integer gcd(a, b)
    //! a, b \in \Z.
    //! 0 := identity element and empty product here.
    //! gcd(0, 0) := 0
    //! \prod_{\emptyset} := 0
    pub trait Base: Default + PartialEq + Copy {}
    impl<T> Base for T where T: Default + PartialEq + Copy {}
    pub fn euclid<T>(mut a: T, mut b: T) -> T
    where
        T: Base + PartialOrd + std::ops::SubAssign,
    {
        let zero = T::default();
        assert!(zero < a && zero < b);
        loop {
            if a < b {
                std::mem::swap(&mut a, &mut b);
            }
            if b == zero {
                return a;
            }
            a -= b;
        }
    }
    pub fn euclidean<T>(mut a: T, mut b: T) -> T
    where
        T: Base + std::ops::RemAssign,
    {
        let zero = T::default();
        while b != zero {
            a %= b;
            std::mem::swap(&mut a, &mut b);
        }
        a
    }
    pub fn euclidean_recurse<T>(a: T, b: T) -> T
    where
        T: Base + std::ops::Rem<Output = T>,
    {
        if b == T::default() { a } else { euclidean_recurse(b, a % b) }
    }
    pub fn euclidean_signed<T>(a: T, b: T) -> T
    where
        T: Base + std::ops::RemAssign + PartialOrd + std::ops::Neg<Output = T>,
    {
        let mut g = euclidean(a, b);
        if g < T::default() {
            g = -g;
        }
        g
    }
    pub fn gcd_reduce<T, I>(iter: I) -> T
    where
        I: Iterator<Item = T>,
        T: Base + std::ops::RemAssign + PartialOrd,
    {
        iter.fold(T::default(), |a, b| euclidean(a, b))
    }
    // TODO: not implemented
    pub fn by_prime_factorize() {}
    // TODO: not implemented
    pub fn lehmer() {}
    // TODO: not implemented
    pub fn binary_gcd() {}
    // TODO: not implemented
    /// with Thomae's Function
    pub fn thomae() {}
    #[cfg(test)]
    mod tests {
        use super::*;
        const CASES: &[(&[i32], i32)] = &[
            (&[], 0),
            (&[0], 0),
            (&[10], 10),
            (&[0, 2, 8, 4], 2),
            (&[33, -111], 3),
            (&[-33, 111], 3),
            (&[-33, -111], 3),
            (&[100, -3], 1),
            (&[-1, 0], 1),
            (&[10, 5], 5),
            (&[0, 10], 10),
        ];
        fn test_2<F>(gcd: &F, a: i32, b: i32, expected: i32)
        where
            F: Fn(i32, i32) -> i32,
        {
            let mut g = gcd(a, b);
            if g < 0 {
                g = -g;
            }
            assert_eq!(g, expected);
        }
        #[test]
        fn test_euclidean() {
            for &(v, ans) in CASES {
                if v.len() != 2 {
                    continue;
                }
                test_2(&euclidean, v[0], v[1], ans);
            }
        }
        #[test]
        fn test_euclidean_recurse() {
            for &(v, ans) in CASES {
                if v.len() != 2 {
                    continue;
                }
                test_2(&euclidean_recurse, v[0], v[1], ans);
            }
        }
        #[test]
        fn test_reduce() {
            for &(values, ans) in CASES {
                assert_eq!(gcd_reduce(values.iter().cloned()).abs(), ans);
            }
        }
    }
}
