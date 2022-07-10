pub fn argsort(mut a: Vec<usize>) -> Vec<usize> {
    let n = a.len();
    let mut m = *a.iter().min().unwrap();
    for i in 0..n {
        a[i] -= m;
    }
    m = *a.iter().max().unwrap();
    let mut arg = vec![0; m + 2];
    for &x in a.iter() {
        arg[x + 1] += 1;
    }
    for i in 0..m + 1 {
        arg[i + 1] += arg[i];
    }
    let mut res = vec![0; n];
    for i in 0..n {
        res[arg[a[i]]] = i;
        arg[a[i]] += 1;
    }
    res
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut a = vec![7, 2, 1, 3, 2, 1];
        assert_eq!(argsort(a), [2, 5, 1, 4, 3, 0]);
    }
}