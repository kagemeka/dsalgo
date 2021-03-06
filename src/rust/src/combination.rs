use crate::{
    factorial_table::factorial_table,
    inverse_factorial_table::inverse_factorial_table,
    ops::MulInv,
};

pub struct Combination<T> {
    fact: Vec<T>,
    inv_fact: Vec<T>,
}

impl<T> Combination<T>
where
    T: std::ops::Mul<Output = T> + From<u64> + Clone,
{
    pub fn new(size: usize) -> Self
    where
        T: MulInv<Output = T>,
    {
        Self {
            fact: factorial_table::<T>(size),
            inv_fact: inverse_factorial_table::<T>(size),
        }
    }

    pub fn calc(&self, n: usize, k: usize) -> T {
        if k > n {
            return 0.into();
        }
        self.fact[n].clone()
            * self.inv_fact[n - k].clone()
            * self.inv_fact[k].clone()
    }

    pub fn inv(&self, n: usize, k: usize) -> T {
        assert!(k <= n); // (n, k) := 0 if k > n, so the inverse is undefined.
        self.inv_fact[n].clone()
            * self.fact[k].clone()
            * self.fact[n - k].clone()
    }
}

// #[cfg(test)]
mod tests {

    #[test]
    fn test() {
        use super::*;
        use crate::modular::{
            arithmetic::Modular1_000_000_007,
            int::Modint as StaticModularInt,
        };
        type Mint = StaticModularInt<u32, Modular1_000_000_007>;
        let choose = Combination::<Mint>::new(100);
        assert_eq!(choose.calc(5, 2), 10.into());
    }
}
