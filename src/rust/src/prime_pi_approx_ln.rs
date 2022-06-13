use crate::bit_length::bit_length_128;

/// mainly used for initializing prime_numbers vec with capacity.
pub fn prime_pi_approx_ln(n: u128) -> u128 {
    if n < 2 {
        return 0;
    }
    return n * 3 / bit_length_128(n) as u128 >> 1;
    // suppose pi(x) ~= [x / ln(x)] * 1.1
    // = [x / log_2(x) * (log_2(x) / ln(x))] * 1.1
    // = [x / log_2(x) * ln(2)^{-1}] * 1.1
    // ~= [x / log_2(x) * 1.4427] * 1.1
    // ~= x * 3 / log_2(x) / 2
}
