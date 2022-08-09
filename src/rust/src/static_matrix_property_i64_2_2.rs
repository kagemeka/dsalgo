use crate::{
    static_matrix_property_trait::{ElementType, Shape},
    static_square_matrix_property_trait::Size,
};
pub struct MatrixPropI6422;
impl Size for MatrixPropI6422 {
    fn size() -> usize { 2 }
}
impl Shape for MatrixPropI6422 {
    fn shape() -> (usize, usize) { (Self::size(), Self::size()) }
}
impl ElementType for MatrixPropI6422 {
    type T = i64;
}
