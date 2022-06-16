use crate::{algebraic_structure::*, binary_function::*, group_theory_id::*};

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

impl BinaryOp for GroupApprox<usize, Additive> {
    type S = usize;

    fn op(lhs: usize, rhs: usize) -> usize { lhs + rhs }
}

impl Associative for GroupApprox<usize, Additive> {}

impl Commutative for GroupApprox<usize, Additive> {}

impl Identity for GroupApprox<usize, Additive> {
    fn e() -> Self::S { 0 }
}
