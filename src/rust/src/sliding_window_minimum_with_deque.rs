pub fn sliding_window_minimum<T: Ord>(a: &[T], k: usize) -> Vec<usize> {
    let n = a.len();
    assert!(k <= n);
    let mut que = std::collections::VecDeque::new();
    let mut res = Vec::with_capacity(n - k + 1);
    let mut f = |i: usize| -> usize {
        if !que.is_empty() && que.front().unwrap() + k <= i {
            que.pop_front();
        }
        while !que.is_empty() && a[*que.back().unwrap()] >= a[i] {
            que.pop_back();
        }
        que.push_back(i);
        *que.front().unwrap()
    };
    for i in 0..k - 1 {
        f(i);
    }
    for i in k - 1..n {
        res.push(f(i));
    }
    res
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![
            ((vec![1, 3, -1, -3, 5, 3, 6, 7], 3), vec![-1, -3, -3, -3, 3, 3]),
            ((vec![1], 1), vec![1]),
        ];
        for ((a, k), ans) in cases {
            let idx = sliding_window_minimum(&a, k);
            let res: Vec<_> = idx.into_iter().map(|i| a[i]).collect();
            assert_eq!(res, ans);
        }
    }
}
