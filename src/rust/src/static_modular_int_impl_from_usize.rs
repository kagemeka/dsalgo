use crate::{
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

impl<M> From<usize> for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
{
    fn from(value: usize) -> Self { Self::from(value as u64) }
}

impl<M> From<usize> for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
{
    fn from(value: usize) -> Self { Self::from(value as u64) }
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
