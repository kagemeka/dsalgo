pub fn morris_pratt_table<T: PartialEq>(a: &[T]) -> Vec<isize> {
    let n = a.len();
    let mut lb = vec![0; n + 1];
    let mut d = -1;
    lb[0] = d;
    for i in 0..n {
        while d != -1 && a[d as usize] != a[i] {
            d = lb[d as usize]
        }
        d += 1;
        lb[i + 1] = d;
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
            (
                "abcdabd",
                vec![-1, 0, 0, 0, 0, 1, 2, 0],
            ),
            (
                "abacababc",
                vec![-1, 0, 0, 1, 0, 1, 2, 3, 2, 0],
            ),
            (
                "abacababa",
                vec![-1, 0, 0, 1, 0, 1, 2, 3, 2, 3],
            ),
            (
                "participate in parachute",
                vec![
                    -1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 3,
                    0, 0, 0, 0, 0, 0,
                ],
            ),
        ];

        for (s, ans) in cases {
            let s = s.chars().collect::<Vec<_>>();
            assert_eq!(morris_pratt_table(&s), ans);
        }
    }
}
