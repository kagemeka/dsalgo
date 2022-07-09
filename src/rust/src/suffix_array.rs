pub fn doubling_counting_sort(a: &Vec<usize>) -> Vec<usize> {
    use crate::array_compression_unique_binary_search::ArrayCompression;
    let n = a.len();
    let counting_sort_key = |a: &Vec<usize>| -> Vec<usize> {
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
    let mut rank = ArrayCompression::once(a.to_vec());
    let mut k = 1usize;
    let mut key = vec![0; n];
    let mut first = vec![0; n];
    let mut second = vec![0; n];
    let mut sa = vec![0; n];
    loop {
        for i in 0..n {
            second[i] = if i + k < n { 1 + rank[i + k] } else { 0 };
        }
        let rank_second = counting_sort_key(&second);
        for i in 0..n {
            first[i] = rank[rank_second[i]];
        }
        let rank_first = counting_sort_key(&first);
        for i in 0..n {
            sa[i] = rank_second[rank_first[i]];
        }
        for i in 0..n {
            key[i] = first[rank_first[i]] << 30 | second[sa[i]];
        }
        rank[sa[0]] = 0;
        for i in 0..n - 1 {
            rank[sa[i + 1]] = rank[sa[i]];
            if key[i + 1] > key[i] {
                rank[sa[i + 1]] += 1;
            }
        }
        k <<= 1;
        if k >= n {
            break;
        }
    }
    sa
}
#[cfg(test)]
mod tests {
    #[test]
    fn suffix_array() {
        let s = vec![1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0];
        let answer = vec![15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4];
        assert_eq!(super::doubling_counting_sort(&s), answer,);
    }
}
