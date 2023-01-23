use crate::binary_search_on_slice_bisection_of_ng_ok::binary_search;
pub fn upper_bound<T: PartialOrd>(
    monotonic_sequence: &[T],
    x: &T,
) -> usize {
    binary_search(&|y: &T| y > x, monotonic_sequence)
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let v = (0..10).collect::<Vec<_>>();
        assert_eq!(upper_bound(&v, &-1), 0);
        assert_eq!(upper_bound(&v, &0), 1);
        assert_eq!(upper_bound(&v, &15), 10);
    }
}
