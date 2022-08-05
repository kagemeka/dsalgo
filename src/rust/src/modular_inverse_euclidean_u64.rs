use crate::extended_euclidean_modular_gcd_inverse_u64_direct::mod_gcd_inv;
/// inverse by Extended Euclidean Algorithm.
pub fn modinv(modulus: u64, element: u64) -> Result<u64, &'static str> {
    let (gcd, inv) = mod_gcd_inv(modulus, element);
    if gcd == 1 {
        Ok(inv)
    } else {
        Err("modulus and element are not coprime")
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        const MOD: u64 = 1_000_000_007;
        const INV: u64 = (MOD + 1) >> 1;
        assert_eq!(modinv(MOD, 2), Ok(INV));
    }
}
