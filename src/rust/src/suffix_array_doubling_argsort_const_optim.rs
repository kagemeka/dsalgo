/// O(N\log^2{N})
pub fn suffix_array(mut a: Vec<usize>) -> Vec<usize> {
    let n = a.len();
    let mut d = 1;
    let mut sa: Vec<_> = (0..n).collect();
    loop {
        for i in 0..n {
            a[i] <<= 30;
            if i + d < n {
                a[i] |= 1 + a[i + d];
            }
        }
        sa.sort_unstable_by_key(|&i| a[i]);
        d <<= 1;
        if d >= n {
            return sa;
        }
        let mut rank = 0;
        let mut prev = a[sa[0]];
        for &i in sa.iter() {
            if a[i] > prev {
                rank += 1;
                prev = a[i];
            }
            a[i] = rank;
        }
        if rank == n {
            return sa;
        }
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
