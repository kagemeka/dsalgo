/// O(N\log^2{N})
pub fn suffix_array(mut a: Vec<usize>) -> Vec<usize> {
    use crate::array_compression_unique_binary_search::ArrayCompression;
    let n = a.len();
    let mut d = 1usize;
    loop {
        for i in 0..n {
            a[i] = a[i] << 30;
            if i + d < n {
                a[i] |= 1 + a[i + d];
            }
        }
        a = ArrayCompression::once(a);
        d <<= 1;
        if d >= n {
            break;
        }
    }
    let mut sa = (0..n).collect::<Vec<_>>();
    sa.sort_by_key(|&i| a[i]);
    sa
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
