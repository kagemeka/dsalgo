use crate::binary_operation_id::BinaryOperationId;

pub trait AbsorbingElement<Id: BinaryOperationId> {
    type X;
    fn absorbing_element() -> Self::X;
}
