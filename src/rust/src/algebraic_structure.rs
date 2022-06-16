use crate::binary_function::*;

pub trait Magma<I: Id>: BinaryOp<I> {}

impl<I, T> Magma<I> for T
where
    T: BinaryOp<I>,
    I: Id,
{
}

pub trait Semigroup<I: Id>: Magma<I> + Associative<I> {}

impl<I, T> Semigroup<I> for T
where
    T: Magma<I> + Associative<I>,
    I: Id,
{
}

pub trait Monoid<I: Id>: Semigroup<I> + Identity<I> {}

impl<I, T> Monoid<I> for T
where
    T: Semigroup<I> + Identity<I>,
    I: Id,
{
}

// TODO:
pub trait Quasigroup<I: Id>: Magma<I> {}
// TODO:
pub trait Loop<I: Id>: Quasigroup<I> + Identity<I> {}

pub trait Group<I: Id>: Monoid<I> + Inverse<I> {}

impl<I, T> Group<I> for T
where
    T: Monoid<I> + Inverse<I>,
    I: Id,
{
}

pub trait AbelianGroup<I: Id>: Group<I> + Commutative<I> {}

impl<I, T> AbelianGroup<I> for T
where
    T: Group<I> + Commutative<I>,
    I: Id,
{
}

pub trait Semiring<A, M>
where
    A: Id,
    M: Id,
{
    type S;
    fn add(l: Self::S, r: Self::S) -> Self::S;
    fn mul(l: Self::S, r: Self::S) -> Self::S;
    fn zero() -> Self::S;
    fn one() -> Self::S;
}

impl<S, A, M, T> Semiring<A, M> for T
where
    T: Monoid<A, S = S>
        + Commutative<A>
        + Monoid<M, S = S>
        + Distributive<A, M>
        + Zero<A, M>,
    A: Id,
    M: Id,
{
    type S = S;

    fn add(l: Self::S, r: Self::S) -> Self::S { <T as BinaryOp<A>>::op(l, r) }

    fn mul(l: Self::S, r: Self::S) -> Self::S { <T as BinaryOp<M>>::op(l, r) }

    fn zero() -> Self::S { <T as Identity<A>>::e() }

    fn one() -> Self::S { <T as Identity<M>>::e() }
}

pub trait Ring<A, M>: Semiring<A, M>
where
    A: Id,
    M: Id,
{
    fn add_inv(element: Self::S) -> Self::S;
}

impl<S, A, M, T> Ring<A, M> for T
where
    T: Semiring<A, M, S = S> + Inverse<A, S = S>,
    A: Id,
    M: Id,
{
    fn add_inv(element: Self::S) -> Self::S { <T as Inverse<A>>::inv(element) }
}
