use std::collections::{BinaryHeap, HashMap};
pub struct LazyBinaryHeap<T> {
    que: BinaryHeap<T>,
    cnt: HashMap<T, isize>,
}
impl<T: Ord + std::hash::Hash + Clone> LazyBinaryHeap<T> {
    pub fn new() -> Self {
        Self { que: BinaryHeap::new(), cnt: HashMap::new() }
    }

    pub fn count(&self, x: &T) -> isize {
        *self.cnt.get(&x).or_else(|| Some(&0)).unwrap()
    }

    pub fn contains(&self, x: &T) -> bool { self.count(x) > 0 }

    pub fn add(&mut self, x: T, delta: isize) {
        let c = self.cnt.entry(x.clone()).or_insert(0);
        if *c <= 0 && *c + delta > 0 {
            self.que.push(x);
        }
        *c += delta;
    }

    fn lazy_discard_false_peek(&mut self) {
        while let Some(x) = self.que.peek() {
            if self.count(x) <= 0 {
                self.que.pop();
                continue;
            }
            break;
        }
    }

    pub fn peek(&mut self) -> Option<&T> {
        self.lazy_discard_false_peek();
        self.que.peek()
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut que = LazyBinaryHeap::new();
        que.add(1, 5);
        assert_eq!(que.peek(), Some(&1));
        que.add(2, 1);
        assert_eq!(que.peek(), Some(&2));
        que.add(1, -6);
        assert_eq!(que.count(&1), -1);
        que.add(1, 1);
        que.add(2, -1);
        assert_eq!(que.peek(), None);
    }
}
