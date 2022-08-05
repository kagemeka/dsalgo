pub struct SparseTable<T, F> {
    data: Vec<Vec<T>>,
    f: F,
}
impl<T: Clone, F: Fn(T, T) -> T> SparseTable<T, F> {
    pub fn new(f: F, a: &[T]) -> Self {
        let n = a.len();
        assert!(n > 0);
        let h = n.next_power_of_two().trailing_zeros().max(1) as usize;
        let mut data = vec![vec![]; h];
        data[0] = a.to_vec();
        for i in 1..h {
            let d1 = 1 << i;
            let d0 = d1 >> 1;
            let w = n - d1 + 1;
            data[i] = (0..w)
                .map(|j| f(data[i - 1][j].clone(), data[i - 1][j + d0].clone()))
                .collect();
        }
        Self { data, f }
    }

    pub fn size(&self) -> usize { self.data[0].len() }

    pub fn get(&self, l: usize, r: usize) -> T {
        assert!(l < r && r <= self.size());
        if r - l == 1 {
            return self.data[0][l].clone();
        }
        let i = (r - l).next_power_of_two().trailing_zeros() as usize - 1;
        (self.f)(self.data[i][l].clone(), self.data[i][r - (1 << i)].clone())
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let a: Vec<usize> = vec![0, 4, 2, 8, 5, 1];
        let f = |a: usize, b: usize| a.min(b);
        let sp = SparseTable::new(&f, &a);
        assert_eq!(sp.get(0, 4), 0);
        assert_eq!(sp.get(3, 4), 8);
        assert_eq!(sp.get(1, 6), 1);
    }
}
