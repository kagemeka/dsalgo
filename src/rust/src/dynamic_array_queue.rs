pub struct Queue<T> {
    data: Vec<T>,
    buf_size: usize,
    idx: usize,
}
impl<T: Clone> Queue<T> {
    pub fn new(buf_size: usize) -> Self {
        Self { data: vec![], buf_size, idx: 0 }
    }

    pub fn size(&self) -> usize { self.data.len() - self.idx }

    pub fn is_full(&self) -> bool { self.size() == self.buf_size }

    pub fn reform(&mut self) {
        self.data = self.data[self.idx..].to_vec();
        self.idx = 0;
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.size() == 0 {
            return None;
        }
        let v = self.data[self.idx].clone();
        self.idx += 1;
        Some(v)
    }

    pub fn push(&mut self, x: T) {
        assert!(!self.is_full());
        self.data.push(x);
        if self.data.len() == self.buf_size {
            self.reform();
        }
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut que = Queue::new(10);
        que.push(2);
        que.push(1);
        assert_eq!(que.pop(), Some(2));
        que.push(3);
        assert_eq!(que.pop(), Some(1));
        assert_eq!(que.pop(), Some(3));
        assert_eq!(que.pop(), None);
    }
}
