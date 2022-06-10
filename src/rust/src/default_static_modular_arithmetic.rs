use crate::{
    modular_inverse_extgcd::modular_inverse_extgcd,
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modulus_trait::StaticModulusGet,
};

/// why `default`?
/// because there are other modular arithmetic implementations.
/// e.g. Montgomery Multiplication, or Burrett Reduction.
/// this is equivalent to defining belows.
/// - DefaultStaticModularArithmetic64<M: StaticModulusGet<T=u64>>
/// - DefaultStaticModularArithmetic32<M: StaticModulusGet<T=u32>>
/// - ...
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord)]
pub struct DefaultStaticModularArithmetic<T, M: StaticModulusGet<T = T>>(
    std::marker::PhantomData<(T, M)>,
);

macro_rules! impl_default_static_modular_arithmetic {
    ($uint:ty, $mul_cast_uint:ty) => {
        impl<M: StaticModulusGet<T = $uint>> StaticModularArithmeticTrait
            for DefaultStaticModularArithmetic<$uint, M>
        {
            type T = $uint;

            fn modulus() -> Self::T { M::get() }

            fn add(lhs: Self::T, rhs: Self::T) -> Self::T {
                let mut x = lhs;
                x += rhs;
                if x >= M::get() {
                    x -= M::get();
                }
                x
            }

            fn neg(x: Self::T) -> Self::T {
                if x == 0 { 0 } else { M::get() - x }
            }

            fn mul(lhs: Self::T, rhs: Self::T) -> Self::T {
                let mut x = lhs as $mul_cast_uint;
                x *= rhs as $mul_cast_uint;
                x %= M::get() as $mul_cast_uint;
                x as Self::T
            }

            fn invert(x: $uint) -> Self::T {
                assert!(x > 0);
                modular_inverse_extgcd(M::get() as u64, x as u64).unwrap()
                    as Self::T
            }
        }
    };
}

impl_default_static_modular_arithmetic!(u32, u64);
impl_default_static_modular_arithmetic!(u64, u128);

use crate::const_modulus::ConstMod32;

#[allow(dead_code)]
pub type Modular1_000_000_007 =
    DefaultStaticModularArithmetic<u32, ConstMod32<1_000_000_007>>;

#[allow(dead_code)]
pub type Modular998_244_353 =
    DefaultStaticModularArithmetic<u32, ConstMod32<998_244_353>>;

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::Modular1_000_000_007;
        use crate::static_modular_int::StaticModularInt;

        type Mint = StaticModularInt<u32, Modular1_000_000_007>;
        let a = Mint::from(1_000_000_008);
        assert_eq!(a.value(), 1);
    }
}
