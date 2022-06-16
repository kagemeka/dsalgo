fn main() {
    // use crate::{monoid_self::Monoid, static_segment_tree::SegmentTree};

    // struct Add;
    // impl Monoid<Add> for i32 {
    //     fn operate(lhs: Self, rhs: Self) -> Self { lhs + rhs }

    //     fn identity() -> Self { 0 }
    // }

    // struct Xor;
    // impl Monoid<Xor> for i32 {
    //     fn operate(lhs: Self, rhs: Self) -> Self { lhs ^ rhs }

    //     fn identity() -> Self { 0 }
    // }

    // let seg = SegmentTree::<i32>::new::<Xor>(5);
    // println!("{:?}", seg);

    // let g: u32 = gcd::int::gcd(-33, 111) as u32;

    println!("{}", (-1i32 << 1));
}

pub mod static_segment_tree {
    use crate::monoid_self::Monoid;

    #[derive(Debug)]
    pub struct SegmentTree<S> {
        size: usize,
        data: Vec<S>,
    }

    impl<S> SegmentTree<S> {
        pub fn new<Id>(size: usize) -> Self
        where
            S: Monoid<Id> + Clone,
        {
            let data = vec![S::identity(); size];
            Self { size, data }
        }
    }
}

pub mod gcd {
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

        pub fn gcd<T>(mut a: T, mut b: T) -> T
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

        pub fn recurse<T>(a: T, b: T) -> T
        where
            T: Base + std::ops::Rem<Output = T>,
        {
            if b == T::default() { a } else { recurse(b, a % b) }
        }

        pub fn signed<T>(a: T, b: T) -> T
        where
            T: Base
                + std::ops::RemAssign
                + PartialOrd
                + std::ops::Neg<Output = T>,
        {
            let mut g = gcd(a, b);
            if g < T::default() {
                g = -g;
            }
            g
        }

        pub fn gcd_reduce<T, I>(iter: I) -> T
        where
            I: Iterator<Item = T>,
            T: Base
                + std::ops::RemAssign
                + PartialOrd
                + std::ops::Neg<Output = T>,
        {
            iter.fold(T::default(), |a, b| {
                signed(a, b)
            })
        }

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
            fn test_gcd() {
                for &(v, ans) in CASES {
                    if v.len() != 2 {
                        continue;
                    }
                    test_2(&gcd, v[0], v[1], ans);
                }
            }

            #[test]
            fn test_recurse() {
                for &(v, ans) in CASES {
                    if v.len() != 2 {
                        continue;
                    }
                    test_2(&recurse, v[0], v[1], ans);
                }
            }

            #[test]
            fn test_reduce() {
                for &(values, ans) in CASES {
                    assert_eq!(
                        gcd_reduce(values.iter().cloned()),
                        ans
                    );
                }
            }
        }
    }
}

pub mod static_monoid {
    /// this has not operation id as generics.
    /// it should be controlled by the implementor.
    /// Example
    /// ```
    /// struct Int64Monoid<Id>;
    /// struct Add;
    /// impl Monoid for Int64Monoid<Add> {
    ///     type S = i64;
    ///
    ///     fn operate(lhs: Self::S, rhs: Self::S) -> Self::S { lhs + rhs }
    ///
    ///     fn identity() -> Self::S { 0 }
    /// }
    /// assert_eq!(Int64Monoid::identity(), 0);
    /// ```
    pub trait Monoid: Semigroup {
        fn identity() -> Self::S;
    }

    pub trait Magma {
        type S;
        fn operate(_: Self::S, _: Self::S) -> Self::S;
    }

    pub trait Semigroup: Magma {}
}

pub mod dynamic_monoid {

    pub trait Monoid {
        type S;
        fn operate(&self, lhs: Self::S, rhs: Self::S) -> Self::S;
        fn identity(&self) -> Self::S;
    }
}

pub mod monoid_self {
    //! unlike monoid `(S, *, e)`,
    //! monoid element `S as a (*, e)` is only static.
    //! because operation and identity must be common for all instances.

    /// operation-id is necessary.
    /// for example,
    /// if you implement monoid element trait for `i32`,
    /// the operation can be add, mul, xor, etc,
    /// and not unique.
    pub trait Monoid<Id> {
        fn operate(_: Self, _: Self) -> Self;
        fn identity() -> Self;
    }
}
