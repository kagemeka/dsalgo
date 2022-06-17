use crate::{algebraic_structure::*, binary_function::*};

pub struct SparseTable<G: Semigroup> {
    data: Vec<Vec<G::S>>,
}

impl<G> std::iter::FromIterator<G::S> for SparseTable<G>
where
    G: Semigroup + Idempotence + Commutative,
    G::S: Clone,
{
    fn from_iter<T: IntoIterator<Item = G::S>>(iter: T) -> Self {
        let mut data = vec![iter.into_iter().collect::<Vec<_>>()];
        let max_width = data[0].len();
        let height = if max_width <= 1 {
            1
        } else {
            max_width.next_power_of_two().trailing_zeros() as usize
        };
        for i in 1..height {
            let row_size = max_width - (1 << i) + 1;
            // last is max_width - (1 << i) covering (1 << i)
            // including the position.
            data.push(
                (0..row_size)
                    .map(|j| {
                        G::op(
                            data[i - 1][j].clone(),
                            data[i - 1][j + (1 << (i - 1))].clone(),
                        )
                    })
                    .collect(),
            );
        }
        Self { data }
    }
}

impl<G> SparseTable<G>
where
    G: Semigroup + Idempotence + Commutative,
    G::S: Clone,
{
    pub fn new(slice: &[G::S]) -> Self {
        Self::from_iter(slice.iter().cloned())
    }

    pub fn size(&self) -> usize { self.data[0].len() }

    pub fn reduce(&self, l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        if r - l == 1 {
            return self.data[0][l].clone();
        }
        let i = (r - l).next_power_of_two().trailing_zeros() as usize - 1;
        G::op(
            self.data[i][l].clone(),
            self.data[i][r - (1 << i)].clone(),
        )
    }
}

use crate::{algebraic_structure_impl::*, range_get_query::RangeGetQuery};

impl<S, I> RangeGetQuery<I> for SparseTable<GroupApprox<S, I>>
where
    GroupApprox<S, I>: Semigroup<S = S> + Idempotence + Commutative,
    S: Clone,
{
    type T = S;

    fn get_range(&mut self, l: usize, r: usize) -> Self::T { self.reduce(l, r) }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_self_as_min() {
        use crate::grouop_theory_id::Min;

        let arr: Vec<usize> = vec![0, 4, 2, 8, 5, 1];
        let sp = SparseTable::<GroupApprox<usize, Min>>::new(&arr);
        assert_eq!(sp.reduce(0, 4), 0);
        assert_eq!(sp.reduce(3, 4), 8);
        assert_eq!(sp.reduce(1, 6), 1);
    }
}
