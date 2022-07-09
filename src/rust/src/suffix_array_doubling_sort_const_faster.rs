/// O(N\log^2{N})
pub fn suffix_array(mut a: Vec<usize>) -> Vec<usize> {
    let n = a.len();
    let mut rank = vec![0; n];
    let mut sa = vec![0; n];
    let mut d = 1usize;
    loop {
        for i in 0..n {
            a[i] = a[i] << 30;
            if i + d < n {
                a[i] |= 1 + a[i + d];
            }
            sa[i] = i;
        }
        sa.sort_by_key(|&i| a[i]);
        d <<= 1;
        if d >= n {
            return sa;
        }
        rank[sa[0]] = 0;
        for i in 0..n - 1 {
            rank[sa[i + 1]] =
                rank[sa[i]] + if a[sa[i + 1]] != a[sa[i]] { 1 } else { 0 };
        }
        std::mem::swap(&mut a, &mut rank);
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let s = vec![1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0];
        let answer = vec![15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4];
        assert_eq!(suffix_array(s), answer);
    }
}
