use crate::{algebraic_structure::*, isqrt};

pub struct SqrtDecomposition<G: Semigroup> {
    pub(crate) data: Vec<G::S>,
    pub(crate) buckets: Vec<G::S>,
}

impl<G: Semigroup> SqrtDecomposition<G> {
    pub fn size(&self) -> usize { self.data.len() }

    pub(crate) fn sqrt(&self) -> usize {
        let n = self.buckets.len();
        (self.size() + n - 1) / n
    }
}

impl<G> std::iter::FromIterator<G::S> for SqrtDecomposition<G>
where
    G: Semigroup,
    G::S: Clone,
{
    fn from_iter<T: IntoIterator<Item = G::S>>(iter: T) -> Self {
        let data = iter.into_iter().collect::<Vec<_>>();
        let size = data.len();
        let n = isqrt::floor(size as u64) as usize;
        let buckets = (0..(size + n - 1) / n)
            .map(|j| {
                // data[j * n..std::cmp::min((j + 1) * n, size)]
                //     .iter()
                //     .cloned()
                //     .reduce(|l, r| G::op(l, r))
                //     .unwrap()
                // CHANGE LATER: reduce is not supported on atcoder yet.

                let mut iter = data[j * n..std::cmp::min((j + 1) * n, size)]
                    .iter()
                    .cloned();
                let mut v = iter.next().unwrap();
                for x in iter {
                    v = G::op(v, x);
                }
                v
            })
            .collect();
        Self { data, buckets }
    }
}

impl<G> SqrtDecomposition<G>
where
    G: Semigroup,
    G::S: Clone,
{
    pub(crate) fn update(&mut self, bucket: usize) {
        let j = bucket;
        let n = self.sqrt();
        // self.buckets[j] = self.data
        //     [j * n..std::cmp::min((j + 1) * n, self.size())]
        //     .iter()
        //     .cloned()
        //     .reduce(|l, r| G::op(l, r))
        //     .unwrap();
        // CHANGE LATER: reduce is not supported on atcoder yet.
        let mut iter = self.data
            [j * n..std::cmp::min((j + 1) * n, self.size())]
            .iter()
            .cloned();
        let mut v = iter.next().unwrap();
        for x in iter {
            v = G::op(v, x);
        }
        self.buckets[j] = v;
    }

    pub fn apply<F>(&mut self, i: usize, f: F)
    where
        F: FnOnce(G::S) -> G::S,
    {
        self.data[i] = f(self.data[i].clone());
        self.update(i / self.sqrt());
    }

    // TODO: move out from core implementation.
    // because set can be defined as application of 'replacement'
    // (the core is apply method)
    pub fn set(&mut self, i: usize, x: G::S) {
        self.data[i] = x;
        self.update(i / self.sqrt());
    }

    pub fn reduce(&self, l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        // just for early panic. it's not necessary to be checked here.
        let n = self.sqrt();
        // (0..self.buckets.len())
        //     .filter_map(|j| {
        //         if r <= n * j || n * (j + 1) <= l {
        //             return None;
        //         }
        //         if l <= n * j && n * (j + 1) <= r {
        //             return Some(self.buckets[j].clone());
        //         }
        //         (0..n)
        //             .filter_map(|k| {
        //                 let i = j * n + k;
        //                 if l <= i && i < r {
        //                     Some(self.data[i].clone())
        //                 } else {
        //                     None
        //                 }
        //             })
        //             .reduce(|l, r| G::op(l, r))
        //     })
        //     .reduce(|l, r| G::op(l, r))
        // CHANGE LATER: reduce is not supported on atcoder yet.

        let mut iter = (0..self.buckets.len()).filter_map(|j| {
            if r <= n * j || n * (j + 1) <= l {
                return None;
            }
            if l <= n * j && n * (j + 1) <= r {
                return Some(self.buckets[j].clone());
            }

            let mut iter = (0..n).filter_map(|k| {
                let i = j * n + k;
                if l <= i && i < r { Some(self.data[i].clone()) } else { None }
            });
            let mut v = iter.next().unwrap();
            for x in iter {
                v = G::op(v, x);
            }
            Some(v)
        });
        let mut v = iter.next().unwrap();
        for x in iter {
            v = G::op(v, x);
        }
        v
    }
}

/// fast reduce
impl<G> SqrtDecomposition<G>
where
    G: Semigroup,
    G::S: Clone,
{
    /// faster with constant time optimization.
    /// more strictly, 2-times faster for random range queries mathematically.
    pub fn fast_reduce(&self, mut l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        let n = self.sqrt();
        let mut v = self.data[l].clone();
        l += 1;
        let lj = (l + n - 1) / n;
        let rj = r / n;
        if rj < lj {
            for i in l..r {
                v = G::op(v, self.data[i].clone());
            }
            return v;
        }
        for i in l..lj * n {
            v = G::op(v, self.data[i].clone());
        }
        for j in lj..rj {
            v = G::op(v, self.buckets[j].clone());
        }
        for i in rj * n..r {
            v = G::op(v, self.data[i].clone());
        }
        v
    }
}

use crate::{algebraic_structure_impl::*, query::RangeGetQuery};

impl<S, I> RangeGetQuery<I> for SqrtDecomposition<GroupApprox<S, I>>
where
    GroupApprox<S, I>: Semigroup<S = S>,
    S: Clone,
{
    type T = S;

    fn get_range(&mut self, l: usize, r: usize) -> Self::T {
        self.fast_reduce(l, r)
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
