pub fn normalize(mut a: Vec<usize>) -> Vec<usize> {
    let mn = *a.iter().min().unwrap_or(&0);
    for x in a.iter_mut() {
        *x -= mn;
    }
    a
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let a = vec![2, 4, 1];
        assert_eq!(normalize(a), [1, 3, 0]);
    }
}
