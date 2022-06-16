pub trait RangeGetQuery<I> {
    type T;
    fn get_range(&mut self, l: usize, r: usize) -> Self::T;
}
