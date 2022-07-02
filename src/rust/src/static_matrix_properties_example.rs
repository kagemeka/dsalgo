use crate::{
    square_matrix_trait::Size,
    static_matrix_trait::{ElementType, Shape},
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
