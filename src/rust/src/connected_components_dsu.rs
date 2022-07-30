use crate::{union_find_low_memory_with_trait::*, union_find_traits::*};
pub fn connected_components(
    v_size: usize, edges: &[(usize, usize)],
) -> Vec<usize> {
    let mut uf = UnionFind::new(v_size);
    for &(u, v) in edges {
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
