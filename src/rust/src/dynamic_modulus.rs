// use crate::modulus::Modulus;

use crate::dynamic_modulus_trait::{DynamicModulusGet, DynamicModulusSet};

/// T is gonna be u64 or u32
#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct DynamicMod<T>(T);

impl<T> DynamicMod<T> {
    pub fn new(value: T) -> Self { Self(value) }
}

impl<T: Copy> DynamicModulusGet for DynamicMod<T> {
    type T = T;

    fn get(&self) -> Self::T { self.0 }
}

impl<T> DynamicModulusSet for DynamicMod<T> {
    type T = T;

    fn set(&mut self, value: Self::T) { self.0 = value }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        type Mod = DynamicMod<u32>;

        let mut x = Mod::new(998_244_353);
        assert_eq!(x.get(), 998_244_353);
        x.set(1_000_000_007);
        assert_eq!(x.get(), 1_000_000_007);
    }
}
