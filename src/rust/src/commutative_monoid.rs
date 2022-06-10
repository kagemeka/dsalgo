use crate::{
    binary_operation_id::BinaryOperationId,
    commutative_property::CommutativeProperty,
    monoid::Monoid,
};

pub trait CommutativeMonoid<Id: BinaryOperationId>: Monoid<Id> {}

impl<Id, T> CommutativeMonoid<Id> for T
where
    T: Monoid<Id> + CommutativeProperty<Id>,
    Id: BinaryOperationId,
{
}
