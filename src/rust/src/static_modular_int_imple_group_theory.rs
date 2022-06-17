use crate::{
    associative_property::AssociativeProperty,
    binary_operation::BinaryOperation,
    group_theory_id::Multiplicative,
    identity_element::IdentityElement,
    multiplicative_inverse::MulInv,
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

impl<T, M> BinaryOperation<Multiplicative> for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Codomain = Self;
    type Lhs = Self;
    type Rhs = Self;

    fn map(lhs: Self, rhs: Self) -> Self { lhs * rhs }
}

impl<M> IdentityElement<Multiplicative> for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
{
    type X = Self;

    fn identity() -> Self { 1.into() }
}

impl<M> IdentityElement<Multiplicative> for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
{
    type X = Self;

    fn identity() -> Self { 1.into() }
}

impl<T, M> AssociativeProperty<Multiplicative> for StaticModularInt<T, M> where
    M: StaticModularArithmeticTrait<T = T>
{
}

impl<M> MulInv for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64> + Copy,
{
    type Output = Self;

    fn mul_inv(self) -> Self::Output { self.invert() }
}

impl<M> MulInv for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32> + Copy,
{
    type Output = Self;

    fn mul_inv(self) -> Self::Output { self.invert() }
}
