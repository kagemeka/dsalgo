use crate::binary_operation_id::BinaryOperationId;

pub trait DistributiveProperty<Add, Mul>
where
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}
