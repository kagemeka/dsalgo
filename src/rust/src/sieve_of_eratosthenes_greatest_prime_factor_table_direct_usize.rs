pub fn greatest_prime_factor(size: usize) -> Vec<usize> {
    let mut gpf: Vec<usize> = (0..size).collect();
    for i in 2..size {
        if gpf[i] != i {
            continue;
        }
        for j in (i * 2..size).step_by(i) {
            gpf[j] = i;
        }
    }
    gpf
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        assert_eq!(greatest_prime_factor(20), [
            0, 1, 2, 3, 2, 5, 3, 7, 2, 3, 5, 11, 3, 13, 7, 5, 2, 17, 3, 19
        ]);
    }
}
