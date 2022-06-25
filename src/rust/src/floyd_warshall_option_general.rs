type Mat<T> = Vec<Vec<Option<T>>>;

pub fn floyd_warshall<T>(adj_mat: Mat<T>) -> Mat<T>
where
    T: Copy + std::ops::Add<Output = T> + Ord,
{
    let mut g = adj_mat;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            if g[i][k].is_none() {
                continue;
            }
            let d0 = g[i][k].unwrap();
            for j in 0..n {
                if g[k][j].is_none() {
                    continue;
                }
                let d = d0 + g[k][j].unwrap();
                if g[i][j].is_none() || Some(d) < g[i][j] {
                    g[i][j] = Some(d);
                }
            }
        }
    }
    g
}
