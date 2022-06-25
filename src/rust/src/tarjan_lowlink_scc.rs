/// with tarjan's lowlink algorithm.
pub fn tarjan(adj_list: &[Vec<usize>]) -> Vec<usize> {
    let g = adj_list;
    let n = g.len();

    let mut order = vec![n; n];
    let mut labels = vec![n; n];
    let mut o = 0;
    let mut l = 0;

    let mut st = vec![];
    let mut low_ord = vec![n; n];
    let mut st_dfs = vec![];
    let mut parent = vec![n; n];
    for i in 0..n {
        if order[i] != n {
            continue;
        }
        st_dfs.push(i as isize);
        while let Some(u) = st_dfs.pop() {
            if u < 0 {
                let u = !u as usize;
                if low_ord[u] == order[u] {
                    loop {
                        let v = st.pop().unwrap();
                        labels[v] = l;
                        if v == u {
                            break;
                        }
                    }
                    l += 1;
                }
                let p = parent[u];
                if p != n {
                    low_ord[p] = low_ord[p].min(low_ord[u]);
                }
                continue;
            }
            let u = u as usize;
            if order[u] != n {
                continue;
            }
            st_dfs.push(!(u as isize));
            order[u] = o;
            low_ord[u] = o;
            o += 1;
            st.push(u);
            for &v in g[u].iter() {
                if order[v] == n {
                    parent[v] = u;
                    st_dfs.push(v as isize);
                } else if labels[v] == n {
                    low_ord[u] = low_ord[u].min(order[v]);
                }
            }
        }
    }

    use crate::scc_topological_sort::toposort;
    toposort(labels)
}
