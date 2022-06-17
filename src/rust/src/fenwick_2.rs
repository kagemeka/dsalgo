//! fenwick tree (binary indexed tree)

use crate::{
    algebraic_structure::*,
    binary_function::*,
    bitops::{lsb_number, reset_least_bit},
};

/// Node Indices
/// (case $|given array| = 8$,
/// internally 1-indexed implemetation)
/// |8              |
/// |4      |       |
/// |2  |   |6  |   |
/// |1| |3| |5| |7| |
pub struct Fenwick<G: Monoid> {
    data: Vec<G::S>, // data
}

impl<G> Fenwick<G>
where
    G: Monoid + Commutative,
    G::S: Clone,
{
    /// you need to pass initial values because,
    /// it might not be identity element.
    pub fn new(a: Vec<G::S>) -> Self {
        let size = a.len();
        let mut d = vec![G::e()];
        d.append(&mut a.to_vec());
        for i in 1..size {
            let j = i + lsb_number(i as u64) as usize;
            if j <= size {
                d[j] = G::op(d[j].clone(), d[i].clone());
            }
        }
        Self { data: d }
    }

    pub fn size(&self) -> usize { self.data.len() - 1 }

    pub fn operate(&mut self, mut i: usize, v: G::S) {
        i += 1;
        while i <= self.size() {
            self.data[i] = G::op(self.data[i].clone(), v.clone());
            i += lsb_number(i as u64) as usize;
        }
    }

    // reduce less than.
    pub fn reduce_lt(&self, mut i: usize) -> G::S {
        let mut v = G::e();
        while i > 0 {
            v = G::op(v, self.data[i].clone());
            i = reset_least_bit(i as u64) as usize;
        }
        v
    }

    pub fn max_right<F>(&self, is_ok: &F) -> usize
    where
        F: Fn(&G::S) -> bool,
    {
        let mut len = (self.size() + 1).next_power_of_two();
        let mut v = G::e();
        let mut r = 0;
        loop {
            len >>= 1;
            if len == 0 {
                return r;
            }
            if r + len > self.size() {
                continue;
            }
            let nv = G::op(
                v.clone(),
                self.data[r + len].clone(),
            );
            if is_ok(&nv) {
                r += len;
                v = nv;
            }
        }
    }
}

impl<G> Fenwick<G>
where
    G: AbelianGroup,
    G::S: Clone,
{
    pub fn reduce(&self, l: usize, r: usize) -> G::S {
        assert!(l <= r);
        G::op(
            G::inv(self.reduce_lt(l)),
            self.reduce_lt(r),
        )
    }

    pub fn get(&self, i: usize) -> G::S { self.reduce(i, i + 1) }

    /// find r such that \prod[l, r) = true
    pub fn max_right_from<F>(&self, is_ok: &F, l: usize) -> usize
    where
        F: Fn(&G::S) -> bool,
    {
        assert!(l <= self.size());
        let mut len = (self.size() + 1).next_power_of_two();
        let mut v = G::inv(self.reduce_lt(l));
        let mut r = 0;
        loop {
            len >>= 1;
            if len == 0 {
                debug_assert!(l <= r);
                return r;
            }
            if r + len > self.size() {
                continue;
            }
            let nv = G::op(
                v.clone(),
                self.data[r + len].clone(),
            );
            if r + len <= l || r + len <= self.size() && is_ok(&nv) {
                r += len;
                v = nv;
            }
        }
    }

    /// find l such that \prod[l, r) = true, or return r
    pub fn min_left_from<F>(&self, is_ok: &F, r: usize) -> usize
    where
        F: Fn(&G::S) -> bool,
    {
        assert!(r <= self.size());
        if r == 0 {
            return 0;
        }
        let mut len = (self.size() + 1).next_power_of_two();
        let mut v = self.reduce_lt(r);
        if is_ok(&v) {
            return 0;
        }
        let mut l = 1;
        loop {
            len >>= 1;
            if len == 0 {
                debug_assert!(l <= r);
                return l;
            }
            if l + len > r {
                continue;
            }
            let nv = G::op(
                G::inv(self.data[l + len - 1].clone()),
                v.clone(),
            );
            if !is_ok(&nv) {
                l += len;
                v = nv;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_as_abelian_group() {
        use crate::{
            algebraic_structure_impl::GroupApprox,
            group_theory_id::Additive,
        };

        let arr = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

        let mut fw = Fenwick::<GroupApprox<i32, Additive>>::new(arr);

        assert_eq!(fw.reduce(0, 10), 45);
        assert_eq!(fw.reduce(6, 10), 30);
        fw.operate(5, 10);
        assert_eq!(fw.reduce(6, 10), 30);
        assert_eq!(fw.reduce_lt(5), 10);
        assert_eq!(fw.reduce_lt(6), 25);
        assert_eq!(fw.get(5), 15);
        let is_ok = |x: &i32| *x <= 25;
        assert_eq!(fw.max_right(&is_ok), 6);
        assert_eq!(fw.max_right_from(&is_ok, 0), 6);
        let is_ok = |x: &i32| *x < 25;
        assert_eq!(fw.max_right(&is_ok), 5);
        assert_eq!(fw.max_right_from(&is_ok, 0), 5);
        assert_eq!(fw.max_right_from(&is_ok, 4), 6);
        assert_eq!(fw.max_right_from(&is_ok, 5), 7);
        assert_eq!(fw.max_right_from(&is_ok, 6), 9);
        assert_eq!(
            fw.max_right_from(&is_ok, 9),
            10
        );
        assert_eq!(fw.min_left_from(&is_ok, 10), 7);
        assert_eq!(fw.min_left_from(&is_ok, 0), 0);
        assert_eq!(fw.min_left_from(&is_ok, 6), 2);
        assert_eq!(fw.min_left_from(&is_ok, 5), 0);
        let is_ok = |x: &i32| *x < 15;
        assert_eq!(fw.max_right_from(&is_ok, 5), 5);
        assert_eq!(fw.min_left_from(&is_ok, 6), 6);
        assert_eq!(fw.min_left_from(&is_ok, 10), 9);
        let is_ok = |x: &i32| *x < 9;
        assert_eq!(
            fw.min_left_from(&is_ok, 10),
            10
        );
    }
}
