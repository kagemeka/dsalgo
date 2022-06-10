use crate::power_monoid::pow_monoid;

pub fn modular_pow(modulus: u32, base: u64, exponent: u64) -> u32 {
    let modulus = modulus as u64;
    pow_monoid(
        &|x, y| x * y % modulus,
        &|| 1,
        base % modulus,
        exponent,
    ) as u32
}

pub fn modular_pow_64(modulus: u64, base: u128, exponent: u64) -> u64 {
    let modulus = modulus as u128;
    pow_monoid(
        &|x, y| x * y % modulus,
        &|| 1,
        base % modulus,
        exponent,
    ) as u64
}

// TODO:
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
