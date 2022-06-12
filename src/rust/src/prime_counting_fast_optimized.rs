use crate::floor_sqrt::floor_sqrt;

/// Compute \pi(n)
/// reference
/// - https://judge.yosupo.jp/submission/61553
pub fn prime_pi_fast_optimized(n: u64) -> u64 {
    if n < 2 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    let sqrt = floor_sqrt(n) as usize;
    let n = n as usize;
    let mut size = (sqrt + 1) >> 1;
    let mut small: Vec<usize> = (0..size).collect();
    let mut rough: Vec<usize> = (0..size).map(|i| i << 1 | 1).collect();
    let mut large: Vec<usize> =
        (0..size).map(|i| (n / (i << 1 | 1) - 1) >> 1).collect();
    let mut skip = vec![false; sqrt + 1];
    let half = |i: usize| (i - 1) >> 1;
    let mut pi = 0;
    for i in (3..=sqrt).step_by(2) {
        if skip[i] {
            continue;
        }
        let i2 = i * i;
        if i2 * i2 > n {
            break;
        }
        skip[i] = true;
        for j in (i2..=sqrt).step_by(i << 1) {
            skip[j] = true;
        }
        let mut next_k = 0;
        for k in 0..size {
            let j = rough[k];
            if skip[j] {
                continue;
            }
            let border = j * i;
            large[next_k] = large[k]
                - if border <= sqrt {
                    large[small[border >> 1] - pi]
                } else {
                    small[half(n / border)]
                }
                + pi;
            rough[next_k] = j;
            next_k += 1;
        }
        size = next_k;
        let mut j = half(sqrt);
        let mut k = sqrt / i - 1 | 1;
        while k >= i {
            let c = small[k >> 1] - pi;
            let e = k * i >> 1;
            while j >= e {
                small[j] -= c;
                j -= 1;
            }
            k -= 2;
        }
        pi += 1;
    }
    large[0] += if pi > 0 {
        size + ((pi - 1) << 1)
    } else {
        // -1 << 1 == -2
        size.saturating_sub(2)
        // if size == 1,
        // (size + ((pi - 1) << 1)) * (size - 1) >> 1 == 0
        // regardless of `size + ((pi - 1) << 1)`
    } * (size - 1)
        >> 1;
    for k in 1..size {
        large[0] -= large[k];
    }
    for k in 1..size {
        let q = rough[k];
        let n_q = n / q;
        let e = small[half(n_q / q)] - pi;
        if e < k + 1 {
            break;
        }
        let mut t = 0;
        for l in k + 1..=e {
            t += small[half(n_q / rough[l])];
        }
        large[0] += t - (e - k) * (pi + k - 1);
    }

    large[0] as u64 + 1
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::*;
        use crate::test_fast_prime_counting::test_fast_prime_counting;
        test_fast_prime_counting(&prime_pi_fast_optimized);
    }
}
