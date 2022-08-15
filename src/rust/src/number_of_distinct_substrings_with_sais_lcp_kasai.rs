use crate::{
    longest_common_prefix_array_kasai::lcp_array,
    suffix_array_induced_sort_recurse::sa_is,
};
pub fn count_substrings(a: &[usize]) -> usize {
    let sa = sa_is(a.to_vec());
    let lcp = lcp_array(&a, &sa);
    let n = sa.len();
    n * (n + 1) / 2 - lcp.iter().sum::<usize>()
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![
            (vec![0, 1, 2, 1, 2, 1, 0], 21),
            (vec![1, 0, 3, 3, 0, 3, 3, 0, 2, 2, 0], 53),
            (vec![0, 1, 0, 1, 0, 2, 0, 2, 0], 33),
            (vec![0, 0, 0, 0, 0], 5),
        ];
        for (a, ans) in cases {
            assert_eq!(count_substrings(&a), ans);
        }
    }
}
