fn main() {}

pub mod algebraic_structure {
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

        fn add(l: Self::S, r: Self::S) -> Self::S {
            <T as BinaryOp<A>>::op(l, r)
        }

        fn mul(l: Self::S, r: Self::S) -> Self::S {
            <T as BinaryOp<M>>::op(l, r)
        }

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
        fn add_inv(element: Self::S) -> Self::S {
            <T as Inverse<A>>::inv(element)
        }
    }
}

pub mod binary_function {
    pub trait Id {}
    impl<T> Id for T {}

    /// binary function
    pub trait BinaryFunc<I: Id> {
        type L;
        type R;
        type Cod;
        fn f(_: Self::L, _: Self::R) -> Self::Cod;
    }

    /// external binary operation
    pub trait ExtBinaryOp<I: Id>: BinaryFunc<I> {}
    impl<I: Id, T: BinaryFunc<I>> ExtBinaryOp<I> for T {}

    /// binary operation on a set.
    pub trait BinaryOp<I: Id> {
        type S;
        fn op(_: Self::S, _: Self::S) -> Self::S;
    }

    fn is_left_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        f(e, x.clone()) == x
    }

    fn is_right_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        f(x.clone(), e) == x
    }

    fn is_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        is_left_identity(f, e.clone(), x.clone()) && is_right_identity(f, e, x)
    }

    /// identity element
    pub trait Identity<I: Id>: BinaryOp<I> {
        fn e() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_identity(
                &Self::op,
                Self::e(),
                x
            ));
        }
    }

    pub fn is_invertible<F, G, X>(op: &F, inv: &G, e: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        G: Fn(X) -> X,
        X: Clone + PartialEq,
    {
        op(x.clone(), inv(x.clone())) == e.clone()
            && op(inv(x.clone()), x.clone()) == e
    }

    /// inverse element
    pub trait Inverse<I: Id>: Identity<I> {
        fn inv(_: Self::S) -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_invertible(
                &Self::op,
                &Self::inv,
                Self::e(),
                x
            ));
        }
    }

    pub fn is_commutative<F, X, Y>(f: &F, a: X, b: X) -> bool
    where
        F: Fn(X, X) -> Y,
        X: Clone,
        Y: PartialEq,
    {
        f(a.clone(), b.clone()) == f(b, a)
    }

    /// commutative property
    pub trait Commutative<I: Id>: BinaryOp<I> {
        fn assert(x: Self::S, y: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_commutative(&Self::op, x, y));
        }
    }

    pub fn is_associative<F, X>(f: &F, a: X, b: X, c: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(
            f(a.clone(), b.clone()),
            c.clone(),
        ) == f(a, f(b, c))
    }
    /// associative property
    pub trait Associative<I: Id>: BinaryOp<I> {
        fn assert(x: Self::S, y: Self::S, z: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_associative(
                &Self::op,
                x,
                y,
                z
            ));
        }
    }

    pub fn is_idempotent<F, X>(f: &F, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x.clone(), x.clone()) == x
    }

    pub trait Idempotence<I: Id>: BinaryOp<I> {
        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_idempotent(&Self::op, x));
        }
    }

    pub fn is_left_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(z.clone(), x) == z
    }

    pub fn is_right_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x, z.clone()) == z
    }

    pub fn is_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_left_absorbing(f, z.clone(), x.clone())
            && is_right_absorbing(f, z, x)
    }

    /// absorbing element
    pub trait Absorbing<I: Id>: BinaryOp<I> {
        type X;
        fn z() -> Self::X;
    }

    pub fn is_left_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        x: X,
        y: X,
        z: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        mul(
            x.clone(),
            add(y.clone(), z.clone()),
        ) == add(mul(x.clone(), y), mul(x, z))
    }

    pub fn is_right_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        y: X,
        z: X,
        x: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        mul(
            add(y.clone(), z.clone()),
            x.clone(),
        ) == add(mul(y, x.clone()), mul(z, x))
    }

    pub fn is_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        x: X,
        y: X,
        z: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_left_distributive(
            add,
            mul,
            x.clone(),
            y.clone(),
            z.clone(),
        ) && is_right_distributive(add, mul, y, z, x)
    }

    // TODO:
    /// distributive property
    pub trait Distributive<A, M>
    where
        A: Id,
        M: Id,
    {
    }

    pub fn iz_zero<F, X>(mul: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_absorbing(mul, z, x)
    }

    // TODO:
    /// zero element
    /// additive identity and multiplicative absorbing.
    pub trait Zero<A, M>
    where
        A: Id,
        M: Id,
    {
    }
}
