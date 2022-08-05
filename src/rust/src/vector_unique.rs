pub fn unique<T: Ord>(mut a: Vec<T>) -> Vec<T> {
    a.sort();
    a.dedup();
    a
}
// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
