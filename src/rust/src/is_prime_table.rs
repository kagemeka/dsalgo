use crate::psieve::erat;
/// is prime table
pub fn is_p_t(sz: usize) -> Vec<bool> {
    let mut is_prime = vec![false; sz];
    for p in erat::ps(sz) {
        is_prime[p as usize] = true;
    }
    is_prime
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let is_prime = is_p_t(20);
        assert_eq!(is_prime, vec![
            false, false, true, true, false, true, false, true, false, false,
            false, true, false, true, false, false, false, true, false, true
        ],);
    }
}
