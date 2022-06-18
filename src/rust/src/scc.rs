//! strongly connected components

pub fn scc_kosaraju(sparse_graph: Vec<Vec<usize>>) -> Vec<usize> {
    SCCKosaraju::compute_labels(sparse_graph)
}

struct SCCKosaraju {
    graph: Vec<Vec<usize>>,
    visited: Vec<bool>,
    topological_reverse_order: Vec<usize>,
    labels: Vec<usize>,
}

impl SCCKosaraju {
    fn compute_labels(directed_sparse_graph: Vec<Vec<usize>>) -> Vec<usize> {
        let mut scc = SCCKosaraju::new(directed_sparse_graph);

        for u in 0..scc.size() {
            if !scc.visited[u] {
                scc.compute_topological_rev_ord(u);
            }
        }
        scc.transpose_graph();
        let mut label = 0;
        for u in scc.topological_reverse_order.clone().into_iter().rev() {
            if scc.labels[u] != scc.size() {
                continue;
            }
            scc.labeling(label, u);
            label += 1;
        }
        scc.labels
    }

    fn new(directed_sparse_graph: Vec<Vec<usize>>) -> Self {
        let n = directed_sparse_graph.len();
        Self {
            graph: directed_sparse_graph,
            visited: vec![false; n],
            topological_reverse_order: vec![],
            labels: vec![n; n],
        }
    }

    fn size(&self) -> usize { self.graph.len() }

    fn transpose_graph(&mut self) {
        let n = self.size();
        let mut g = vec![vec![]; n];
        for i in 0..n {
            for &j in &self.graph[i] {
                g[j].push(i);
            }
        }
        self.graph = g;
    }

    fn compute_topological_rev_ord(&mut self, u: usize) {
        self.visited[u] = true;
        for v in self.graph[u].clone().into_iter() {
            if !self.visited[v] {
                Self::compute_topological_rev_ord(self, v);
            }
        }
        self.topological_reverse_order.push(u);
    }

    // components are fixed in topological order for initial(user-given) edges.
    fn labeling(&mut self, label: usize, u: usize) {
        self.labels[u] = label;
        for v in self.graph[u].clone().into_iter() {
            if self.labels[v] == self.size() {
                self.labeling(label, v);
            }
        }
    }
}

/// essentially same with Path-Based algorithm
pub fn scc_tarjan_lowlink(sparse_graph: &[Vec<usize>]) -> Vec<usize> {
    SCCTarjanLowLink::compute_labels(sparse_graph)
}

// just a data wrapper to avoid having many parameters in a dfs function.
struct SCCTarjanLowLink<'a> {
    graph: &'a [Vec<usize>],
    stack: Vec<usize>,
    orders: Vec<usize>,
    order: usize,
    low_order: Vec<usize>,
    labels: Vec<usize>,
    label: usize,
}

impl<'a> SCCTarjanLowLink<'a> {
    pub fn compute_labels(
        directed_sparse_graph: &'a [Vec<usize>],
    ) -> Vec<usize> {
        let mut scc = Self::new(directed_sparse_graph);
        for i in 0..scc.size() {
            if scc.labels[i] == scc.size() {
                Self::labeling(&mut scc, i);
            }
        }
        Self::topological_sort(scc.labels)
    }

    fn new(graph: &'a [Vec<usize>]) -> Self {
        let n = graph.len();
        Self {
            graph,
            stack: vec![],
            orders: vec![n; n],
            order: 0,
            low_order: vec![n; n],
            labels: vec![n; n],
            label: 0,
        }
    }

    fn size(&self) -> usize { self.graph.len() }

    // labels are fixed in topologically reverse order of components.
    fn labeling(scc: &mut Self, u: usize) {
        scc.orders[u] = scc.order;
        scc.order += 1;
        scc.stack.push(u);
        for &v in &scc.graph[u] {
            if scc.orders[v] == scc.size() {
                Self::labeling(scc, v);
                scc.low_order[u] = std::cmp::min(
                    scc.low_order[u],
                    scc.low_order[v],
                );
            } else if scc.labels[v] == scc.size() {
                // v is not in a scc yet.
                scc.low_order[u] =
                    std::cmp::min(scc.low_order[u], scc.orders[v]);
                // `s.t. if low[v] < low[u] then low[u] = low[v]`?
                // but low[v] is still under computing.
                // here,
                // it's just enough to know whether
                // low[u] can be smaller than or equal to ord[v].
            }
        }
        if scc.low_order[u] < scc.orders[u] {
            return;
        }
        // a scc is fixed.
        loop {
            let v = scc.stack.pop().unwrap();
            scc.labels[v] = scc.label;
            if v == u {
                break;
            }
        }
        scc.label += 1;
    }

    fn topological_sort(labels: Vec<usize>) -> Vec<usize> {
        // after labeling, labels are still reverse order
        // in a point of topologicality.
        let k = *labels.iter().max().unwrap();
        labels.into_iter().map(|l| k - l).collect::<Vec<_>>()
    }
}

/// essentially same with Tarjan's Lowlink algorithm
pub fn scc_path_based(sparse_graph: &[Vec<usize>]) -> Vec<usize> {
    SCCPathBased::compute_labels(sparse_graph)
}

struct SCCPathBased<'a> {
    graph: &'a [Vec<usize>],
    stack: Vec<usize>,
    low_stack: Vec<usize>,
    orders: Vec<usize>,
    order: usize,
    labels: Vec<usize>,
    label: usize,
}

impl<'a> SCCPathBased<'a> {
    pub fn compute_labels(
        directed_sparse_graph: &'a [Vec<usize>],
    ) -> Vec<usize> {
        let mut scc = Self::new(directed_sparse_graph);
        for i in 0..scc.size() {
            if scc.labels[i] == scc.size() {
                Self::labeling(&mut scc, i);
            }
        }
        Self::topological_sort(scc.labels)
    }

    fn new(graph: &'a [Vec<usize>]) -> Self {
        let n = graph.len();
        Self {
            graph,
            stack: vec![],
            low_stack: vec![],
            orders: vec![n; n],
            order: 0,
            labels: vec![n; n],
            label: 0,
        }
    }

    fn size(&self) -> usize { self.graph.len() }

    fn labeling(scc: &mut Self, u: usize) {
        scc.orders[u] = scc.order;
        scc.order += 1;
        scc.stack.push(u);
        scc.low_stack.push(u);
        for &v in &scc.graph[u] {
            if scc.orders[v] == scc.size() {
                Self::labeling(scc, v);
            } else if scc.labels[v] == scc.size() {
                while scc.orders[*scc.low_stack.last().unwrap()] > scc.orders[v]
                {
                    scc.low_stack.pop();
                }
            }
        }
        if scc.low_stack.last().unwrap() != &u {
            return;
        }
        loop {
            let v = scc.stack.pop().unwrap();
            scc.labels[v] = scc.label;
            if v == u {
                break;
            }
        }
        scc.label += 1;
        scc.low_stack.pop();
    }

    fn topological_sort(labels: Vec<usize>) -> Vec<usize> {
        let k = *labels.iter().max().unwrap();
        labels.into_iter().map(|l| k - l).collect::<Vec<_>>()
    }
}

// TODO:
pub fn scc_reachability_based() {}

// TODO
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
