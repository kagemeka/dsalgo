use crate::multiplicative_inverse::MulInv;

/// unlike DynamicModularArithmetic,
/// DynamicModularInt does not exist.
/// because modular arithmetic for ModularInt is gonna be commonly defined
/// at entire struct level rather than each instance level.
pub trait StaticModularIntTrait:
    Sized
    + std::ops::Add<Self, Output = Self>
    + std::ops::Neg<Output = Self>
    + std::ops::Sub<Self, Output = Self>
    + std::ops::Mul<Self, Output = Self>
    + MulInv<Output = Self>
    + std::ops::Div<Self, Output = Self>
    + std::fmt::Display
    + std::fmt::Debug
{
}
