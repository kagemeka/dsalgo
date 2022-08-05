pub trait Monoid {
    type T;
    fn op(_: Self::T, _: Self::T) -> Self::T;
    fn e() -> Self::T;
}
pub struct Fenwick<M: Monoid>(Vec<M::T>);
impl<M: Monoid> Fenwick<M>
where
    M::T: Clone,
{
    pub fn size(&self) -> usize { self.0.len() - 1 }

    pub fn new(size: usize) -> Self { Self(vec![M::e(); size + 1]) }

    pub fn apply(&mut self, mut i: usize, x: M::T) {
        i += 1;
        while i <= self.size() {
            self.0[i] = M::op(self.0[i].clone(), x.clone());
            i += 1 << i.trailing_zeros();
        }
    }

    pub fn get(&self, mut i: usize) -> M::T {
        let mut v = M::e();
        while i > 0 {
            v = M::op(v.clone(), self.0[i].clone());
            i -= 1 << i.trailing_zeros();
        }
        v
    }

    pub fn max_right<F: Fn(&M::T) -> bool>(&self, f: F) -> usize {
        let n = self.size();
        let mut d = (n + 1).next_power_of_two();
        let mut v = M::e();
        let mut i = 0;
        loop {
            d >>= 1;
            if d == 0 {
                return i;
            }
            if i + d > n {
                continue;
            }
            let nv = M::op(v.clone(), self.0[i + d].clone());
            if f(&nv) {
                v = nv;
                i += d;
            }
        }
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
