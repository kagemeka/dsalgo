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
        pub fn with_rand(epochs: u8) -> Self {
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
