pub struct Segtree {
    pub size: usize,
    pub(crate) data: Vec<i64>,
}
impl Segtree {
    fn n(&self) -> usize { self.data.len() >> 1 }

    fn update(&mut self, i: usize) {
        self.data[i] = self.data[i << 1] + self.data[i << 1 | 1];
    }

    pub fn new(size: usize) -> Self {
        assert!(size > 0);
        let data = vec![0; size.next_power_of_two() << 1];
        Self { size, data }
    }

    pub fn set(&mut self, mut i: usize, x: i64) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.update(i);
        }
    }

    pub fn fold(&self, mut l: usize, mut r: usize) -> i64 {
        assert!(l <= r && r <= self.size);
        let mut vl = 0;
        let mut vr = 0;
        let n = self.n();
        l += n;
        r += n;
        while l < r {
            if l & 1 == 1 {
                vl += self.data[l];
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.data[r] + vr;
            }
            l >>= 1;
            r >>= 1;
        }
        vl + vr
    }
}
use std::ops::*;
impl Index<usize> for Segtree {
    type Output = i64;

    fn index(&self, i: usize) -> &Self::Output { &self.data[i + self.n()] }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
