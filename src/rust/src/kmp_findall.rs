pub fn kmp_findall<T: PartialEq>(a: &[T], pattern: &[T]) -> Vec<usize> {
    use crate::kmp_table_0_indexed::kmp_table;
    let b = pattern;
    let (n, m) = (a.len(), b.len());
    let f = kmp_table(b);
    let mut indices = vec![];
    let mut j = 0;
    for i in 0..n {
        while j != 0 && b[j] != a[i] {
            j = f[j - 1];
        }
        if b[j] == a[i] {
            j += 1;
        }
        if j == m {
            indices.push(i + 1 - m);
            j = f[m - 1];
        }
    }
    indices
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let s = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'c'];
        assert_eq!(kmp_findall(&s, &['a', 'b', 'a']), [0, 2, 4]);
    }
}
