type Mat<T> = Vec<Vec<T>>;

pub fn floyd_warshall<T>(mut g: Mat<T>) -> Mat<T>
where
    T: Ord + std::ops::Add<Output = T> + Copy,
{
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = g[i][j].min(g[i][k] + g[k][j]);
            }
        }
    }
    g
}

#[cfg(test)]
mod tests {
    use super::*;
}
