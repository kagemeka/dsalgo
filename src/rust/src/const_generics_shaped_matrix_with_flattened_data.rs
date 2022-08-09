#[derive(Debug, Clone, Copy)]
pub struct Matrix<T, const H: usize, const W: usize>([T; H * W])
where
    [(); H * W]:;
impl<T, const H: usize, const W: usize> Matrix<T, H, W>
where
    [(); H * W]:,
    T: Default + Copy,
{
    type A = [T; H * W];

    pub fn new() -> Self { Self([T::default(); H * W]) }
}
use std::ops::*;
impl<T, const H: usize, const W: usize> Index<(usize, usize)>
    for Matrix<T, H, W>
where
    [(); H * W]:,
{
    type Output = T;

    fn index(&self, index: (usize, usize)) -> &Self::Output {
        &self.0[index.0 * W + index.1]
    }
}
impl<T, const H: usize, const W: usize> IndexMut<(usize, usize)>
    for Matrix<T, H, W>
where
    [(); H * W]:,
{
    fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
        &mut self.0[index.0 * W + index.1]
    }
}
use std::convert::Into;
impl<T, const H: usize, const W: usize> Into<[[T; W]; H]> for Matrix<T, H, W>
where
    [(); H * W]:,
    T: Copy + Default,
{
    fn into(self) -> [[T; W]; H] {
        let mut res = [[T::default(); W]; H];
        for i in 0..H {
            res[i].clone_from_slice(&self.0[i * W..(i + 1) * W]);
        }
        res
    }
}
impl<T, const H: usize, const W: usize> std::fmt::Display for Matrix<T, H, W>
where
    [(); H * W]:,
    T: std::fmt::Debug + Copy + Default,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let format_str = <Self as Into<[[T; W]; H]>>::into(*self)
            .iter()
            .map(|row| format!("{:?}", row))
            .collect::<Vec<_>>()
            .join("\n");
        write!(f, "{}", format_str)
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        type Mat = Matrix<i64, 4, 3>;
        let mut a = Mat::new();
        a[(1, 1)] += 1;
        println!("{:?}", a);
        println!("{}", a);
    }
}
