pub fn morris_pratt_table<T: PartialEq>(a: &[T]) -> Vec<usize> {
    let n = a.len();
    let mut lb = vec![0; n]; // longest border
    let mut d = 0;
    for i in 1..n {
        while d != 0 && a[d] != a[i] {
            d = lb[d - 1];
        }
        if a[d] == a[i] {
            d += 1;
        }
        lb[i] = d;
    }
    lb
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        // refs: en-wiki
        let cases = [
            ("abcdabd", vec![0, 0, 0, 0, 1, 2, 0]),
            ("abacababc", vec![0, 0, 1, 0, 1, 2, 3, 2, 0]),
            ("abacababa", vec![0, 0, 1, 0, 1, 2, 3, 2, 3]),
            ("participate in parachute", vec![
                0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0,
                0, 0, 0,
            ]),
        ];
        for (s, ans) in cases {
            let s = s.chars().collect::<Vec<_>>();
            assert_eq!(morris_pratt_table(&s), ans);
        }
    }
}
