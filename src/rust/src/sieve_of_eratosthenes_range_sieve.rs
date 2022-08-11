use crate::{
    find_root::isqrt, sieve_of_eratosthenes_enumerate_primes_u32::enumerate_primes,
};
pub struct RangeSieve {
    primes: Vec<u64>,
    less_than: u64,
}
impl RangeSieve {
    pub fn new(less_than: u64) -> Self {
        Self {
            primes: enumerate_primes(isqrt::floor(less_than) as u32 + 1)
                .into_iter()
                .map(|p| p as u64)
                .collect(),
            less_than,
        }
    }

    /// find prime numbers in [lo, hi).
    /// time: O((hi - lo)\log{\log{less_than}})
    /// space: O(hi - lo)
    pub fn ps(&self, mut lo: u64, hi: u64) -> Vec<u64> {
        assert!(lo <= hi && hi <= self.less_than);
        if hi <= 2 {
            return vec![];
        }
        if lo < 2 {
            lo = 2;
        }
        debug_assert!(2 <= lo && lo < hi);
        let mut a = vec![];
        if lo & 1 == 0 {
            if lo == 2 {
                a.push(2);
            }
            lo += 1;
        }
        if lo == hi {
            return a;
        }
        // initially, only odd numbers are in sieve.
        // be careful of indices.
        let sz = ((hi - lo + 1) >> 1) as usize;
        let mut is_p = vec![true; sz];
        for &p in self.primes.iter().skip(1) {
            let mut from = p * p;
            if from >= hi {
                break;
            }
            from = from.max((lo + p - 1) / p * p);
            if from & 1 == 0 {
                from += p;
            }
            debug_assert!(from & 1 == 1);
            for j in (((from - lo) >> 1) as usize..sz).step_by(p as usize) {
                is_p[j] = false;
            }
        }
        a.extend(is_p.into_iter().enumerate().filter_map(|(i, is_p)| {
            if is_p { Some(lo + (i << 1) as u64) } else { None }
        }));
        a
    }
}
#[test]
fn test_rs() {
    let gen = RangeSieve::new(1 << 10);
    assert_eq!(gen.ps(100, 500), vec![
        101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
        173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
        251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
        337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    ],);
}
