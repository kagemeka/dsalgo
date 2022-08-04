use std::{cmp::Reverse, collections::BinaryHeap};
pub struct MedianQueue<T> {
    low_que: BinaryHeap<T>,
    high_que: BinaryHeap<Reverse<T>>,
}
impl<T: Clone + Ord> MedianQueue<T> {
    pub fn new() -> Self {
        Self { low_que: BinaryHeap::new(), high_que: BinaryHeap::new() }
    }

    pub fn size(&self) -> usize { self.low_que.len() + self.high_que.len() }

    pub fn peek(&self) -> Option<&T> { self.low_que.peek() }

    fn low_to_high(&mut self) {
        self.high_que.push(Reverse(self.low_que.pop().unwrap()));
    }

    fn high_to_low(&mut self) {
        self.low_que.push(self.high_que.pop().unwrap().0);
    }

    pub fn push(&mut self, x: T) {
        if self.size() & 1 == 1 {
            self.low_que.push(x);
            self.low_to_high()
        } else {
            self.high_que.push(Reverse(x));
            self.high_to_low();
        }
    }

    pub fn pop(&mut self) -> Option<T> {
        let v = self.low_que.pop();
        if self.size() & 1 == 1 {
            self.high_to_low();
        }
        v
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut que = MedianQueue::new();
        for i in 0..5 {
            que.push(i);
        }
        assert_eq!(que.pop(), Some(2));
        assert_eq!(que.pop(), Some(1));
        assert_eq!(que.pop(), Some(3));
        assert_eq!(que.pop(), Some(0));
        assert_eq!(que.pop(), Some(4));
        assert_eq!(que.pop(), None);
    }
}
