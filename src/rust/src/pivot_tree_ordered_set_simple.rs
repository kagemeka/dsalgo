use crate::pivot_tree_node_usize_recurse::*;
pub struct PivotSet {
    root: Option<Box<Node>>,
    max_height: usize,
    size: usize,
}
impl PivotSet {
    pub fn new(max_size: usize) -> Self {
        let max_height =
            (max_size + 1).next_power_of_two().trailing_zeros() as usize;
        Self { root: None, max_height, size: 0 }
    }

    pub fn size(&self) -> usize { self.size }

    pub fn min_ge(&self, x: usize) -> Option<usize> {
        let v = Node::min_ok(|v| v >= x + 1, self.root.as_ref())?;
        Some(v - 1)
    }

    pub fn max_le(&self, x: usize) -> Option<usize> {
        let v = Node::max_ok(|v| v <= x + 1, self.root.as_ref())?;
        Some(v - 1)
    }

    pub fn contains(&self, x: usize) -> bool {
        if let Some(v) = self.min_ge(x) { v == x } else { false }
    }

    pub fn insert(&mut self, mut x: usize) {
        assert!(x < (1 << self.max_height) - 1);
        if self.contains(x) {
            return;
        }
        x += 1;
        if let Some(root) = self.root.as_mut() {
            root.insert(x);
        } else {
            self.root = Node::new(x, self.max_height)
        }
        self.size += 1;
    }

    pub fn remove(&mut self, x: usize) {
        if !self.contains(x + 1) {
            return;
        }
        self.root = Node::remove(self.root.take(), x + 1);
        self.size -= 1;
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a usize> {
        self.root.as_ref().unwrap().iter()
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut s = PivotSet::new(1 << 30);
        s.insert(1);
        assert_eq!(s.size(), 1);
        s.insert(0);
        assert_eq!(s.size(), 2);
        let n = 1 << 30;
        s.insert(n - 1);
        assert_eq!(s.size(), 3);
        assert_eq!(s.min_ge(2), Some(n - 1));
        assert_eq!(s.min_ge(1), Some(1));
        assert_eq!(s.min_ge(0), Some(0));
        assert_eq!(s.max_le(2), Some(1));
        assert_eq!(s.max_le(1), Some(1));
        assert_eq!(s.max_le(0), Some(0));
        assert!(s.contains(0));
        s.remove(0);
        assert!(!s.contains(0));
        for x in s.iter() {
            dbg!(x);
        }
    }
}
