use crate::strongly_connected_components_transpose::transpose;
pub fn scc(g: &[Vec<usize>]) -> Vec<usize> {
    fn dfs(
        g: &[Vec<usize>], visited: &mut [bool], post_order: &mut Vec<usize>,
        u: usize,
    ) {
        visited[u] = true;
        for &v in g[u].iter() {
            if !visited[v] {
                dfs(g, visited, post_order, v);
            }
        }
        post_order.push(u);
    }
    fn rev_dfs(g: &[Vec<usize>], labels: &mut [usize], l: usize, u: usize) {
        labels[u] = l;
        for &v in g[u].iter() {
            if labels[v] == g.len() {
                rev_dfs(g, labels, l, v);
            }
        }
    }
    let n = g.len();
    let mut visited = vec![false; n];
    let mut post_order = Vec::with_capacity(n);
    for i in 0..n {
        if !visited[i] {
            dfs(g, &mut visited, &mut post_order, i);
        }
    }
    let g = transpose(g);
    let mut labels = vec![n; n];
    let mut l = 0;
    for i in post_order.into_iter().rev() {
        if labels[i] == n {
            rev_dfs(&g, &mut labels, l, i);
            l += 1;
        }
    }
    labels
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![(
            (6, vec![(1, 4), (5, 2), (3, 0), (5, 5), (4, 1), (0, 3), (4, 2)]),
            vec![3, 1, 2, 3, 1, 0],
        )];
        for ((n, edges), ans) in cases {
            let mut g = vec![vec![]; n];
            for (u, v) in edges {
                g[u].push(v);
            }
            assert_eq!(scc(&g), ans);
        }
    }
}
