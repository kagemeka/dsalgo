fn main() {}

pub mod algebraic_structure {
    use crate::binary_function::*;

    pub trait Magma: BinaryOp {}

    impl<T: BinaryOp> Magma for T {}

    pub trait Semigroup: Magma + Associative {}

    impl<T: Magma + Associative> Semigroup for T {}

    pub trait Monoid: Semigroup + Identity {}

    impl<T> Monoid for T where T: Semigroup + Identity {}

    pub trait UnitalMagma: Magma + Identity {}

    impl<T: Magma + Identity> UnitalMagma for T {}

    pub trait Quasigroup: Magma + LatinSquare {}

    impl<T: Magma + LatinSquare> Quasigroup for T {}

    pub trait Loop: Quasigroup + Identity {}

    impl<T: Quasigroup + Identity> Loop for T {}

    pub trait Group: Monoid + Inverse {}

    impl<T: Monoid + Inverse> Group for T {}

    pub trait AbelianGroup: Group + Commutative {}

    impl<T: Group + Commutative> AbelianGroup for T {}

    pub trait Semiring: Zero + One + Distributive {}

    impl<T: Zero + One + Distributive> Semiring for T {}

    pub trait Ring: Semiring + AddInv {}

    impl<T: Semiring + AddInv> Ring for T {}

    pub mod dynamic {
        use crate::binary_function::dynamic::*;
        pub trait Magma: BinaryOp {}

        impl<T: BinaryOp> Magma for T {}
    }

    pub mod itself {
        use crate::binary_function::itself::*;

        pub trait Magma<I: Id>: BinaryOp<I> {}

        impl<I, T> Magma<I> for T
        where
            T: BinaryOp<I>,
            I: Id,
        {
        }
    }
}

pub mod binary_function {
    /// binary function
    pub trait BinaryFunc {
        type L;
        type R;
        type Cod;
        fn f(_: Self::L, _: Self::R) -> Self::Cod;
    }

    /// external binary operation
    pub trait ExtBinaryOp: BinaryFunc {}
    impl<T: BinaryFunc> ExtBinaryOp for T {}

    /// binary operation on a set.
    pub trait BinaryOp {
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
    pub trait Identity: BinaryOp {
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

    fn is_invertible<F, G, X>(op: &F, inv: &G, e: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        G: Fn(X) -> X,
        X: Clone + PartialEq,
    {
        op(x.clone(), inv(x.clone())) == e.clone()
            && op(inv(x.clone()), x.clone()) == e
    }

    /// inverse element
    pub trait Inverse: Identity {
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

    fn is_commutative<F, X, Y>(f: &F, a: X, b: X) -> bool
    where
        F: Fn(X, X) -> Y,
        X: Clone,
        Y: PartialEq,
    {
        f(a.clone(), b.clone()) == f(b, a)
    }

    /// commutative property
    pub trait Commutative: BinaryOp {
        fn assert(a: Self::S, b: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_commutative(&Self::op, a, b));
        }
    }

    fn is_associative<F, X>(f: &F, a: X, b: X, c: X) -> bool
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
    pub trait Associative: BinaryOp {
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

    fn is_idempotent<F, X>(f: &F, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x.clone(), x.clone()) == x
    }

    pub trait Idempotence: BinaryOp {
        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_idempotent(&Self::op, x));
        }
    }

    /// latain square property
    pub trait LatinSquare: BinaryOp {}

    impl<T: Inverse> LatinSquare for T {}

    // TODO: assertion latin square

    fn is_left_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(z.clone(), x) == z
    }

    fn is_right_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x, z.clone()) == z
    }

    fn is_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_left_absorbing(f, z.clone(), x.clone())
            && is_right_absorbing(f, z, x)
    }

    /// absorbing element
    pub trait Absorbing: BinaryOp {
        fn z() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_absorbing(
                &Self::op,
                Self::z(),
                x
            ));
        }
    }

    pub trait Add {
        type S;
        fn add(_: Self::S, _: Self::S) -> Self::S;
    }

    pub trait Mul: Add {
        fn mul(_: Self::S, _: Self::S) -> Self::S;
    }

    fn iz_zero<F, X>(mul: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_absorbing(mul, z, x)
    }

    pub trait Zero: Mul {
        fn zero() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(iz_zero(
                &Self::mul,
                Self::zero(),
                x
            ));
        }
    }

    pub trait One: Mul {
        fn one() -> Self::S;
    }

    pub trait AddInv: Add {
        fn add_inv(_: Self::S) -> Self::S;
    }

    pub trait MulInv: Mul {
        fn mul_inv(_: Self::S) -> Self::S;
    }

    fn is_left_distributive<Add, Mul, X>(
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

    fn is_right_distributive<Add, Mul, X>(
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

    fn is_distributive<Add, Mul, X>(
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

    pub trait Distributive: Mul {
        fn assert(x: Self::S, y: Self::S, z: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_distributive(
                &Self::mul,
                &Self::add,
                x,
                y,
                z
            ));
        }
    }

    pub mod dynamic {
        pub trait BinaryOp {
            type S;
            fn op(&self, _: Self::S, _: Self::S) -> Self::S;
        }
    }

    pub mod itself {
        pub trait Id {}
        impl<T> Id for T {}

        pub trait BinaryOp<I: Id> {
            fn op(_: Self, _: Self) -> Self;
        }
    }
}
