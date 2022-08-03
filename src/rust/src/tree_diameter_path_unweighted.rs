use crate::tree_bfs_parent_depth::bfs;
pub fn diameter_path(g: &[Vec<usize>]) -> Vec<usize> {
    let n = g.len();
    let argmax = |dep: &[usize], root| {
        let mut v = root;
        let mut mx = 0;
        for i in 0..n {
            if dep[i] <= mx {
                continue;
            }
            mx = dep[i];
            v = i;
        }
        v
    };
    let (_, dep) = bfs(&g, 0);
    let u = argmax(&dep, 0);
    let (parent, dep) = bfs(&g, u);
    let mut v = argmax(&dep, u);
    let mut path = vec![v];
    for _ in 0..dep[v] {
        v = parent[v];
        path.push(v);
    }
    path
}
