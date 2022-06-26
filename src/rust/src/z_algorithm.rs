pub fn z_algorithm<T>(a: &[T]) -> Vec<usize>
where
    T: PartialEq,
{
    let n = a.len();
    let mut lcp = vec![0; n];
    let mut l = 0;
    for i in 1..n {
        let r = l + lcp[l];
        let mut d = if r <= i { 0 } else { lcp[i - l].min(r - i) };
        while i + d < n && a[i + d] == a[d] {
            d += 1;
        }
        lcp[i] = d;
        if r < i + d {
            l = i;
        }
    }
    lcp[0] = n;
    lcp
}
