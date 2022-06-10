//! new version, cannot compile on Some Online Judges yet.

use crate::static_modulus_trait::StaticModulusGet;

macro_rules! define_const_modulus {
    ($name:ident, $uint:ty) => {
        #[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub struct $name<const MOD: $uint>;

        impl<const MOD: $uint> StaticModulusGet for $name<MOD> {
            type T = $uint;

            fn get() -> Self::T { MOD }
        }
    };
}

define_const_modulus!(ConstMod64, u64);
define_const_modulus!(ConstMod32, u32);

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::ConstMod32;
        use crate::static_modulus_trait::StaticModulusGet;

        type Mod = ConstMod32<1_000_000_007>;
        assert_eq!(Mod::get(), 1_000_000_007);
    }
}
