/// d(n) table. d(0) := 0 here.
/// O(N\log{N})
pub fn number_of_divisors(size: usize) -> Vec<u64> {
    let mut cnt = vec![1; size];
    cnt[0] = 0;
    for i in (1..size).rev() {
        for j in (i << 1..size).step_by(i) {
            cnt[j] += cnt[i];
        }
    }
    cnt
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::*;
        assert_eq!(number_of_divisors(10), [0, 1, 2, 2, 3, 2, 4, 2, 4, 3]);
    }
}
