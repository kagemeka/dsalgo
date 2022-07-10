pub fn normalize(mut a: Vec<usize>, offset: usize) -> Vec<usize> {
    let mn = *a.iter().min().unwrap_or(&0);
    for x in a.iter_mut() {
        *x = *x - mn + offset;
    }
    a
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let a = vec![2, 4, 1];
        assert_eq!(normalize(a, 3), [4, 6, 3]);
    }
}
