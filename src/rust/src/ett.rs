//! euler tour teqnique

use crate::{
    tree_edges_to_graph::tree_edges_to_graph,
    tree_parents::tree_parents,
};

/// Undirected Tree Edges.
pub type E = [(usize, usize)];

pub fn tour_edges(tree_edges: &E, root: usize) -> Vec<isize> {
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    let mut parent = vec![None; n];
    let mut tour = Vec::with_capacity(n << 1);
    let mut stack = vec![root as isize];
    for _ in 0..n << 1 {
        let u = stack.pop().unwrap();
        tour.push(u);
        if u < 0 {
            continue;
        }
        stack.push(!u);
        let u = u as usize;
        graph[u].iter().rev().for_each(|&v| {
            if Some(v) != parent[u] {
                parent[v] = Some(u);
                stack.push(v as isize);
            }
        });
    }
    tour
}

pub fn last_positions(tour_nodes: &[usize]) -> Vec<usize> {
    let n = tour_nodes.iter().max().unwrap() + 1;
    let mut pos = vec![None; n];
    tour_nodes
        .iter()
        .enumerate()
        .for_each(|(i, &u)| pos[u] = Some(i));
    pos.iter().map(|&p| p.unwrap()).collect()
}

pub fn first_positions(tour_nodes: &[usize]) -> Vec<usize> {
    let size = tour_nodes.len();
    let mut tour = tour_nodes.to_vec();
    tour.reverse();
    last_positions(&tour).iter().map(|&i| size - i - 1).collect()
}

pub fn tour_nodes(tree_edges: &E, root: usize) -> Vec<usize> {
    let parent = tree_parents(tree_edges, root);
    tour_edges(tree_edges, root)
        .iter()
        .rev()
        .skip(1)
        .rev()
        .map(
            |&u| {
                if u < 0 { parent[!u as usize].unwrap() } else { u as usize }
            },
        )
        .collect()
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
