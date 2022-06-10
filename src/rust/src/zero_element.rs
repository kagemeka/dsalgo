use crate::binary_operation_id::BinaryOperationId;

pub trait ZeroElement<Add, Mul>
where
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}
