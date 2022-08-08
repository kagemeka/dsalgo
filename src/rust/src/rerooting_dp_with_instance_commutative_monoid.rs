pub trait Monoid {
    type T;
    fn op(&self, _: Self::T, _: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub trait Edge {
    fn to(&self) -> usize;
}
pub fn rerooting_dp<M, E, F>(g: &[Vec<E>], m: M, f: F) -> Vec<M::T>
where
    M: Monoid,
    M::T: Clone,
    E: Clone + Edge,
    F: Fn(&E, M::T) -> M::T,
{
    let n = g.len();
    let mut dp_from_childs = vec![m.e(); n];
    let mut dp = vec![m.e(); n];
    let mut parent = vec![n; n];
    let mut st = vec![0isize];
    let mut rev_edge = vec![None; n];
    while let Some(u) = st.pop() {
        if u < 0 {
            let u = !u as usize;
            for e in g[u].iter() {
                let v = e.to();
                if v == parent[u] {
                    continue;
                }
                dp_from_childs[u] = m.op(
                    dp_from_childs[u].clone(),
                    f(e, dp_from_childs[v].clone()),
                );
            }
            continue;
        }
        st.push(!u);
        let u = u as usize;
        for e in g[u].iter() {
            let v = e.to();
            if v == parent[u] {
                rev_edge[u] = Some(e);
                continue;
            }
            parent[v] = u;
            st.push(v as isize)
        }
    }
    let mut st = vec![(0, m.e())];
    while let Some((u, x)) = st.pop() {
        dp[u] = m.op(x.clone(), dp_from_childs[u].clone());
        let mut childs = vec![];
        for e in g[u].iter() {
            if e.to() != parent[u] {
                childs.push(e);
            }
        }
        let n = childs.len();
        let mut dp_l = vec![m.e(); n + 1];
        let mut dp_r = vec![m.e(); n + 1];
        for (i, e) in childs.iter().enumerate() {
            dp_l[i + 1] =
                m.op(dp_l[i].clone(), f(e, dp_from_childs[e.to()].clone()));
        }
        for (i, e) in childs.iter().enumerate().rev() {
            dp_r[i] =
                m.op(f(e, dp_from_childs[e.to()].clone()), dp_r[i + 1].clone());
        }
        for (i, e) in childs.iter().enumerate() {
            let y = f(
                rev_edge[e.to()].unwrap(),
                m.op(x.clone(), m.op(dp_l[i].clone(), dp_r[i + 1].clone())),
            );
            st.push((e.to(), y));
        }
    }
    dp
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        // https://atcoder.jp/contests/abc222/tasks/abc222_f
        struct M;
        impl Monoid for M {
            type T = u64;

            fn op(&self, lhs: Self::T, rhs: Self::T) -> Self::T { lhs.max(rhs) }

            fn e(&self) -> Self::T { 0 }
        }
        #[derive(Clone)]
        struct E {
            to: usize,
            weight: u64,
        }
        impl E {
            pub fn new(to: usize, weight: u64) -> Self { Self { to, weight } }
        }
        impl Edge for E {
            fn to(&self) -> usize { self.to }
        }
        let g =
            vec![vec![E::new(1, 2)], vec![E::new(0, 2), E::new(2, 3)], vec![
                E::new(1, 3),
            ]];
        let d = vec![1, 2, 3];
        let map = |e: &E, x: u64| -> u64 { e.weight + x.max(d[e.to()]) };
        let res = rerooting_dp(&g, M {}, &map);
        assert_eq!(res, [8, 6, 6]);
    }
}
