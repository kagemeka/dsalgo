pub fn path_based(adj_list: &[Vec<usize>]) -> Vec<usize> {
    let g = adj_list;
    let n = g.len();

    let mut order = vec![n; n];
    let mut labels = vec![n; n];
    let mut o = 0;
    let mut l = 0;

    let mut st = vec![];
    let mut st_low = vec![];
    let mut st_dfs = vec![];
    for i in 0..n {
        if order[i] != n {
            continue;
        }
        st_dfs.push(i as isize);
        while let Some(u) = st_dfs.pop() {
            if u < 0 {
                let u = !u as usize;
                if st_low.last().unwrap() != &u {
                    continue;
                }
                loop {
                    let v = st.pop().unwrap();
                    labels[v] = l;
                    if v == u {
                        break;
                    }
                }
                l += 1;
                st_low.pop();
                continue;
            }
            let u = u as usize;
            if order[u] != n {
                continue;
            }
            st_dfs.push(!(u as isize));
            order[u] = o;
            o += 1;
            st.push(u);
            st_low.push(u);
            for &v in g[u].iter() {
                if order[v] == n {
                    st_dfs.push(v as isize);
                } else if labels[v] == n {
                    while order[*st_low.last().unwrap()] > order[v] {
                        st_low.pop();
                    }
                }
            }
        }
    }
    use crate::scc_topological_sort::toposort;
    toposort(labels)
}
