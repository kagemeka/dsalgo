use crate::{choose::Choose, combination::Combination};

impl<T> Choose<T> for Combination<T>
where
    T: std::ops::Mul<Output = T> + From<u64> + Clone,
{
    fn choose(&mut self, n: u64, k: u64) -> T {
        self.calc(n as usize, k as usize)
    }
}
