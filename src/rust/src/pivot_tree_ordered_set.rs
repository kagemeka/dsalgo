use crate::pivot_tree_node_usize_with_size_recurse::*;
pub struct PivotSet {
    root: Option<Box<Node>>,
    max_height: usize,
}
impl PivotSet {
    pub fn new(max_height: usize) -> Self { Self { root: None, max_height } }

    pub fn size(&self) -> usize { Node::size(self.root.as_ref()) }

    pub fn lower_bound(&self, x: usize) -> usize {
        Node::binary_search(|v| v >= x + 1, self.root.as_ref())
    }

    pub fn upper_bound(&self, x: usize) -> usize {
        Node::binary_search(|v| v > x + 1, self.root.as_ref())
    }

    pub fn count(&self, x: usize) -> usize {
        self.upper_bound(x) - self.lower_bound(x)
    }

    pub fn contains(&self, x: usize) -> bool { self.count(x) > 0 }

    pub fn insert(&mut self, mut x: usize) {
        assert!(x < (1 << self.max_height) - 1);
        if self.contains(x) {
            return;
        }
        x += 1;
        if let Some(root) = self.root.as_mut() {
            root.insert(x);
        } else {
            self.root = Node::new(self.max_height, x);
        }
    }

    pub fn remove(&mut self, x: usize) {
        if !self.contains(x) {
            return;
        }
        let i = self.lower_bound(x);
        self.root = Node::remove(self.root.take().unwrap(), i);
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a usize> {
        self.root.as_ref().unwrap().iter()
    }

    pub fn get(&self, i: usize) -> usize {
        self.root.as_ref().unwrap().kth_node(i).value - 1
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let h = 31;
        let mut s = PivotSet::new(h);
        s.insert(1);
        assert_eq!(s.size(), 1);
        s.insert(0);
        assert_eq!(s.size(), 2);
        s.insert(1 << (h - 1));
        assert_eq!(s.size(), 3);
        assert_eq!(s.get(2), 1 << (h - 1));
        assert_eq!(s.get(1), 1);
        assert_eq!(s.get(0), 0);
        assert!(s.contains(0));
        s.remove(0);
        assert!(!s.contains(0));
        for x in s.iter() {
            dbg!(x);
        }
    }
    #[test]
    fn test_abc217() {
        let cases = vec![
            (5, vec![((2, 2), 5), ((1, 3), 0), ((2, 2), 3)]),
            (5, vec![((1, 2), 0), ((1, 4), 0), ((2, 3), 2)]),
            (100, vec![
                ((1, 31), 0),
                ((2, 41), 69),
                ((1, 59), 0),
                ((2, 26), 31),
                ((1, 53), 0),
                ((2, 58), 6),
                ((1, 97), 0),
                ((2, 93), 38),
                ((1, 23), 0),
                ((2, 84), 38),
            ]),
        ];
        for (l, q) in cases {
            let mut s = PivotSet::new(30);
            s.insert(0);
            s.insert(l);
            for ((t, x), ans) in q {
                if t == 1 {
                    s.insert(x);
                } else {
                    let i = s.lower_bound(x);
                    dbg!(i);
                    assert_eq!(s.get(i) - s.get(i - 1), ans);
                }
            }
        }
    }
}
