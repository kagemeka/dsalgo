use crate::{
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

impl<M> From<i32> for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
{
    fn from(value: i32) -> Self { Self::from(value as i64) }
}

impl<M> From<i32> for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
{
    fn from(value: i32) -> Self { Self::from(value as i64) }
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
