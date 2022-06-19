//! lowest common ancestor

pub mod tree {

    use crate::{
        bitops::len::with_clz as bit_length,
        tree_depths::tree_depths,
        tree_parents::tree_parents,
    };

    pub struct LCABinaryLifting {
        ancestors: Vec<Vec<usize>>,
        depth: Vec<usize>,
    }

    impl LCABinaryLifting {
        pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self {
            let n = tree_edges.len() + 1;
            let depth = tree_depths(&tree_edges, root);
            let k = std::cmp::max(
                1,
                bit_length(*depth.iter().max().unwrap() as u64),
            ) as usize;
            let mut ancestors = vec![vec![n; n]; k];
            let mut parent = tree_parents(&tree_edges, root);
            parent[root] = Some(root);
            ancestors[0] = parent.iter().map(|&v| v.unwrap()).collect();
            for i in 0..k - 1 {
                for j in 0..n {
                    ancestors[i + 1][j] = ancestors[i][ancestors[i][j]];
                }
            }
            Self { ancestors, depth }
        }

        pub fn get(&self, mut u: usize, mut v: usize) -> usize {
            if self.depth[u] > self.depth[v] {
                std::mem::swap(&mut u, &mut v);
            }
            let d = self.depth[v] - self.depth[u];
            for i in 0..bit_length(d as u64) as usize {
                if d >> i & 1 == 1 {
                    v = self.ancestors[i][v];
                }
            }
            if v == u {
                return u;
            }
            for a in self.ancestors.iter().rev() {
                let nu = a[u];
                let nv = a[v];
                if nu != nv {
                    u = nu;
                    v = nv;
                }
            }
            self.ancestors[0][u]
        }
    }

    use crate::{tree_edges_to_graph::tree_edges_to_graph, uf::*};

    pub fn offline_tarjan(
        tree_edges: &[(usize, usize)],
        queries: &[(usize, usize)],
        root: usize,
    ) -> Vec<usize> {
        fn dfs(
            g: &Vec<Vec<usize>>,
            q: &Vec<Vec<(usize, usize)>>,
            visited: &mut Vec<bool>,
            uf: &mut UF,
            ancestor: &mut Vec<usize>,
            lca: &mut Vec<usize>,
            u: usize,
        ) {
            visited[u] = true;
            ancestor[u] = u;
            for &v in g[u].iter() {
                if visited[v] {
                    continue;
                }
                dfs(
                    g, q, visited, uf, ancestor, lca, v,
                );
                uf.unite(u, v);
                ancestor[uf.root(u)] = u;
            }
            q[u].iter().filter(|&&(v, _)| visited[v]).for_each(|&(v, i)| {
                lca[i] = ancestor[uf.root(v)];
            });
        }
        let n = tree_edges.len() + 1;
        let graph = tree_edges_to_graph(tree_edges);
        let mut q = vec![vec![]; n];
        for (i, &(u, v)) in queries.iter().enumerate() {
            q[u].push((v, i));
            q[v].push((u, i));
        }
        let mut visited = vec![false; n];
        let mut uf = UF::new(n);
        let mut ancestor = vec![n; n];
        let mut lca = vec![n; queries.len()];
        dfs(
            &graph,
            &q,
            &mut visited,
            &mut uf,
            &mut ancestor,
            &mut lca,
            root,
        );
        lca
    }

    use crate::heavy_light_decomposition::heavy_light_decompose;

    pub struct LCAHLD {
        parent: Vec<Option<usize>>,
        depth: Vec<usize>,
        roots: Vec<usize>,
    }

    impl LCAHLD {
        pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self {
            Self {
                parent: tree_parents(tree_edges, root),
                depth: tree_depths(tree_edges, root),
                roots: heavy_light_decompose(tree_edges, root),
            }
        }

        pub fn get(&self, mut u: usize, mut v: usize) -> usize {
            while self.roots[u] != self.roots[v] {
                if self.depth[self.roots[u]] > self.depth[self.roots[v]] {
                    std::mem::swap(&mut u, &mut v);
                }
                v = self.parent[self.roots[v]].unwrap();
            }
            if self.depth[u] <= self.depth[v] { u } else { v }
        }
    }

    use crate::{
        euler_tour_indices::first_positions,
        euler_tour_nodes::euler_tour_nodes,
        query::RangeMinimumQuery,
    };

    /// with euler tour and static range minimum query.
    pub struct EulerTourRMQ<Q> {
        first_pos: Vec<usize>,
        rmq: Q,
    }

    impl<Q> EulerTourRMQ<Q> {
        pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self
        where
            Q: std::iter::FromIterator<(usize, usize)>,
        {
            let tour_nodes = euler_tour_nodes(tree_edges, root);
            let depth = tree_depths(tree_edges, root);
            let first_pos = first_positions(&tour_nodes);
            let depth =
                tour_nodes.iter().map(|&u| depth[u]).collect::<Vec<_>>();
            let rmq =
                Q::from_iter(depth.into_iter().zip(tour_nodes.into_iter()));
            Self { first_pos, rmq }
        }

        pub fn get(&mut self, u: usize, v: usize) -> usize
        where
            Q: RangeMinimumQuery<T = (usize, usize)>,
        {
            let mut left = self.first_pos[u];
            let mut right = self.first_pos[v];
            if left > right {
                std::mem::swap(&mut left, &mut right);
            }
            self.rmq.range_minimum(left, right + 1).1
        }
    }

    use crate::{
        algebraic_structure_impl::*,
        group_theory_id::Min,
        segtree::Segtree,
    };

    type CommonG = GroupApprox<(usize, usize), Min>;

    #[allow(dead_code)]
    type ETRMQSeg = EulerTourRMQ<Segtree<CommonG>>;

    use crate::sparse_table::SparseTable;

    #[allow(dead_code)]
    type ETRMQSpT = EulerTourRMQ<SparseTable<CommonG>>;

    use crate::sqrt_decomposition::SqrtDecomposition;

    #[allow(dead_code)]
    type ETRMQSqD = EulerTourRMQ<SqrtDecomposition<CommonG>>;

    use crate::sparse_table::DisjointSparseTable;

    #[allow(dead_code)]
    type ETRMQDSpT = EulerTourRMQ<DisjointSparseTable<CommonG>>;
}

// TODO:
pub mod dyn_tree {
    //! LCA for dynamic tree.

    // draft
    // by using e.g. lazy segment tree, we can remove a node from tree, and
    // answer for the lca query.
    // if a node is removed, all the descendants' depth are reduced by 1
    // -> range add range minimum query.
    // also, by using dynamic binary search tree like (lazy?) splay tree,
    // we might be able to add a node in addition to removing a node.
}

// TODO:
pub mod dag {
    //! LCA on a DAG.
}
