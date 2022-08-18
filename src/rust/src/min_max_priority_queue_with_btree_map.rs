use std::collections::BTreeMap;
pub struct MinMaxQueue<T>(BTreeMap<T, usize>);
impl<T: Ord> MinMaxQueue<T> {
    pub fn new() -> Self { Self(BTreeMap::new()) }

    pub fn count(&self, x: &T) -> usize {
        *self.0.get(x).or_else(|| Some(&0)).unwrap()
    }

    pub fn insert(&mut self, x: T, count: usize) {
        *self.0.entry(x).or_insert(0) += count;
    }

    pub fn remove(&mut self, x: &T, count: usize) {
        let c = self.0.get_mut(x).unwrap();
        *c -= count;
        if *c == 0 {
            self.0.remove(x);
        }
    }

    pub fn min(&mut self) -> Option<&T> {
        if let Some((x, _)) = self.0.first_key_value() {
            Some(x)
        } else {
            None
        }
    }

    pub fn max(&mut self) -> Option<&T> {
        if let Some((x, _)) = self.0.last_key_value() {
            Some(x)
        } else {
            None
        }
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut que = MinMaxQueue::new();
        que.insert(1, 5);
        assert_eq!(que.min(), Some(&1));
        que.insert(-1, 1);
        assert_eq!(que.min(), Some(&-1));
        assert_eq!(que.max(), Some(&1));
        que.remove(&1, 1);
        que.remove(&1, 3);
        que.remove(&-1, 1);
    }
}
