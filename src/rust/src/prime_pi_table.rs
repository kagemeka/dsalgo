use crate::sieve_of_eratosthenes::sieve_of_eratosthenes;

pub fn prime_pi_table(size: usize) -> Vec<u32> {
    let mut pi = vec![0; size];
    for p in sieve_of_eratosthenes(size) {
        pi[p as usize] += 1;
    }
    for i in 0..size - 1 {
        pi[i + 1] += pi[i];
    }

    pi
}
