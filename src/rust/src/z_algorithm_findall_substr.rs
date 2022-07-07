pub fn z_algorithm_findall<T: PartialEq + Clone>(
    a: &[T], pattern: &[T],
) -> Vec<usize> {
    use crate::z_algorithm::z_algorithm;
    let mut s = pattern.to_vec();
    let n = s.len();
    s.append(&mut a.to_vec());
    z_algorithm(&s)[n..]
        .iter()
        .enumerate()
        .filter_map(|(i, &z)| if z >= n { Some(i) } else { None })
        .collect()
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let s = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'c'];
        assert_eq!(z_algorithm_findall(&s, &['a', 'b', 'a']), [0, 2, 4]);
    }
}
