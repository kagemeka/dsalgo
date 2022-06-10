use crate::{
    static_modular_arithmetic_trait::StaticModularArithmeticTrait,
    static_modular_int::StaticModularInt,
};

// TODO: move out From<T> from this file.
// because these are extensions rather than core functionality.
impl<M> From<u64> for StaticModularInt<u64, M>
where
    M: StaticModularArithmeticTrait<T = u64>,
{
    fn from(mut value: u64) -> Self {
        let m = M::modulus();
        if value >= m {
            value %= m;
        }
        Self::new(value)
    }
}

impl<M> From<u64> for StaticModularInt<u32, M>
where
    M: StaticModularArithmeticTrait<T = u32>,
{
    fn from(mut value: u64) -> Self {
        let m = M::modulus() as u64;
        if value >= m {
            value %= m;
        }
        Self::new(value as u32)
    }
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
