use crate::{
    power_monoid::PowerMonoidSelf,
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

impl<M> StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
    Self: Clone,
{
    pub fn pow(self, exponent: u64) -> Self { self.pow_monoid(exponent) }
}

impl<M> StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
    Self: Clone,
{
    pub fn pow(self, exponent: u64) -> Self { self.pow_monoid(exponent) }
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
