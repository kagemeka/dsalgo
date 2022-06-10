//! old version for Online Judges.
//! see also const_modulus.rs

use crate::static_modulus_trait::StaticModulusGet;

macro_rules! define_const_modulus_old {
    ($name:ident, $uint:ty, $value:expr) => {
        #[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub struct $name;

        impl StaticModulusGet for $name {
            type T = $uint;

            fn get() -> Self::T { $value }
        }
    };
}

define_const_modulus_old!(
    Mod998_244_353,
    u32,
    998_244_353
);
define_const_modulus_old!(
    Mod1_000_000_007,
    u32,
    1_000_000_007
);

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::Mod1_000_000_007 as Mod;
        use crate::static_modulus_trait::StaticModulusGet;

        assert_eq!(Mod::get(), 1_000_000_007);
    }
}
