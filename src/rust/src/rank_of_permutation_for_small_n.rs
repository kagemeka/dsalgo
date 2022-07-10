pub fn permutation_rank(p: &Vec<usize>) -> usize {
    let n = p.len();
    let mut s = (1usize << n) - 1;
    let mut fact = 1;
    let mut rank = 0;
    for i in 0..n {
        let j = p[n - 1 - i];
        rank += (j - (s & ((1 << j) - 1)).count_ones() as usize) * fact;
        s &= !(1 << j);
        fact *= i + 1;
    }
    rank
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![(vec![0, 2, 1], 1), (vec![2, 0, 1], 4)];
        for (p, r) in cases {
            assert_eq!(permutation_rank(&p), r);
        }
    }
}
