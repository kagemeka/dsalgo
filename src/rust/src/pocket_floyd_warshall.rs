type G<T> = Vec<Vec<T>>;

pub fn floyd_warshall<T>(adjacency_matrix: G<T>, inf: T) -> G<T>
where
    T: std::ops::Add<Output = T> + Copy + PartialEq + Ord,
{
    let mut g = adjacency_matrix;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if g[i][k] != inf && g[k][j] != inf {
                    g[i][j] = g[i][j].min(g[i][k] + g[k][j]);
                }
            }
        }
    }
    g
}
