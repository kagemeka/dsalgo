pub fn argmax<T: PartialOrd + Clone>(a: Vec<T>) -> usize {
    let (mut idx, mut mx) = (0, a[0].clone());
    for (i, x) in a.into_iter().enumerate() {
        if x > mx {
            idx = i;
            mx = x;
        }
    }
    idx
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let a = vec![3, 4, 0, 5, 0];
        assert_eq!(argmax(a), 3);
    }
}
