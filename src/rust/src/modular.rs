pub mod inv {
    //! well-known modular inverse algorithms.
    /// inverse by Fermat's Little Theorem.
    /// for prime modulus.
    pub fn fermat() {
        // TODO:
    }
    /// inverse by Euler's Theorem.
    pub fn euler() {
        // TODO:
        // check gcd
        // return error if gcd != 1
        // or compute inverse with totient function.
        // related: carmichael_function.rs
    }
    use crate::extended_euclidean_modular_gcd_inverse_u64_direct::mod_gcd_inv;
    /// inverse by Extended Euclidean Algorithm.
    pub fn extgcd(modulus: u64, element: u64) -> Result<u64, &'static str> {
        let (gcd, inv) = mod_gcd_inv(modulus, element);
        if gcd == 1 {
            Ok(inv)
        } else {
            Err("modulus and element are not coprime")
        }
    }
}
