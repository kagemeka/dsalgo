type G<T> = Vec<Vec<T>>;
pub fn floyd_warshall<T, F, H>(adj_mat: G<T>, f: &F, cb: &mut H) -> G<T>
where
    T: Clone,
    F: Fn(T, T, T) -> T,
    H: FnMut(&G<T>),
{
    let mut g = adj_mat;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = f(g[i][j].clone(), g[i][k].clone(), g[k][j].clone());
            }
        }
        cb(&g);
    }
    g
}
