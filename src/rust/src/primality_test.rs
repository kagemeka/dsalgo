pub mod mr {
    //! Miller Rabin's Test

    pub mod bases {
        //! deterministic Miller Rabin bases

        pub const B32: [u32; 3] = [2, 7, 61];

        pub const B64: [u64; 12] = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        ];

        pub const B64_FEW: [u64; 7] = [
            2,
            325,
            9_375,
            28_178,
            450_775,
            9_780_504,
            1_795_265_022,
        ];
    }

    pub struct FixedBases(Vec<u64>);

    impl Default for FixedBases {
        fn default() -> Self { Self::new(bases::B64_FEW.to_vec()) }
    }

    impl FixedBases {
        pub fn new(bases: Vec<u64>) -> Self { Self(bases) }

        // TODO: impl as common trait
        pub fn new_rand(epochs: u8) -> Self {
            use crate::rng_static_xorshift64::static_xorshift64;
            Self::new(
                (0..epochs).map(|_| static_xorshift64()).collect::<Vec<_>>(),
            )
        }

        pub fn is_prime(&self, n: u64) -> bool {
            use crate::{
                montgomery_modular_multiplication_64::*,
                power::pow_semigroup,
            };
            if n == 2 {
                return true;
            }
            if n < 2 || n & 1 == 0 {
                return false;
            }
            let s = (n - 1).trailing_zeros();
            let d = (n - 1) >> s;
            // n - 1 = 2^s*d
            let m = MontgomeryMultiplication64::new(n);
            let mul = |x, y| m.mul(x, y);

            let is_composite = |b| -> bool {
                assert!(n > 2 && n & 1 == 1 && 2 <= b && b < n - 1);
                let mut x = pow_semigroup(&mul, b, d);
                if x == 1 {
                    return false;
                }
                for _ in 0..s {
                    if x == n - 1 {
                        return false;
                    }
                    x = mul(x, x);
                }
                true // definite
            };
            // [2, n - 1)
            self.0
                .iter()
                .map(|&base| base % n)
                .filter(|&b| 2 <= b && b < n - 1)
                .all(|b| !is_composite(b))
            // strong probable prime.
        }
    }

    pub fn is_prime(n: u64) -> bool { FixedBases::default().is_prime(n) }

    #[cfg(test)]
    mod tests {
        #[test]
        fn test_mr() {
            use super::*;
            assert!(is_prime(998_244_353));
            assert!(is_prime(1_000_000_007));
            assert!(is_prime(1_000_000_007));
            assert!(!is_prime(561));
            assert!(!is_prime(512_461));
        }
    }
}

pub mod ss {
    //! solovay strassen's test

    use crate::{
        euler_criterion::try_euler_criterion,
        jacobi_symbol::jacobi_symbol,
    };

    pub fn is_composite_euler_jacobi(b: u64, n: u64) -> bool {
        assert!(n > 2 && n & 1 == 1 && 2 <= b && b < n);
        // 2 <= a because if a == 1, it's trivial jacobi = euler = 1.
        // compare jcobi symbol and euler's criterion.
        let jacobi = jacobi_symbol(n, b);
        if jacobi == 0 {
            return true;
        }
        if let Ok(euler) = try_euler_criterion(n, b) {
            let jacobi = if jacobi == 1 { 1 } else { n - 1 };
            euler != jacobi
        } else {
            true
        }
    }
    pub struct FixedBases(Vec<u64>);

    impl FixedBases {
        pub fn new(bases: Vec<u64>) -> Self { Self(bases) }

        // TODO: implement as common trait.
        pub fn new_rand(epochs: u8) -> Self {
            use crate::rng_static_xorshift64::static_xorshift64;
            Self::new(
                (0..epochs).map(|_| static_xorshift64()).collect::<Vec<_>>(),
            )
        }

        /// check whether n is Euler-Jacobi pseudo-prime or definite composite.
        pub fn is_prime(&self, n: u64) -> bool {
            if n == 2 {
                return true;
            }
            if n < 2 || n & 1 == 0 {
                return false;
            }
            // [2, n)
            self.0
                .iter()
                .map(|&base| base % n)
                .filter(|&b| 2 <= b && b < n)
                .all(|b| !is_composite_euler_jacobi(b, n))
        }
    }

    pub fn is_prime(n: u64, epochs: u8) -> bool {
        FixedBases::new_rand(epochs).is_prime(n)
    }

    // TODO:
    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {}
    }
}

pub mod mr_ss {
    //! Miller Rabin - Solovay Strassen's Test
}

pub mod fermat {
    //! Fermat's Test

    use crate::{
        gcd::int::euclidean as gcd,
        montgomery_modular_multiplication_64::MontgomeryMultiplication64,
        power::pow_semigroup,
    };

    pub struct FixedBases(Vec<u64>);

    impl FixedBases {
        pub fn new(bases: Vec<u64>) -> Self { Self(bases) }

        // TODO: implement as common trait.
        pub fn new_rand(epochs: u8) -> Self {
            use crate::rng_static_xorshift64::static_xorshift64;
            Self::new(
                (0..epochs).map(|_| static_xorshift64()).collect::<Vec<_>>(),
            )
        }

        pub fn is_prime(&self, n: u64) -> bool {
            if n == 2 {
                return true;
            }
            if n < 2 || n & 1 == 0 {
                return false;
            }
            let m = MontgomeryMultiplication64::new(n);
            let mul = |x, y| m.mul(x, y);
            let is_composite =
                |b| -> bool { pow_semigroup(&mul, b, n - 1) != 1 };
            // [2, n - 1)
            self.0
                .iter()
                .map(|&base| base % n)
                .filter(|&b| 2 <= b && b < n - 1)
                .all(|b| gcd(b, n) == 1 && !is_composite(b))
            // strong probable prime.
        }
    }

    pub fn is_prime(n: u64, epochs: u8) -> bool {
        FixedBases::new_rand(epochs).is_prime(n)
    }

    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {
            assert_eq!(
                super::is_prime(998_244_353, 10),
                true
            );
            assert_eq!(
                super::is_prime(1_000_000_007, 10),
                true
            );
            assert_eq!(super::is_prime(561, 10), false);
            assert_eq!(
                super::is_prime(512461, 10),
                false
            );
        }
    }
}
