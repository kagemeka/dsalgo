use crate::next_combination_bits::next_combination;
pub fn combinations(n: usize, k: usize) -> Vec<usize> {
    assert!(k <= n);
    if k == 0 {
        return vec![0];
    }
    let offset = (std::mem::size_of::<usize>() << 3) - n;
    let mut res = vec![];
    let mut s: usize = (1 << k) - 1;
    let lim = 1 << n;
    while s < lim {
        res.push(s.reverse_bits() >> offset);
        s = next_combination(s);
    }
    res.reverse();
    res
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        dbg!(std::mem::size_of::<usize>());
        for s in combinations(8, 4) {
            println!("{:08b}", s);
        }
    }
}
