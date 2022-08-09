use std::ops::*;

use crate::{
    matrix_with_static_property::Matrix,
    static_matrix_property_trait::{ElementType, Shape},
    static_square_matrix_property_trait::Size,
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
            for k in 0..n {
                for j in 0..n {
                    res[(i, j)] += self[(i, k)] * rhs[(k, j)];
                }
            }
        }
        res
    }
}
