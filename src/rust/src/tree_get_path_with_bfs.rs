use crate::tree_bfs_parent::*;
pub fn tree_path(g: &[Vec<usize>], mut u: usize, v: usize) -> Vec<usize> {
    let p = tree_bfs_parent(&g, v);
    let mut path = Vec::new();
    loop {
        path.push(u);
        if u == v {
            break;
        }
        u = p[u];
    }
    path
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let g = vec![vec![1], vec![0, 2, 3], vec![1], vec![1, 4], vec![3]];
        assert_eq!(tree_path(&g, 4, 2), [4, 3, 1, 2]);
    }
}
