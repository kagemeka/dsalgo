use crate::{
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

impl<M> From<i64> for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
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

impl<M> From<i64> for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
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

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
