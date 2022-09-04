/// able to compute (k <= 2^max_exp)-th from any node in O(max_exp) time
pub fn doubling_table(f: &[usize], max_exp: usize) -> Vec<Vec<usize>> {
    let n = f.len();
    let mut a = Vec::with_capacity(max_exp + 1);
    a.push(f.to_owned());
    for i in 0..max_exp {
        let row = &a[i];
        a.push((0..n).map(|j| row[row[j]]).collect());
    }
    a
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
