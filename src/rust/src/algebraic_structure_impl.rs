use crate::{binary_function::*, grouop_theory_id::*};

/// ((usize, usize), min)
pub struct GroupApprox<S, I>(std::marker::PhantomData<(S, I)>);

impl BinaryOp for GroupApprox<(usize, usize), Min> {
    type S = (usize, usize);

    fn op(lhs: Self::S, rhs: Self::S) -> Self::S { lhs.min(rhs) }
}

impl Idempotence for GroupApprox<(usize, usize), Min> {}

impl Commutative for GroupApprox<(usize, usize), Min> {}

impl Associative for GroupApprox<(usize, usize), Min> {}

impl Identity for GroupApprox<(usize, usize), Min> {
    fn e() -> Self::S {
        (
            std::usize::MAX,
            std::usize::MAX,
        )
    }
}

/// (usize, min)
impl BinaryOp for GroupApprox<usize, Min> {
    type S = usize;

    fn op(lhs: usize, rhs: usize) -> usize { lhs.min(rhs) }
}

impl Idempotence for GroupApprox<usize, Min> {}

impl Commutative for GroupApprox<usize, Min> {}

impl Associative for GroupApprox<usize, Min> {}

impl Identity for GroupApprox<usize, Min> {
    fn e() -> Self::S { std::usize::MAX }
}

/// (usize, +)
impl BinaryOp for GroupApprox<usize, Additive> {
    type S = usize;

    fn op(lhs: usize, rhs: usize) -> usize { lhs + rhs }
}

impl Associative for GroupApprox<usize, Additive> {}

impl Commutative for GroupApprox<usize, Additive> {}

impl Identity for GroupApprox<usize, Additive> {
    fn e() -> Self::S { 0 }
}

/// (i32, +)
impl BinaryOp for GroupApprox<i32, Additive> {
    type S = i32;

    fn op(lhs: i32, rhs: i32) -> i32 { lhs + rhs }
}

impl Associative for GroupApprox<i32, Additive> {}

impl Commutative for GroupApprox<i32, Additive> {}

impl Identity for GroupApprox<i32, Additive> {
    fn e() -> Self::S { 0 }
}

impl Inverse for GroupApprox<i32, Additive> {
    fn inv(x: i32) -> i32 { -x }
}
