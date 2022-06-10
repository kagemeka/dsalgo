use crate::static_modular_arithmetic_trait::StaticModularArithmeticTrait;

/// T should be u32 or u64.
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default)]
pub struct StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
{
    value: M::T,
}

impl<T, M> std::fmt::Display for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    M::T: std::fmt::Display,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

impl<T, M> StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    M::T: Copy,
{
    pub const fn value(&self) -> M::T { self.value }

    pub const fn new(value: M::T) -> Self { Self { value } }

    pub fn modulus() -> M::T { M::modulus() }
}

impl<T, M> std::ops::Add for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self.value = M::add(self.value, rhs.value);
        self
    }
}

impl<T, M> std::ops::AddAssign for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T> + Copy,
    T: Copy,
{
    fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
}

impl<T, M> std::ops::Sub for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Output = Self;

    fn sub(mut self, rhs: Self) -> Self::Output {
        self.value = M::sub(self.value, rhs.value);
        self
    }
}

impl<T, M> std::ops::SubAssign for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T> + Copy,
    T: Copy,
{
    fn sub_assign(&mut self, rhs: Self) { *self = *self - rhs; }
}

impl<T, M> std::ops::Neg for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Output = Self;

    fn neg(mut self) -> Self::Output {
        self.value = M::neg(self.value);
        self
    }
}

impl<T, M> std::ops::Mul for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Output = Self;

    fn mul(mut self, rhs: Self) -> Self::Output {
        self.value = M::mul(self.value, rhs.value);
        self
    }
}

impl<T, M> std::ops::MulAssign for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T> + Copy,
    T: Copy,
{
    fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
}

impl<T, M> std::ops::Div for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T>,
    T: Copy,
{
    type Output = Self;

    fn div(mut self, rhs: Self) -> Self::Output {
        self.value = M::div(self.value, rhs.value);
        self
    }
}

impl<T, M> std::ops::DivAssign for StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T> + Copy,
    T: Copy,
{
    fn div_assign(&mut self, rhs: Self) { *self = *self / rhs; }
}

impl<T, M> StaticModularInt<T, M>
where
    M: StaticModularArithmeticTrait<T = T> + Copy,
    T: Copy,
{
    pub fn invert(mut self) -> Self {
        self.value = M::invert(self.value);
        self
    }
}

// use crate::{modular_arithmetic::ModularArithemetic, modulus::Modulus};
// use crate::static_modulus_trait::{StaticModulusGet};

// // TODO: make M as ModularArithemetic (not Modulus)
// #[derive(Debug, Clone, Copy, PartialEq, Eq)]
// pub struct StaticModularInt<M> {
//     phantom: std::marker::PhantomData<M>,
//     value: u32,
// }

// impl<M> std::fmt::Display for StaticModularInt<M> {
//     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
//         write!(f, "{}", self.value)
//     }
// }

// impl<M> ModularInt<M> {
//     // TODO: make const
//     pub fn value(&self) -> u32 { self.value }
// }

// impl<M: Modulus> ModularInt<M> {
//     pub fn new(mut value: u32) -> Self {
//         if value >= M::modulus() {
//             value %= M::modulus();
//         }
//         Self {
//             phantom: std::marker::PhantomData,
//             value,
//         }
//     }

//     pub fn modulus() -> u32 { M::modulus() }
// }

// impl<M: Modulus> From<u64> for ModularInt<M> {
//     fn from(mut value: u64) -> Self {
//         let m = M::modulus() as u64;
//         if value >= m {
//             value %= m;
//         }
//         Self::new(value as u32)
//     }
// }
// impl<M: Modulus> From<i64> for ModularInt<M> {
//     fn from(mut value: i64) -> Self {
//         let m = M::modulus() as i64;
//         if value < -m || value >= m {
//             value %= m;
//         }
//         if value < 0 {
//             value += m;
//         }
//         Self::new(value as u32)
//     }
// }

// impl<M: Modulus> std::ops::AddAssign<Self> for ModularInt<M> {
//     fn add_assign(&mut self, rhs: Self) {
//         self.value = ModularArithemetic::<M>::add(self.value, rhs.value);
//     }
// }

// impl<M: Modulus> std::ops::Add<Self> for ModularInt<M> {
//     type Output = Self;

//     fn add(mut self, rhs: Self) -> Self::Output {
//         self += rhs;
//         self
//     }
// }

// impl<M: Modulus> std::ops::Neg for ModularInt<M> {
//     type Output = Self;

//     fn neg(mut self) -> Self::Output {
//         self.value = ModularArithemetic::<M>::neg(self.value);
//         self
//     }
// }

// impl<M: Modulus> std::ops::SubAssign<Self> for ModularInt<M> {
//     fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
// }

// impl<M: Modulus> std::ops::Sub<Self> for ModularInt<M> {
//     type Output = Self;

//     fn sub(mut self, rhs: Self) -> Self {
//         self -= rhs;
//         self
//     }
// }

// impl<M: Modulus> std::ops::MulAssign<Self> for ModularInt<M> {
//     fn mul_assign(&mut self, rhs: Self) {
//         self.value = ModularArithemetic::<M>::mul(self.value, rhs.value);
//     }
// }

// impl<M: Modulus> std::ops::Mul<Self> for ModularInt<M> {
//     type Output = Self;

//     fn mul(mut self, rhs: Self) -> Self {
//         self *= rhs;
//         self
//     }
// }

// impl<M: Modulus> std::ops::DivAssign<Self> for ModularInt<M> {
//     fn div_assign(&mut self, rhs: Self) { *self *= rhs.invert().unwrap(); }
// }
// impl<M: Modulus> std::ops::Div<Self> for ModularInt<M> {
//     type Output = Self;

//     fn div(mut self, rhs: Self) -> Self::Output {
//         self /= rhs;
//         self
//     }
// }

// impl<M: Modulus> ModularInt<M> {
//     pub fn invert(self) -> Result<Self, &'static str> {
//         if self.value() == 0 {
//             // user does not call extgcd directly,
//             // so return err instead of panic.
//             return Err("0 is not invertible");
//         }
//         Ok(Self::new(
//             ModularArithemetic::<M>::invert(self.value())?,
//         ))
//     }
// }

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
