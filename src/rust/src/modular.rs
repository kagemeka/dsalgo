pub mod arithmetic {
    //! reference
    //! https://en.wikipedia.org/wiki/Modular_arithmetic#Properties
    pub trait Static {
        type T;
        fn modulus() -> Self::T;
        fn add(lhs: Self::T, rhs: Self::T) -> Self::T;
        fn neg(x: Self::T) -> Self::T;
        fn sub(lhs: Self::T, rhs: Self::T) -> Self::T {
            Self::add(lhs, Self::neg(rhs))
        }
        fn mul(lhs: Self::T, rhs: Self::T) -> Self::T;
        fn inv(x: Self::T) -> Self::T;
        fn div(lhs: Self::T, rhs: Self::T) -> Self::T {
            Self::mul(lhs, Self::inv(rhs))
        }
    }
    pub trait Dyn {
        type T;
        fn modulus(&self) -> Self::T;
        fn add(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
        fn neg(&self, x: Self::T) -> Self::T;
        fn sub(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
            self.add(lhs, self.neg(rhs))
        }
        fn mul(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
        fn inv(&self, x: Self::T) -> Self::T;
        fn div(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
            self.mul(lhs, self.inv(rhs))
        }
    }
    use crate::{modular::inv::extgcd as invert, static_modulus_trait::Get};
    /// why `default`?
    /// because there exists other modular arithmetic implementations.
    /// e.g. Montgomery Multiplication, or Burrett Reduction.
    #[derive(
        Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord, Default,
    )]
    pub struct DefaultStatic<T, M: Get<T = T>>(
        std::marker::PhantomData<(T, M)>,
    );
    macro_rules! impl_default_static {
        ($uint:ty, $mul_cast_uint:ty) => {
            impl<M: Get<T = $uint>> Static for DefaultStatic<$uint, M> {
                type T = $uint;

                fn modulus() -> Self::T { M::get() }

                fn add(lhs: Self::T, rhs: Self::T) -> Self::T {
                    assert!(lhs < M::get() && rhs < M::get());
                    let mut x = lhs;
                    x += rhs;
                    if x >= M::get() {
                        x -= M::get();
                    }
                    x
                }

                fn neg(x: Self::T) -> Self::T {
                    assert!(x < M::get());
                    if x == 0 { 0 } else { M::get() - x }
                }

                fn mul(lhs: Self::T, rhs: Self::T) -> Self::T {
                    let mut x = lhs as $mul_cast_uint;
                    x *= rhs as $mul_cast_uint;
                    x %= M::get() as $mul_cast_uint;
                    x as Self::T
                }

                fn inv(x: $uint) -> Self::T {
                    assert!(x > 0);
                    invert(M::get() as u64, x as u64).unwrap() as Self::T
                }
            }
        };
    }
    impl_default_static!(u32, u64);
    impl_default_static!(u64, u128);
    // TODO: change later. still not compile on AtCoder.
    // use crate::modular::modulus::ConstMod32;
    // #[allow(dead_code)]
    // pub type Modular1_000_000_007 =
    //     DefaultStatic<u32, ConstMod32<1_000_000_007>>;
    // #[allow(dead_code)]
    // pub type Modular998_244_353 =
    //     DefaultStatic<u32, ConstMod32<998_244_353>>;
    use crate::define_const_modulus_macro::{Mod1_000_000_007, Mod998_244_353};
    #[allow(dead_code)]
    pub type Modular1_000_000_007 = DefaultStatic<u32, Mod1_000_000_007>;
    #[allow(dead_code)]
    pub type Modular998_244_353 = DefaultStatic<u32, Mod998_244_353>;
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test() {
            use crate::modular::int::Modint;
            type Mint = Modint<u32, Modular1_000_000_007>;
            let a = Mint::from(1_000_000_008);
            assert_eq!(a.value(), 1);
        }
    }
}
pub mod inv {
    //! well-known modular inverse algorithms.
    /// inverse by Fermat's Little Theorem.
    /// for prime modulus.
    pub fn fermat() {
        // TODO:
    }
    /// inverse by Euler's Theorem.
    pub fn euler() {
        // TODO:
        // check gcd
        // return error if gcd != 1
        // or compute inverse with totient function.
        // related: carmichael_function.rs
    }
    use crate::extended_euclidean_modular_gcd_inverse_u64_direct::mod_gcd_inv;
    /// inverse by Extended Euclidean Algorithm.
    pub fn extgcd(modulus: u64, element: u64) -> Result<u64, &'static str> {
        let (gcd, inv) = mod_gcd_inv(modulus, element);
        if gcd == 1 {
            Ok(inv)
        } else {
            Err("modulus and element are not coprime")
        }
    }
}
pub mod int {
    use crate::modular::arithmetic::Static as Arithmetic;
    /// static modular element.
    /// modular element is only static.
    /// because all instances should be in the same arithmetic context.
    /// T should be u32 or u64.
    #[derive(
        Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default,
    )]
    pub struct Modint<T, M>
    where
        M: Arithmetic<T = T>,
    {
        value: M::T,
    }
    impl<T, M> std::fmt::Display for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        M::T: std::fmt::Display,
    {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            write!(f, "{}", self.value)
        }
    }
    impl<M: Arithmetic<T = u64>> Modint<u64, M> {
        pub fn new(mut v: u64) -> Self {
            if v >= M::modulus() {
                v %= M::modulus();
            }
            Modint { value: v }
        }
    }
    impl<M: Arithmetic<T = u32>> Modint<u32, M> {
        pub fn new(mut v: u32) -> Self {
            if v >= M::modulus() {
                v %= M::modulus();
            }
            Modint { value: v }
        }
    }
    impl<T, M> Modint<T, M>
    where
        M: Arithmetic<T = T>,
        M::T: Copy,
    {
        // TODO: make const
        pub fn value(&self) -> M::T { self.value }

        // pub fn new(value: M::T) -> Self { Self { value } }
        pub fn modulus() -> M::T { M::modulus() }
    }
    impl<T, M> std::ops::Add for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self::Output {
            self.value = M::add(self.value, rhs.value);
            self
        }
    }
    impl<T, M> std::ops::AddAssign for Modint<T, M>
    where
        M: Arithmetic<T = T> + Copy,
        T: Copy,
    {
        fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
    }
    impl<T, M> std::ops::Sub for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        type Output = Self;

        fn sub(mut self, rhs: Self) -> Self::Output {
            self.value = M::sub(self.value, rhs.value);
            self
        }
    }
    impl<T, M> std::ops::SubAssign for Modint<T, M>
    where
        M: Arithmetic<T = T> + Copy,
        T: Copy,
    {
        fn sub_assign(&mut self, rhs: Self) { *self = *self - rhs; }
    }
    impl<T, M> std::ops::Neg for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        type Output = Self;

        fn neg(mut self) -> Self::Output {
            self.value = M::neg(self.value);
            self
        }
    }
    impl<T, M> std::ops::Mul for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        type Output = Self;

        fn mul(mut self, rhs: Self) -> Self::Output {
            self.value = M::mul(self.value, rhs.value);
            self
        }
    }
    impl<T, M> std::ops::MulAssign for Modint<T, M>
    where
        M: Arithmetic<T = T> + Copy,
        T: Copy,
    {
        fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
    }
    impl<T, M> std::ops::Div for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        type Output = Self;

        fn div(mut self, rhs: Self) -> Self::Output {
            self.value = M::div(self.value, rhs.value);
            self
        }
    }
    impl<T, M> std::ops::DivAssign for Modint<T, M>
    where
        M: Arithmetic<T = T> + Copy,
        T: Copy,
    {
        fn div_assign(&mut self, rhs: Self) { *self = *self / rhs; }
    }
    impl<T, M> Modint<T, M>
    where
        M: Arithmetic<T = T> + Copy,
        T: Copy,
    {
        pub fn inv(mut self) -> Self {
            self.value = M::inv(self.value);
            self
        }
    }
    impl<M> From<i32> for Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
    {
        fn from(value: i32) -> Self { Self::from(value as i64) }
    }
    impl<M> From<i32> for Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
    {
        fn from(value: i32) -> Self { Self::from(value as i64) }
    }
    impl<M> From<i64> for Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
    {
        fn from(mut value: i64) -> Self {
            let m = M::modulus() as i64;
            if value < -m || value >= m {
                value %= m;
            }
            if value < 0 {
                value += m;
            }
            Self::new(value as u32)
        }
    }
    impl<M> From<i64> for Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
    {
        fn from(mut value: i64) -> Self {
            let m = M::modulus() as i64;
            if value < -m || value >= m {
                value %= m;
            }
            if value < 0 {
                value += m;
            }
            Self::new(value as u64)
        }
    }
    // TODO: move out From<T> from this file.
    // because these are extensions rather than core functionality.
    impl<M> From<u64> for Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
    {
        fn from(mut value: u64) -> Self {
            let m = M::modulus();
            if value >= m {
                value %= m;
            }
            Self::new(value)
        }
    }
    impl<M> From<u64> for Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
    {
        fn from(mut value: u64) -> Self {
            let m = M::modulus() as u64;
            if value >= m {
                value %= m;
            }
            Self::new(value as u32)
        }
    }
    impl<M> From<usize> for Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
    {
        fn from(value: usize) -> Self { Self::from(value as u64) }
    }
    impl<M> From<usize> for Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
    {
        fn from(value: usize) -> Self { Self::from(value as u64) }
    }
    use crate::power_monoid_itself::PowMonoid;
    impl<M> Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
        Self: Clone,
    {
        pub fn pow(self, exponent: u64) -> Self { self.pow_monoid(exponent) }
    }
    impl<M> Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
        Self: Clone,
    {
        pub fn pow(self, exponent: u64) -> Self { self.pow_monoid(exponent) }
    }
    use crate::{binary_function::itself::*, group_theory_id::*, ops::MulInv};
    impl<T, M> BinaryOp<Multiplicative> for Modint<T, M>
    where
        M: Arithmetic<T = T>,
        T: Copy,
    {
        fn op(lhs: Self, rhs: Self) -> Self { lhs * rhs }
    }
    impl<M> Identity<Multiplicative> for Modint<u64, M>
    where
        M: Arithmetic<T = u64>,
    {
        fn e() -> Self { 1.into() }
    }
    impl<M> Identity<Multiplicative> for Modint<u32, M>
    where
        M: Arithmetic<T = u32>,
    {
        fn e() -> Self { 1.into() }
    }
    impl<T, M> Associative<Multiplicative> for Modint<T, M> where
        M: Arithmetic<T = T>
    {
    }
    impl<M> MulInv for Modint<u64, M>
    where
        M: Arithmetic<T = u64> + Copy,
    {
        type Output = Self;

        fn mul_inv(self) -> Self::Output { self.inv() }
    }
    impl<M> MulInv for Modint<u32, M>
    where
        M: Arithmetic<T = u32> + Copy,
    {
        type Output = Self;

        fn mul_inv(self) -> Self::Output { self.inv() }
    }
    // TODO:
    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {}
    }
}
