pub fn pow_semigroup_recurse<F, X>(f: &F, x: X, exp: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exp > 0);
    if exp == 1 {
        return x;
    }
    let mut y = pow_semigroup_recurse(f, x.clone(), exp >> 1);
    y = f(y.clone(), y);
    if exp & 1 == 1 {
        y = f(y, x);
    }
    y
}

pub fn pow_semigroup<F, X>(f: &F, mut x: X, mut exp: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exp > 0);
    let mut y = x.clone();
    exp -= 1;
    while exp > 0 {
        if exp & 1 == 1 {
            y = f(y, x.clone());
        }
        x = f(x.clone(), x);
        exp >>= 1;
    }
    y
}

pub fn pow_monoid<F, E, X>(f: &F, e: &E, x: X, exp: u64) -> X
where
    F: Fn(X, X) -> X,
    E: Fn() -> X,
    X: Clone,
{
    if exp == 0 { e() } else { pow_semigroup(f, x, exp) }
}

pub fn pow_group<F, E, Inv, X>(f: &F, e: &E, inv: &Inv, x: X, exp: i64) -> X
where
    F: Fn(X, X) -> X,
    E: Fn() -> X,
    Inv: Fn(X) -> X,
    X: Clone,
{
    if exp >= 0 {
        pow_monoid(f, e, x, exp as u64)
    } else {
        pow_semigroup(f, inv(x), -exp as u64)
    }
}

use crate::algebraic_structure::*;
pub trait PowSemigroup: Semigroup
where
    Self::S: Clone,
{
    fn pow_seimigroup(x: Self::S, exp: u64) -> Self::S {
        pow_semigroup(&Self::op, x, exp)
    }
}

impl<T: Semigroup> PowSemigroup for T where T::S: Clone {}

pub trait PowMonoid: Monoid
where
    Self::S: Clone,
{
    fn pow_monoid(x: Self::S, exp: u64) -> Self::S {
        pow_monoid(&Self::op, &Self::e, x, exp)
    }
}
impl<T: Monoid> PowMonoid for T where T::S: Clone {}

pub trait PowGroup: Group
where
    Self::S: Clone,
{
    fn pow_group(x: Self::S, exp: i64) -> Self::S {
        pow_group(
            &Self::op,
            &Self::e,
            &Self::inv,
            x,
            exp,
        )
    }
}
impl<T: Group> PowGroup for T where T::S: Clone {}

pub mod itself {
    use crate::algebraic_structure::itself::*;
    pub trait PowSemigroup<I>: Semigroup<I>
    where
        Self: Clone,
    {
        fn pow_seimigroup(self, exp: u64) -> Self {
            super::pow_semigroup(&Self::op, self, exp)
        }
    }

    impl<S: Semigroup<I> + Clone, I> PowSemigroup<I> for S {}

    pub trait PowMonoid<I>: Monoid<I>
    where
        Self: Clone,
    {
        fn pow_monoid(self, exp: u64) -> Self {
            super::pow_monoid(&Self::op, &Self::e, self, exp)
        }
    }

    impl<S: Monoid<I> + Clone, I> PowMonoid<I> for S {}

    pub trait PowGroup<I>: Group<I>
    where
        Self: Clone,
    {
        fn pow_group(self, exp: i64) -> Self {
            super::pow_group(
                &Self::op,
                &Self::e,
                &Self::inv,
                self,
                exp,
            )
        }
    }

    impl<S: Group<I> + Clone, I> PowGroup<I> for S {}
}

pub mod dynamic {}
