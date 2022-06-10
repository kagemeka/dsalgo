use crate::semigroup::Semigroup;

pub fn pow_semigroup_recurse<F, X>(f: &F, x: X, exponent: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exponent > 0);
    if exponent == 1 {
        return x;
    }
    let mut y = pow_semigroup_recurse(f, x.clone(), exponent >> 1);
    y = f(y.clone(), y);
    if exponent & 1 == 1 {
        y = f(y, x);
    }
    y
}

pub fn pow_semigroup<F, X>(f: &F, mut x: X, mut exponent: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exponent > 0);
    let mut y = x.clone();
    exponent -= 1;
    while exponent > 0 {
        if exponent & 1 == 1 {
            y = f(y, x.clone());
        }
        x = f(x.clone(), x);
        exponent >>= 1;
    }
    y
}

pub trait PowerSemigroupSelf<Id>: Semigroup<Id, S = Self>
where
    Self: Clone,
{
    fn pow_seimigroup(self, exponent: u64) -> Self {
        pow_semigroup(&Self::operate, self, exponent)
    }
}
impl<S: Semigroup<Id, S = S> + Clone, Id> PowerSemigroupSelf<Id> for S {}

pub trait StaticPowerSemigroup<Id>: Semigroup<Id>
where
    Self::S: Clone,
{
    fn pow_seimigroup(x: Self::S, exponent: u64) -> Self::S {
        pow_semigroup(&Self::operate, x, exponent)
    }
}
impl<T: Semigroup<Id>, Id> StaticPowerSemigroup<Id> for T where T::S: Clone {}
