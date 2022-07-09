pub struct ArrayCompression<T>(Vec<T>);
impl<T: Ord + Clone> ArrayCompression<T> {
    pub fn new(a: Vec<T>) -> Self { Self(crate::vector_unique::unique(a)) }

    pub fn encode(&self, v: &T) -> usize { self.0.binary_search(v).unwrap() }

    pub fn inv(&self, i: usize) -> T { self.0[i].clone() }

    pub fn once(a: Vec<T>) -> Vec<usize> {
        let f = Self::new(a.clone());
        a.iter().map(|x| f.encode(x)).collect()
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let arr = [4, 3, 0, -1, 3, 10];
        let f = ArrayCompression::new(arr.to_vec());
        assert_eq!(f.encode(&-1), 0);
        assert_eq!(f.encode(&10), 4);
        assert_eq!(f.inv(0), -1);
        // f.encode(&5); // error
        assert_eq!(ArrayCompression::once(arr.to_vec()), vec![
            3, 2, 1, 0, 2, 4
        ]);
    }
}
