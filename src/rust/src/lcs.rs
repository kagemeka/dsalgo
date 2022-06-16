//! Longest Common Subsequence
//! not confused with Longest Common Substring

/// compute dp table.
#[allow(dead_code)]
pub(crate) fn dp<T: PartialEq>(a: &[T], b: &[T]) -> Vec<Vec<usize>> {
    let n = a.len();
    let m = b.len();
    let mut l = vec![vec![0; m + 1]; n + 1]; // length
    for i in 0..n {
        for j in 0..m {
            if a[i] == b[j] {
                debug_assert!(l[i + 1][j + 1] <= l[i][j] + 1);
                l[i + 1][j + 1] = l[i][j] + 1;
                continue;
            }
            l[i + 1][j + 1] = std::cmp::max(l[i][j + 1], l[i + 1][j]);
        }
    }
    l
}

pub fn len<T: PartialEq>(a: &[T], b: &[T]) -> usize {
    dp(a, b)[a.len()][b.len()]
}

#[allow(dead_code)]
pub(crate) fn len_low_mem<T: PartialEq>(a: &[T], b: &[T]) -> usize {
    let m = b.len();
    let mut length = vec![0; m + 1];
    for x in a {
        for j in (0..m).rev() {
            if x == &b[j] {
                debug_assert!(length[j + 1] <= length[j] + 1);
                length[j + 1] = length[j] + 1;
            }
        }
        for j in 0..m {
            length[j + 1] = std::cmp::max(length[j], length[j + 1]);
        }
    }
    length[m]
}

/// restore one of the transtion histories.
pub(crate) fn restore_indices(dp: &[Vec<usize>]) -> Vec<(usize, usize)> {
    let mut indices = vec![];
    let mut i = dp.len() - 1;
    let mut j = dp[0].len() - 1;
    while i > 0 && j > 0 {
        let l = dp[i][j];
        if dp[i][j - 1] == l {
            j -= 1;
            continue;
        }
        if dp[i - 1][j] == l {
            i -= 1;
            continue;
        }
        i -= 1;
        j -= 1;
        indices.push((i, j));
    }
    indices.reverse();
    indices
}

pub fn struct_one<T: PartialEq + Clone>(a: &[T], b: &[T]) -> Vec<T> {
    restore_indices(&dp(a, b))
        .into_iter()
        .map(|(i, _)| a[i].clone())
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_dp() {
        let s = "axyb".chars().collect::<Vec<_>>();
        let t = "abyxb".chars().collect::<Vec<_>>();
        let lcs = dp(&s, &t);
        let ans = vec![
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 2, 2],
            [0, 1, 1, 2, 2, 2],
            [0, 1, 2, 2, 2, 3],
        ];
        assert_eq!(lcs, ans);
    }

    #[test]
    fn test_len() {
        let s = "axyb".chars().collect::<Vec<_>>();
        let t = "abyxb".chars().collect::<Vec<_>>();
        assert_eq!(len(&s, &t), 3);
    }

    #[test]
    fn test() {
        let s = "axyb".chars().collect::<Vec<_>>();
        let t = "abyxb".chars().collect::<Vec<_>>();
        assert_eq!(len_low_mem(&s, &t), 3);
    }

    #[test]
    fn test_restore_indices() {
        let s = "axyb".chars().collect::<Vec<_>>();
        let t = "abyxb".chars().collect::<Vec<_>>();
        let indices = restore_indices(&dp(&s, &t));
        assert_eq!(
            indices,
            vec![(0, 0), (2, 2), (3, 4)]
        );
        // ayb
    }

    #[test]
    fn test_struct_one() {
        let s = "axyb".chars().collect::<Vec<_>>();
        let t = "abyxb".chars().collect::<Vec<_>>();
        assert_eq!(
            struct_one(&s, &t),
            vec!['a', 'y', 'b']
        );
    }
}
