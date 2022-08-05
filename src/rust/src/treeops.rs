use crate::tree_edges_to_graph::tree_edges_to_graph;
pub fn tree_dfs<T, F>(
    tree_edges: &[(usize, usize)], root: usize, default_data: Vec<T>,
    mut assign: F,
) -> Vec<T>
where
    F: FnMut(&mut Vec<T>, usize, usize),
{
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    assert!(default_data.len() == n);
    let mut parent = vec![None; n];
    let mut data = default_data;
    let mut stack: Vec<isize> = Vec::new();
    stack.push(root as isize);
    while let Some(u) = stack.pop() {
        if u < 0 {
            let u = !u as usize;
            if let Some(p) = parent[u] {
                assign(&mut data, p, u);
            }
            continue;
        }
        stack.push(!u);
        let u = u as usize;
        for &v in graph[u].iter() {
            if Some(v) == parent[u] {
                continue;
            }
            parent[v] = Some(u);
            stack.push(v as isize);
        }
    }
    data
}
// TODO: genelized edge type.
// TODO: return parent and data
pub fn tree_bfs<T, F>(
    tree_edges: &[(usize, usize)], root: usize, default_data: Vec<T>,
    mut assign: F,
) -> Vec<T>
where
    F: FnMut(&mut Vec<T>, usize, usize),
{
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    assert!(default_data.len() == n);
    let mut que = std::collections::VecDeque::new();
    let mut parent = vec![None; n];
    let mut data = default_data;
    que.push_back(root);
    while let Some(u) = que.pop_front() {
        for &v in graph[u].iter() {
            if Some(v) == parent[u] {
                continue;
            }
            parent[v] = Some(u);
            assign(&mut data, u, v);
            que.push_back(v);
        }
    }
    data
}
pub fn tree_depths(tree_edges: &[(usize, usize)], root: usize) -> Vec<usize> {
    tree_bfs::<usize, _>(
        tree_edges,
        root,
        vec![0; tree_edges.len() + 1],
        |depth, u, v| {
            depth[v] = depth[u] + 1;
        },
    )
}
// TODO: change interface edges -> Adjacency list
pub fn tree_parents(e: &[(usize, usize)], r: usize) -> Vec<Option<usize>> {
    tree_bfs::<Option<usize>, _>(
        e,
        r,
        vec![None; e.len() + 1],
        |parent, u, v| {
            parent[v] = Some(u);
        },
    )
}
pub fn tree_sizes(tree_edges: &[(usize, usize)], root: usize) -> Vec<usize> {
    tree_dfs::<usize, _>(
        tree_edges,
        root,
        vec![1; tree_edges.len() + 1],
        |size, u, v| {
            size[u] += size[v];
        },
    )
}
