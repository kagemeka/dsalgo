pub trait DynamicModularArithmeticTrait {
    type T;
    fn modulus(&self) -> Self::T;

    fn add(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
    fn neg(&self, x: Self::T) -> Self::T;
    fn sub(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
        self.add(lhs, self.neg(rhs))
    }
    fn mul(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
    fn invert(&self, x: Self::T) -> Self::T;
    fn div(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
        self.mul(lhs, self.invert(rhs))
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
