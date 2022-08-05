pub fn suffix_array(a: Vec<usize>) -> Vec<usize> {
    use crate::array_compression_unique_binary_search::ArrayCompression;
    let n = a.len();
    let counting_argsort = |a: &Vec<usize>| -> Vec<usize> {
        let mut cnt = vec![0; n + 2];
        for &x in a.iter() {
            cnt[x + 1] += 1;
        }
        let mut key = vec![0; n];
        for i in 0..n {
            cnt[i + 1] += cnt[i];
        }
        for i in 0..n {
            key[cnt[a[i]]] = i;
            cnt[a[i]] += 1;
        }
        key
    };
    let mut rank = ArrayCompression::once(a);
    let mut k = 1usize;
    let mut key = vec![0; n];
    let mut key_1 = vec![0; n];
    let mut key_10 = vec![0; n];
    let mut sa = vec![0; n];
    loop {
        for i in 0..n {
            key_1[i] = if i + k < n { 1 + rank[i + k] } else { 0 };
        }
        let sa_1 = counting_argsort(&key_1);
        for i in 0..n {
            key_10[i] = rank[sa_1[i]];
        }
        let sa_10 = counting_argsort(&key_10);
        for i in 0..n {
            sa[i] = sa_1[sa_10[i]];
            key[i] = key_10[sa_10[i]] << 30 | key_1[sa[i]];
        }
        k <<= 1;
        if k >= n {
            return sa;
        }
        rank[sa[0]] = 0;
        for i in 0..n - 1 {
            rank[sa[i + 1]] =
                rank[sa[i]] + if key[i + 1] > key[i] { 1 } else { 0 };
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
        assert_eq!(suffix_array(s), answer,);
    }
}
