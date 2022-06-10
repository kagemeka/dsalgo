use crate::{
    binary_function::BinaryFunction,
    binary_operation_id::BinaryOperationId,
};

pub trait ExternalBinaryOperation<Id>: BinaryFunction<Id>
where
    Id: BinaryOperationId,
{
}
impl<T: BinaryFunction<Id>, Id> ExternalBinaryOperation<Id> for T {}
