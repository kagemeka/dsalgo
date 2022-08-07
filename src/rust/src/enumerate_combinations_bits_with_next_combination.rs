use crate::next_combination_bits::next_combination;
// def combinations_next_comb(
//     n: int,
//     k: int,
// ) -> typing.Generator[tuple[int, ...], None, None]:
//     a = tuple(range(n))
//     n = len(a)
//     if k < 0 or n < k:
//         return
//     if k == 0:
//         yield ()
//         return
//     limit = 1 << n
//     s = (1 << k) - 1
//     while s < limit:
//         yield tuple(a[i] for i in range(n) if s >> i & 1)
//         s = next_combination(s)
pub fn combinations(n: usize, k: usize) -> Vec<usize> {
    assert!(k <= n);
    if k == 0 {
        return vec![0];
    }
    let mut res = vec![];
    let mut s = (1 << k) - 1;
    let lim = 1 << n;
    while s < lim {}
    res.reverse();
    res
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
