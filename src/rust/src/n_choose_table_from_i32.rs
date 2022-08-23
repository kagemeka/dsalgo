use std::ops::*;

use crate::inverse_factorial_table_from_i32::inverse_factorial;
pub fn n_choose<T>(n: usize, size: usize) -> Vec<T>
where
    T: Mul<Output = T> + Div<Output = T> + From<i32> + Clone,
{
    let mut f = inverse_factorial::<T>(size);
    for i in 1..size {
        f[i] = f[i].clone() * ((n + 1 - i) as i32).into();
    }
    f
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        use crate::{
            define_const_modulus_macro::Mod1_000_000_007I64,
            modular_int_with_static_modulus::Modint,
        };
        type Mint = Modint<Mod1_000_000_007I64>;
        let res = n_choose::<Mint>(1_000_000_007, 20)
            .into_iter()
            .map(|x| x.0)
            .collect::<Vec<i64>>();
        assert_eq!(res, [
            1, 0, 500000003, 666666671, 875000006, 766666672, 493055559,
            598809528, 587326393, 344422401, 451247523, 288004802, 809733779,
            109907730, 829933342, 500610602, 917451609, 775212655, 125620192,
            762418468,
        ]);
    }
}
