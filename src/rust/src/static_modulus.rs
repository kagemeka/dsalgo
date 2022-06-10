use crate::static_modulus_trait::{StaticModulusGet, StaticModulusSet};

pub trait StaticModId {}

impl<T> StaticModId for T {}

macro_rules! define_static_modulus {
    (
        $name:ident,
        $uint:ty,
        $atomic_uint:ty,
        $atomic_ordering_store:expr,
        $atomic_ordering_load:expr
    ) => {
        #[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub struct $name<Id>(std::marker::PhantomData<Id>);

        impl<Id> $name<Id> {
            fn cell() -> &'static $atomic_uint {
                // VALUE type needs Sync + 'static
                // std::cell types are not Sync
                // std::sync::Mutex is not 'static
                // only atomic types can be.
                // or we can use external crate like `lazy_static`.

                // why not defining as associated const variable?
                // -> const variables are immutabe in any situation.
                static CELL: $atomic_uint = <$atomic_uint>::new(0);
                &CELL
            }
        }

        impl<Id> StaticModulusGet for $name<Id> {
            type T = $uint;

            fn get() -> Self::T { Self::cell().load($atomic_ordering_load) }
        }

        impl<Id> StaticModulusSet for $name<Id> {
            type T = $uint;

            fn set(value: Self::T) {
                Self::cell().store(value, $atomic_ordering_store);
            }
        }
    };

    ($name:ident, $uint:ty, $atomic_uint:ty) => {
        define_static_modulus!(
            $name,
            $uint,
            $atomic_uint,
            std::sync::atomic::Ordering::SeqCst,
            std::sync::atomic::Ordering::SeqCst
        );
    };
}

use std::sync::atomic::{AtomicU32, AtomicU64};
define_static_modulus!(StaticMod32, u32, AtomicU32);
define_static_modulus!(StaticMod64, u64, AtomicU64);

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        struct Foo;
        type Mod = StaticMod32<Foo>;
        Mod::set(1_000_000_007);
        assert_eq!(Mod::get(), 1_000_000_007);
        Mod::set(998_244_353);
        assert_eq!(Mod::get(), 998_244_353);
    }
}
