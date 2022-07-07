//! prime sieve algorithms
pub mod erat {
    //! sieve of eratosthenes
    /// prime numbers with sieve size.
    pub fn ps(sz: usize) -> Vec<u32> {
        let mut a = Vec::with_capacity(sz >> 4);
        if sz > 2 {
            a.push(2);
        }
        let mut is_p = vec![true; sz >> 1];
        for i in (3..sz).step_by(2) {
            if !is_p[i >> 1] {
                continue;
            }
            a.push(i as u32);
            for j in (i * i >> 1..sz >> 1).step_by(i) {
                is_p[j] = false;
            }
        }
        a
    }
    #[test]
    fn test_erat() {
        assert_eq!(ps(50), vec![
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
        ],)
    }
    use crate::find_root::isqrt;
    /// range sieve
    pub struct RS {
        ps: Vec<u64>,
        lt: u64, // less than
    }
    impl RS {
        pub fn new(lt: u64) -> Self {
            Self {
                ps: ps(isqrt::floor(lt) as usize + 1)
                    .into_iter()
                    .map(|p| p as u64)
                    .collect(),
                lt,
            }
        }

        /// find prime numbers in [lo, hi).
        /// time: O((hi - lo)\log{\log{less_than}})
        /// space: O(hi - lo)
        pub fn ps(&self, mut l: u64, h: u64) -> Vec<u64> {
            assert!(l <= h && h <= self.lt);
            if h <= 2 {
                return vec![];
            }
            if l < 2 {
                l = 2;
            }
            debug_assert!(2 <= l && l < h);
            let mut a = vec![];
            if l & 1 == 0 {
                if l == 2 {
                    a.push(2);
                }
                l += 1;
            }
            if l == h {
                return a;
            }
            // initially, only odd numbers are in sieve.
            // be careful of indices.
            let sz = ((h - l + 1) >> 1) as usize;
            let mut is_p = vec![true; sz];
            for &p in self.ps.iter().skip(1) {
                let mut from = p * p;
                if from >= h {
                    break;
                }
                from = from.max((l + p - 1) / p * p);
                if from & 1 == 0 {
                    from += p;
                }
                debug_assert!(from & 1 == 1);
                for j in (((from - l) >> 1) as usize..sz).step_by(p as usize) {
                    is_p[j] = false;
                }
            }
            a.extend(is_p.into_iter().enumerate().filter_map(|(i, is_p)| {
                if is_p { Some(l + (i << 1) as u64) } else { None }
            }));
            a
        }
    }
    #[test]
    fn test_rs() {
        let gen = RS::new(1 << 10);
        assert_eq!(gen.ps(100, 500), vec![
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
            167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
            239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
            313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
            397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
            467, 479, 487, 491, 499,
        ],);
    }
    /// Low Memory Genrator
    pub struct LMG {
        it: std::vec::IntoIter<u64>,
        rs: RS,
        ranges: std::vec::IntoIter<(u64, u64)>,
    }
    impl LMG {
        /// [lo, hi)
        pub fn new(mut lo: u64, mut hi: u64) -> Self {
            if lo < 2 {
                lo = 2;
            }
            if hi < 2 {
                hi = 2;
            }
            let mut ranges = vec![];
            let sz = (isqrt::floor(hi) as usize) << 3; // 2 ~ 4
            // because range sieve has only odd numbers internally,
            // the size is sqrt / 2.
            // so we can check more than twice the range at once.
            // four times is best in test.
            for i in (lo..hi).step_by(sz) {
                ranges.push((i, hi.min(i + sz as u64)));
            }
            Self {
                it: vec![].into_iter(),
                rs: RS::new(hi as u64),
                ranges: ranges.into_iter(),
            }
        }
    }
    impl Iterator for LMG {
        type Item = u64;

        fn next(&mut self) -> Option<Self::Item> {
            if let Some(p) = self.it.next() {
                return Some(p);
            }
            while let Some((lo, hi)) = self.ranges.next() {
                self.it = self.rs.ps(lo, hi).into_iter();
                if let Some(p) = self.it.next() {
                    return Some(p);
                }
            }
            None
        }
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test() {
            let mut it = LMG::new(20, 30);
            assert_eq!(it.next(), Some(23));
            assert_eq!(it.next(), Some(29));
            assert_eq!(it.next(), None);
        }
    }
}
pub mod linear {
    /// compute least prime factor table and prime numbers list.
    pub fn ps(size: usize) -> (Vec<Option<u32>>, Vec<u32>) {
        let mut lpf = vec![None; size];
        let mut a = Vec::with_capacity(size >> 4);
        for i in 2..size {
            if lpf[i].is_none() {
                lpf[i] = Some(i as u32);
                a.push(i as u32);
            }
            for &p in &a {
                if p > lpf[i].unwrap() || p as usize * i >= size {
                    break;
                }
                debug_assert!(lpf[p as usize * i].is_none());
                lpf[p as usize * i] = Some(p);
            }
        }
        (lpf, a)
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test() {
            use crate::{
                least_prime_factor_table::least_prime_factor_table,
                psieve::erat,
            };
            const K: usize = 1 << 10;
            let lpf_ans = least_prime_factor_table(K);
            let p_ans = erat::ps(K);
            assert_eq!((lpf_ans, p_ans), ps(K));
        }
    }
}
pub mod atkin {
    //! sieve of atkin
}
pub mod erat_lndr {
    //! eratosthenes and legendre sieve.
}
pub mod euler {
    //! sieve of euler
}
pub mod sunda {
    //! sieve of sundaram
    /// prime numbers less than
    pub fn ps(lt: u32) -> Vec<u32> {
        let mut a = vec![];
        if lt <= 2 {
            return a;
        }
        a.push(2);
        let n = (lt >> 1) as usize;
        let mut is_p = vec![true; n];
        for i in 1..n {
            if is_p[i] {
                a.push(((i as u32) << 1) | 1);
            }
            for j in (i * (i + 1) << 1..n).step_by((i << 1) | 1) {
                is_p[j] = false;
            }
        }
        a
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test() {
            use crate::psieve::erat;
            let lim = [99, 100, 101, 102, 1 << 17];
            for l in lim {
                assert_eq!(ps(l), erat::ps(l as usize),);
            }
        }
    }
}
