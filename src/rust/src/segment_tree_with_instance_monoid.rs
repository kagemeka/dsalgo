pub trait Monoid {
    type T;
    fn op(&self, _: Self::T, _: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub struct SegmentTree<G: Monoid> {
    g: G,
    size: usize,
    data: Vec<G::T>,
}
impl<G: Monoid> SegmentTree<G> {
    fn n(&self) -> usize { self.data.len() >> 1 }
}
use std::ops::*;
impl<G: Monoid> Index<usize> for SegmentTree<G> {
    type Output = G::T;

    fn index(&self, i: usize) -> &Self::Output { &self.data[i + self.n()] }
}
impl<G: Monoid> SegmentTree<G>
where
    G::T: Clone,
{
    fn update(&mut self, i: usize) {
        self.data[i] = self
            .g
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    pub fn new(g: G, size: usize) -> Self {
        assert!(size > 0);
        let data = vec![g.e(); size.next_power_of_two() << 1];
        Self { g, size, data }
    }

    pub fn set(&mut self, mut i: usize, x: G::T) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.update(i);
        }
    }

    pub fn get(&self, mut l: usize, mut r: usize) -> G::T {
        assert!(l <= r && r <= self.size);
        let mut vl = self.g.e();
        let mut vr = self.g.e();
        let n = self.n();
        l += n;
        r += n;
        while l < r {
            if l & 1 == 1 {
                vl = self.g.op(vl.clone(), self.data[l].clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.g.op(self.data[r].clone(), vr.clone());
            }
            l >>= 1;
            r >>= 1;
        }
        self.g.op(vl, vr)
    }

    pub fn max_right<F: Fn(&G::T) -> bool>(&self, f: F, l: usize) -> usize {
        assert!(l <= self.size);
        if l == self.size {
            return self.size;
        }
        let mut v = self.g.e();
        let n = self.n();
        let mut i = l + n;
        loop {
            i >>= i.trailing_zeros();
            let nv = self.g.op(v.clone(), self.data[i].clone());
            if !f(&nv) {
                break;
            }
            v = nv;
            i += 1;
            if i.count_ones() == 1 {
                return self.size;
            }
        }
        while i < n {
            i <<= 1;
            let nv = self.g.op(v.clone(), self.data[i].clone());
            if !f(&nv) {
                continue;
            }
            v = nv;
            i += 1;
        }
        i - n
    }

    pub fn min_left<F: Fn(&G::T) -> bool>(&self, f: F, r: usize) -> usize {
        assert!(r <= self.size);
        if r == 0 {
            return 0;
        }
        let mut v = self.g.e();
        let n = self.n();
        let mut i = r + n;
        loop {
            i >>= i.trailing_zeros();
            let nv = self.g.op(self.data[i - 1].clone(), v.clone());
            if !f(&nv) {
                break;
            }
            i -= 1;
            v = nv;
            if i.count_ones() == 1 {
                return self.size;
            }
        }
        while i < n {
            i <<= 1;
            let nv = self.g.op(self.data[i - 1].clone(), v.clone());
            if !f(&nv) {
                continue;
            }
            i -= 1;
            v = nv;
        }
        i - n
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        struct G;
        impl Monoid for G {
            type T = i32;

            fn op(&self, x: i32, y: i32) -> i32 { x + y }

            fn e(&self) -> i32 { 0 }
        }
        let mut seg = SegmentTree::<G>::new(G {}, 5);
        for i in 0..5 {
            seg.set(i, i as i32 + 1);
        }
        assert_eq!(seg[3], 4);
        assert_eq!(seg.get(2, 4), 7);
        assert_eq!(seg.max_right(|&x| x < 5, 1), 2);
        assert_eq!(seg.max_right(|&x| x <= 5, 1), 3);
        assert_eq!(seg.min_left(|&x| x < 7, 4), 3);
        assert_eq!(seg.min_left(|&x| x <= 7, 4), 2);
    }
}
