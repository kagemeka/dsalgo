use crate::binary_operation_id::BinaryOperationId;

pub trait BinaryFunction<Id: BinaryOperationId> {
    type Lhs;
    type Rhs;
    type Codomain;
    fn map(_: Self::Lhs, _: Self::Rhs) -> Self::Codomain;
}
