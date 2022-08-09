use std::ops::*;

use crate::static_matrix_property_trait::{ElementType, Len, Shape};
pub struct Matrix<P: ElementType>(Vec<P::T>);
impl<P: ElementType> Matrix<P> {
    pub fn new<F>(default: F) -> Self
    where
        F: Fn() -> P::T,
        P: Len,
    {
        Self((0..P::len()).map(|_| default()).collect())
    }
}
impl<P> Default for Matrix<P>
where
    P::T: Default,
    P: ElementType + Len,
{
    fn default() -> Self { Self::new(|| P::T::default()) }
}
impl<P> Index<(usize, usize)> for Matrix<P>
where
    P: ElementType + Shape,
{
    type Output = P::T;

    fn index(&self, index: (usize, usize)) -> &Self::Output {
        let (i, j) = index;
        &self.0[i * P::shape().0 + j]
    }
}
impl<P> IndexMut<(usize, usize)> for Matrix<P>
where
    P: ElementType + Shape,
{
    fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
        let (i, j) = index;
        &mut self.0[i * P::shape().0 + j]
    }
}
