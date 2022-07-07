pub trait Shape {
    fn shape() -> (usize, usize);
}

pub trait Len {
    fn len() -> usize;
}

impl<T: Shape> Len for T {
    fn len() -> usize {
        let (h, w) = Self::shape();
        h * w
    }
}

pub trait ElementType {
    type T;
}
