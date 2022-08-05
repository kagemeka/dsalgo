use crate::fenwick_tree_additive::Fenwick;
pub struct Multiset(Fenwick<i32>);
impl Multiset {
    pub fn new(less_than: usize) -> Self { Self(Fenwick::new(less_than)) }

    pub fn size(&self) -> usize { self.0.get(self.0.size()) as usize }

    pub fn count(&self, x: usize) -> i32 { self.0.get(x + 1) - self.0.get(x) }

    /// positive cnt: insert.
    /// negative cnt: remove. (|cnt| <= count(x))
    pub fn add(&mut self, x: usize, cnt: i32) { self.0.operate(x, cnt); }

    pub fn lower_bound(&self, x: usize) -> usize { self.0.get(x) as usize }

    pub fn upper_bound(&self, x: usize) -> usize { self.0.get(x + 1) as usize }

    pub fn get(&self, i: usize) -> usize {
        self.0.max_right(|&x| x as usize <= i)
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut s = Multiset::new(10);
        s.add(5, 2);
        assert_eq!(s.size(), 2);
        assert_eq!(s.count(5), 2);
        assert_eq!(s.count(0), 0);
        assert_eq!(s.lower_bound(5), 0);
        assert_eq!(s.upper_bound(5), 2);
        assert_eq!(s.get(0), 5);
        assert_eq!(s.get(1), 5);
        s.add(5, -2);
        assert_eq!(s.size(), 0);
    }
}
