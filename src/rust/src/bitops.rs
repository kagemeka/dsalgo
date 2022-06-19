/// count leading zeros
/// why L is asccociated variable rather than fixed u8?
/// > due to big integer.
pub trait CLZ {
    type L;

    fn clz(self) -> Self::L;
}

/// count trailing zeros
pub trait CTZ {
    type L;

    fn ctz(self) -> Self::L;
}

/// this is not usually abbreviated as CLO unlike CLZ.
pub trait CountLeadingOnes {
    type L;

    fn leading_ones(self) -> Self::L;
}

pub trait CountTrailingOnes {
    type L;

    fn trailing_ones(self) -> Self::L;
}

pub trait CountZeros {
    type L;

    fn count_zeros(self) -> Self::L;
}

pub trait CountOnes {
    type L;

    fn count_ones(self) -> Self::L;
}

/// bit scan reverse
pub trait BSR {
    type L;

    fn bsr(self) -> Self::L;
}

/// bit scan forward
pub trait BSF {
    type L;

    fn bsf(self) -> Self::L;
}

pub mod len {
    /// O(1)
    pub fn with_clz(n: u64) -> u8 {
        (0u64.leading_zeros() - n.leading_zeros()) as u8
    }

    pub fn with_clz_128(n: u128) -> u8 {
        (0u128.leading_zeros() - n.leading_zeros()) as u8
    }

    /// O(\log\log{N}})
    pub fn binary_search(mut n: u64) -> u8 {
        let mut l = 0;
        for i in (0..6).rev() {
            let d = 1 << i;
            if n >> d > 0 {
                n >>= d;
                l += d;
            }
        }
        if n == 1 {
            l += 1;
            n -= 1;
        }
        debug_assert_eq!(n, 0);
        l
    }

    /// O(\log{N})
    pub fn naive(mut n: u64) -> u8 {
        let mut l = 0;
        while n > 0 {
            n >>= 1;
            l += 1;
        }
        l
    }

    /// O(N)
    pub fn table(size: usize) -> Vec<u8> {
        let mut l = vec![0; size];
        for i in 1..size {
            l[i] = l[i >> 1] + 1;
        }
        l
    }
}

/// just alias of count_ones.
pub trait Popcount: CountOnes {}

impl<T: CountOnes> Popcount for T {}

pub mod popcount {
    /// O(1)
    pub fn with_std(n: u64) -> u8 { n.count_ones() as u8 }

    /// O(\log\log{N})
    pub fn divide_conquer(mut n: u64) -> u8 {
        const M0: u64 = 0x5555555555555555; // 0b0101...
        const M1: u64 = 0x3333333333333333; // 0b0011...
        const M2: u64 = 0x0f0f0f0f0f0f0f0f; // 0b00001111...
        n -= (n >> 1) & M0;
        // = (n & M0) + ((n >> 1) & M0);
        n = (n & M1) + ((n >> 2) & M1);
        n = (n + (n >> 4)) & M2;
        // = (n & M2) + ((n >> 4) & M2)
        // k = 4, 2k < 2^k
        n += n >> 8;
        // it's only enough to mask at last.
        // popcount <= 64 = 7bits < 8.
        n += n >> 16;
        n += n >> 32;
        return (n & 0x7f) as u8;
    }

    /// O(\log{N})
    pub fn naive(mut n: u64) -> u8 {
        let mut c = 0;
        while n > 0 {
            c += (n & 1) as u8;
            n >>= 1
        }
        c
    }

    /// O(N)
    pub fn table(size: usize) -> Vec<u8> {
        let mut count = vec![0; size];
        for i in 1..size {
            count[i] = count[i >> 1] + (i & 1) as u8;
        }
        count
    }

    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {}
    }
}

pub trait Inverse {
    fn invert(self) -> Self;
}

/// equivalent to (2^k - 1) ^ n for k bit integer.
pub fn invert<T: std::ops::Not<Output = T>>(n: T) -> T { !n }

pub trait Reverse {
    fn reverse(self) -> Self;
}

/// TODO: not implemented.
pub fn reverse() {}

pub trait ShrUntilOdd {
    fn shr_until_odd(self) -> Self;
}

/// shift right
pub fn shr_until_odd(n: u64) -> u64 {
    assert!(n > 0);
    n >> n.trailing_zeros()
}

/// most significant bit
/// O(1)
pub fn msb(n: u64) -> usize {
    assert!(n > 0);
    crate::bitops::len::with_clz(n) as usize - 1
}

pub fn msb_number(n: u64) -> u64 { if n == 0 { 0 } else { 1 << msb(n) } }

/// O(\log\log{N})
pub fn msb_number_binary_search(mut n: u64) -> u64 {
    const MASKS: [u64; 6] = [
        0xffffffff00000000,
        0xffff0000ffff0000,
        0xff00ff00ff00ff00,
        0xf0f0f0f0f0f0f0f0,
        0xcccccccccccccccc, // 0b1100...
        0xaaaaaaaaaaaaaaaa, // 0b1010...
    ];
    // TODO: change later. not compile on AtCoder.
    // for m in MASKS {
    for m in MASKS.iter() {
        if n & m > 0 {
            n &= m;
        }
    }
    n
}

/// least significant bit
pub fn lsb(n: u64) -> usize {
    assert!(n > 0);
    n.trailing_zeros() as usize
}

pub fn lsb_number_i64(n: i64) -> i64 { n & -n }

pub fn lsb_number(n: u64) -> u64 {
    match n {
        0 => 0,
        n => 1 << lsb(n),
    }
}

/// rotate left
/// can be called safely only in release mode.
pub fn rot_l(x: u64, k: u8) -> u64 { (x << k) | (x >> (64 - k)) }

pub fn reset(n: u64, i: usize) -> u64 { n & !(1 << i) }

pub fn reset_lsb(n: u64) -> u64 { if n == 0 { 0 } else { n & (n - 1) } }

pub fn flip(n: u64, i: usize) -> u64 { n ^ (1 << i) }

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_shr_until_odd() {
        assert_eq!(shr_until_odd(1), 1);
        assert_eq!(shr_until_odd(2), 1);
        assert_eq!(shr_until_odd(12), 3);
    }

    #[test]
    fn test_lsb() {
        assert_eq!(lsb(1), 0,);
    }

    #[test]
    fn test_lsb_number() {
        assert_eq!(lsb_number_i64(0), 0);
        assert_eq!(lsb_number_i64(1), 1);
        assert_eq!(lsb_number_i64(2), 2);
        assert_eq!(lsb_number_i64(3), 1);

        assert_eq!(lsb_number(0), 0);
        assert_eq!(lsb_number(1), 1);
        assert_eq!(lsb_number(2), 2);
        assert_eq!(lsb_number(3), 1);
    }

    #[test]
    fn test_reset_least_bit() {
        assert_eq!(reset_lsb(0), 0);
        assert_eq!(reset_lsb(16), 0);
        assert_eq!(reset_lsb(3), 2);
    }
}
