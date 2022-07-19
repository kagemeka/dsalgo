//! prime sieve algorithms
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
                least_prime_factor_table_with_sieve_of_eratosthenes::*,
                sieve_of_eratosthenes_enumerate_primes::enumerate_primes,
            };
            const K: usize = 1 << 10;
            let lpf_ans = least_prime_factor_table(K);
            let p_ans = enumerate_primes(K as u32);
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
            use crate::sieve_of_eratosthenes_enumerate_primes::*;
            let lim = [99, 100, 101, 102, 1 << 17];
            for l in lim {
                assert_eq!(ps(l), enumerate_primes(l),);
            }
        }
    }
}
