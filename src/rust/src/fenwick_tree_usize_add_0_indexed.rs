pub struct Fenwick(Vec<usize>);
impl Fenwick {
    pub fn new(size: usize) -> Self { Self(vec![0; size]) }

    pub fn add(&mut self, mut i: usize, x: usize) {
        while i < self.0.len() {
            self.0[i] += x;
            i += i + 1;
        }
    }

    pub fn get(&self, mut i: usize) -> usize {
        let mut v = 0;
        loop {
            v += self.0[i];
            i = i & (i + 1);
            if i == 0 {
                return v;
            }
            i -= 1;
        }
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut fw = Fenwick::new(10);
        fw.add(5, 1);
        assert_eq!(fw.get(4), 0);
        assert_eq!(fw.get(5), 1);
    }
}
