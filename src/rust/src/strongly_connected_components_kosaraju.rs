use crate::strongly_connected_components_transpose::transpose;
pub fn scc(adj_list: Vec<Vec<usize>>) -> Vec<usize> {
    let mut g = adj_list;
    let n = g.len();
    let mut visited = vec![false; n];
    let mut labels = vec![n; n];
    let mut reverse_order = vec![];
    let mut st = vec![];
    for i in 0..n {
        if visited[i] {
            continue;
        }
        st.push(i as isize);
        while let Some(u) = st.pop() {
            if u < 0 {
                reverse_order.push(!u as usize);
                continue;
            }
            if visited[u as usize] {
                continue;
            }
            st.push(!u);
            visited[u as usize] = true;
            for &v in g[u as usize].iter() {
                if !visited[v] {
                    st.push(v as isize);
                }
            }
        }
    }
    g = transpose(g);
    let mut l = 0;
    let mut st = vec![];
    for i in reverse_order.into_iter().rev() {
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
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let cases = vec![(
            (6, vec![(1, 4), (5, 2), (3, 0), (5, 5), (4, 1), (0, 3), (4, 2)]),
            vec![3, 1, 2, 3, 1, 0],
        )];
        for ((n, edges), ans) in cases {
            let mut g = vec![vec![]; n];
            for (u, v) in edges {
                g[u].push(v);
            }
            assert_eq!(scc(g), ans);
        }
    }
}
