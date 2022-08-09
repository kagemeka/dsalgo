use std::ops::*;
pub struct Segtree<T> {
    pub size: usize,
    zero: T,
    pub(crate) data: Vec<T>,
}
impl<T> Segtree<T> {
    fn n(&self) -> usize { self.data.len() >> 1 }
}
impl<T: Add<Output = T> + Clone> Segtree<T> {
    fn update(&mut self, i: usize) {
        self.data[i] =
            self.data[i << 1].clone() + self.data[i << 1 | 1].clone();
    }

    pub fn new(zero: T, size: usize) -> Self {
        assert!(size > 0);
        let data = vec![zero.clone(); size.next_power_of_two() << 1];
        Self { zero, size, data }
    }

    pub fn set(&mut self, mut i: usize, x: T) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.update(i);
        }
    }

    pub fn fold(&self, mut l: usize, mut r: usize) -> T {
        assert!(l <= r && r <= self.size);
        let mut vl = self.zero.clone();
        let mut vr = self.zero.clone();
        let n = self.n();
        l += n;
        r += n;
        while l < r {
            if l & 1 == 1 {
                vl = vl + self.data[l].clone();
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.data[r].clone() + vr;
            }
            l >>= 1;
            r >>= 1;
        }
        vl + vr
    }
}
impl<T> Index<usize> for Segtree<T> {
    type Output = T;

    fn index(&self, i: usize) -> &Self::Output { &self.data[i + self.n()] }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
