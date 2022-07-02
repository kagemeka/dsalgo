use std::ops::*;

use crate::{
    square_matrix_trait::Size,
    static_matrix::Matrix,
    static_matrix_trait::{ElementType, Shape},
};

/// T should be semiring.
impl<P> Mul for Matrix<P>
where
    P: ElementType + Size + Shape,
    P::T: Mul<Output = P::T> + AddAssign + Copy + From<i32>,
    Self: IndexMut<(usize, usize), Output = P::T>,
{
    type Output = Self;

    fn mul(self, rhs: Self) -> Self::Output {
        let n = P::size();
        let mut res = Self::new(|| 0.into());
        for i in 0..n {
            for j in 0..n {
                for k in 0..n {
                    res[(i, j)] += self[(i, k)] * rhs[(k, j)];
                }
            }
        }
        res
    }
}
