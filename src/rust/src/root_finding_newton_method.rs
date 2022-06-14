#[derive(Default)]
pub struct NewtonMethodOptions {
    absolute_tolerance: Option<f64>,
    relative_tolerance: Option<f64>,
    max_iterations: Option<u8>,
}

impl NewtonMethodOptions {
    pub fn new(
        absolute_tolerance: Option<f64>,
        relative_tolerance: Option<f64>,
        max_iterations: Option<u8>,
    ) -> Self {
        Self {
            absolute_tolerance,
            relative_tolerance,
            max_iterations,
        }
    }
}

/// compute x such that f(x) = 0.
/// f_prime: derivative function.
///
/// example
/// f(x) = x^2 - 10.
/// f_prime(x) = 2x
/// x0 = 1.
/// x = 3.16227...
///
/// Err(x) if not terminated in max iterations.
pub fn newton_method<F, D>(
    f: &F,
    f_prime: &D,
    x0: f64,
    options: Option<NewtonMethodOptions>,
) -> Result<f64, f64>
where
    F: Fn(f64) -> f64,
    D: Fn(f64) -> f64,
{
    const DEFAULT_MAX_ITER: u8 = 1 << 6;
    let options = options.unwrap_or_default();
    let abs_tol = options.absolute_tolerance.unwrap_or_default();
    let rel_tol = options.relative_tolerance.unwrap_or_default();
    let max_iter = options.max_iterations.unwrap_or(DEFAULT_MAX_ITER);
    assert!(0. <= abs_tol);
    assert!(0. <= rel_tol && rel_tol < 1.);

    let mut x = x0;
    for _ in 0..max_iter {
        let diff = f(x) / f_prime(x);
        x -= diff;
        if diff.abs() < abs_tol && (diff / x).abs() < rel_tol {
            return Ok(x);
        }
    }
    Err(x)
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {
        use super::*;
        let n = 51628730198202384.;
        let f = |x: f64| x * x - n;
        let f_prime = |x: f64| 2. * x;
        let x0 = 1.0;
        let x = newton_method(&f, &f_prime, x0, None);
        let x = x.unwrap_err();
        assert_eq!(x as u64, 227219563); // 227219563.854...
    }
}
