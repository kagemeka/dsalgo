pub fn kosaraju(adj_list: Vec<Vec<usize>>) -> Vec<usize> {
    let mut g = adj_list;
    let n = g.len();

    let mut visited = vec![false; n];
    let mut labels = vec![n; n];
    let mut que = vec![];
    let mut st = vec![];
    for i in 0..n {
        if visited[i] {
            continue;
        }
        st.push(i as isize);
        while let Some(u) = st.pop() {
            if u < 0 {
                que.push(!u as usize);
                continue;
            }
            if visited[u as usize] {
                continue;
            }
            visited[u as usize] = true;
            st.push(!u);
            for &v in g[u as usize].iter() {
                if !visited[v] {
                    st.push(v as isize);
                }
            }
        }
    }
    use crate::scc_transpose::transpose;
    g = transpose(g);

    let mut l = 0;
    let mut st = vec![];
    for i in que.into_iter().rev() {
        if labels[i] != n {
            continue;
        }
        labels[i] = l;
        st.push(i);
        while let Some(u) = st.pop() {
            for &v in g[u].iter() {
                if labels[v] != n {
                    continue;
                }
                labels[v] = l;
                st.push(v);
            }
        }
        l += 1;
    }
    labels
}
