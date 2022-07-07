use crate::{union_find::*, union_find_trait::*};
pub fn connected_components_uf(
    v_size: usize, undirected_edges: &[(usize, usize)],
) -> Vec<usize> {
    let mut uf = UnionFind::new(v_size);
    for &(u, v) in undirected_edges {
        uf.unite(u, v);
    }
    uf.labels()
}
// TODO
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
