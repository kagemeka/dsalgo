pub fn transpose(g: Vec<Vec<usize>>) -> Vec<Vec<usize>> {
    let n = g.len();
    let mut t = vec![vec![]; n];
    for i in 0..n {
        for j in g[i].clone() {
            t[j].push(i);
        }
    }
    t
}
