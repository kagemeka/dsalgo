use std::ops::*;

use crate::bit_length_with_count_leading_zeros_usize::bit_length;
pub trait Identity {
    fn e() -> Self;
}
#[derive(Debug)]
pub struct LazySegtree<S, F> {
    data: Vec<S>,
    lazy: Vec<F>,
    size: usize,
}
// be careful of composition order
impl<S, F> LazySegtree<S, F>
where
    S: Clone + Add<Output = S> + Add<F, Output = S> + Identity,
    F: Clone + Add<Output = F> + Identity,
{
    pub fn new(size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![S::e(); n << 1];
        let lazy = vec![F::e(); n];
        Self { data, lazy, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.lazy.len() }

    fn height(&self) -> usize { bit_length(self.n()) }

    fn merge(&mut self, i: usize) {
        self.data[i] =
            self.data[i << 1].clone() + self.data[i << 1 | 1].clone();
    }

    fn apply_node(&mut self, i: usize, f: F) {
        self.data[i] = self.data[i].clone() + f.clone();
        if i < self.n() {
            self.lazy[i] = self.lazy[i].clone() + f;
        }
    }

    fn propagate(&mut self, i: usize) {
        let f = self.lazy[i].clone();
        self.apply_node(i << 1, f.clone());
        self.apply_node(i << 1 | 1, f);
        self.lazy[i] = F::e();
    }

    fn pull(&mut self, i: usize) {
        for j in (1..self.height()).rev() {
            self.propagate(i >> j);
        }
    }

    fn merge_above(&mut self, mut i: usize) {
        while i > 1 {
            i >>= 1;
            self.merge(i);
        }
    }

    pub fn apply(&mut self, mut l: usize, mut r: usize, f: F) {
        assert!(l <= r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        let l0 = l >> l.trailing_zeros();
        let r0 = (r >> r.trailing_zeros()) - 1;
        self.pull(l0);
        self.pull(r0);
        while l < r {
            if l & 1 == 1 {
                self.apply_node(l, f.clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                self.apply_node(r, f.clone());
            }
            l >>= 1;
            r >>= 1;
        }
        self.merge_above(l0);
        self.merge_above(r0);
    }

    pub fn set(&mut self, mut i: usize, x: S) {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i] = x;
        self.merge_above(i);
    }

    pub fn fold(&mut self, mut l: usize, mut r: usize) -> S {
        assert!(l <= r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        self.pull(l);
        self.pull(r - 1);
        let mut vl = S::e();
        let mut vr = S::e();
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

    pub fn max_right<G>(&mut self, is_ok: &G, l: usize) -> usize
    where
        G: Fn(&S) -> bool,
    {
        assert!(l <= self.size);
        if l == self.size {
            return self.size;
        }
        let n = self.n();
        let mut v = S::e();
        let mut i = n + l;
        self.pull(i);
        loop {
            i >>= i.trailing_zeros();
            let nv = v.clone() + self.data[i].clone();
            if !is_ok(&nv) {
                break;
            }
            v = nv;
            i += 1;
            if i.count_ones() == 1 {
                return self.size;
            }
        }
        while i < n {
            self.propagate(i);
            i <<= 1;
            let nv = v.clone() + self.data[i].clone();
            if !is_ok(&nv) {
                continue;
            }
            v = nv;
            i += 1;
        }
        i - n
    }

    pub fn min_left<G>(&mut self, is_ok: &G, r: usize) -> usize
    where
        G: Fn(&S) -> bool,
    {
        assert!(r <= self.size);
        if r == 0 {
            return 0;
        }
        let n = self.n();
        let mut v = S::e();
        let mut i = n + r;
        self.pull(i - 1);
        loop {
            debug_assert!(i >= 1);
            i >>= i.trailing_zeros();
            let nv = self.data[i - 1].clone() + v.clone();
            if !is_ok(&nv) {
                break;
            }
            i -= 1;
            v = nv;
            if i == 0 || i.count_ones() == 1 {
                return 0;
            }
        }
        while i < n {
            debug_assert!(i >= 1);
            self.propagate(i - 1);
            i <<= 1;
            let nv = self.data[i - 1].clone() + v.clone();
            if !is_ok(&nv) {
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
    #[test]
    fn test() {}
}
