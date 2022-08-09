use std::{marker::PhantomData, ops::*};

use crate::static_matrix_property_trait::Shape;
#[derive(Debug, Clone, Eq, PartialEq)]
pub struct Matrix<T, P>(Vec<Vec<T>>, PhantomData<P>);
impl<T: Clone, P: Shape> Matrix<T, P> {
    pub fn new(fill_value: T) -> Self {
        let (h, w) = P::shape();
        Self(vec![vec![fill_value; w]; h], PhantomData)
    }
}
impl<T: Clone + Default, P: Shape> Default for Matrix<T, P> {
    fn default() -> Self { Self::new(T::default()) }
}
impl<T, P> Index<usize> for Matrix<T, P> {
    type Output = [T];

    fn index(&self, i: usize) -> &Self::Output { &self.0[i] }
}
impl<T, P> IndexMut<usize> for Matrix<T, P> {
    fn index_mut(&mut self, i: usize) -> &mut Self::Output { &mut self.0[i] }
}
