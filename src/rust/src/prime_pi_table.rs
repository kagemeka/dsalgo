use crate::psieve::erat;

/// prime pi table
pub fn pi_t(sz: usize) -> Vec<u32> {
    let mut pi = vec![0; sz];
    for p in erat::ps(sz) {
        pi[p as usize] = 1;
    }
    for i in 0..sz - 1 {
        pi[i + 1] += pi[i];
    }

    pi
}
