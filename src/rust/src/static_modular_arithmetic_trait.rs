pub trait StaticModularArithmeticTrait {
    type T;

    fn modulus() -> Self::T;

    fn add(lhs: Self::T, rhs: Self::T) -> Self::T;
    fn neg(x: Self::T) -> Self::T;
    fn sub(lhs: Self::T, rhs: Self::T) -> Self::T {
        // default implementation.
        // it's might be different in each struct.
        Self::add(lhs, Self::neg(rhs))
    }
    fn mul(lhs: Self::T, rhs: Self::T) -> Self::T;
    fn invert(x: Self::T) -> Self::T;
    fn div(lhs: Self::T, rhs: Self::T) -> Self::T {
        Self::mul(lhs, Self::invert(rhs))
    }
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
