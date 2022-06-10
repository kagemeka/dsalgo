use crate::binary_operation_id::BinaryOperationId;

pub trait InverseElement<Id: BinaryOperationId> {
    type X;
    fn invert(element: Self::X) -> Self::X;
}
