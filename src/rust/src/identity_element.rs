use crate::binary_operation_id::BinaryOperationId;
pub trait IdentityElement<Id: BinaryOperationId> {
    type X;
    fn identity() -> Self::X;
}
