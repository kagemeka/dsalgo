// TODO:
pub struct Modint<const MOD: i64>(pub i64);
impl<const MOD: i64> Modint<MOD> {
    pub const fn modulus() -> i64 { MOD }

    pub fn normalize(mut v: i64) -> i64 {
        if v < -MOD || v >= MOD {
            v %= MOD;
        }
        if v < 0 {
            v += MOD;
        }
        v
    }

    pub fn new(v: i64) -> Self { Self(Self::normalize(v)) }
}
use std::ops::*;
impl<const MOD: i64> Add for Modint<MOD> {
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self.0 += rhs.0;
        if self.0 >= MOD {
            self.0 -= MOD;
        }
        self
    }
}
impl<const MOD: i64> Neg for Modint<MOD> {
    type Output = Self;

    fn neg(self) -> Self::Output {
        if self.0 == 0 { self } else { Self(MOD - self.0) }
    }
}
impl<const MOD: i64> Mul for Modint<MOD> {
    type Output = Self;

    fn mul(mut self, rhs: Self) -> Self::Output {
        self.0 *= rhs.0;
        if self.0 >= MOD {
            self.0 %= MOD;
        }
        self
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
