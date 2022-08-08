pub trait Monoid {
    type T;
    fn op(&self, _: Self::T, _: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub trait Edge {
    fn to(&self) -> usize;
}
pub struct ReRootingDP<'a, M: Monoid, E, F> {
    g: &'a [Vec<E>],
    m: M,
    f: F,
    rev_edge: Vec<Option<&'a E>>,
    dp_from_childs: Vec<M::T>,
    dp: Vec<M::T>,
}
impl<'a, M: Monoid, E, F: Fn(&E, M::T) -> M::T> ReRootingDP<'a, M, E, F>
where
    M::T: Clone + std::fmt::Debug,
    E: Clone + Edge,
{
    fn new(g: &'a [Vec<E>], m: M, f: F) -> Self {
        let n = g.len();
        let dp_from_childs = vec![m.e(); n];
        let dp = vec![m.e(); n];
        let rev_edge = vec![None; n];
        Self { g, m, f, rev_edge, dp_from_childs, dp }
    }

    pub fn calc(g: &'a [Vec<E>], m: M, f: F) -> Vec<M::T> {
        let mut wrapper = Self::new(g, m, f);
        wrapper.tree_dp(0, 0);
        wrapper.reroot(0, 0, wrapper.m.e());
        wrapper.dp
    }

    fn tree_dp(&mut self, u: usize, parent: usize) {
        for e in self.g[u].iter() {
            let v = e.to();
            if v == parent {
                self.rev_edge[u] = Some(e);
                continue;
            }
            self.tree_dp(v, u);
            self.dp_from_childs[u] = self.m.op(
                self.dp_from_childs[u].clone(),
                (self.f)(&e, self.dp_from_childs[v].clone()),
            );
        }
    }

    fn reroot(&mut self, u: usize, parent: usize, x: M::T) {
        self.dp[u] = self.m.op(x.clone(), self.dp_from_childs[u].clone());
        let mut childs = vec![];
        for e in self.g[u].iter() {
            if e.to() != parent {
                childs.push(e.clone());
            }
        }
        let n = childs.len();
        let mut dp_l = vec![self.m.e(); n + 1];
        let mut dp_r = vec![self.m.e(); n + 1];
        for (i, e) in childs.iter().enumerate() {
            dp_l[i + 1] = self.m.op(
                dp_l[i].clone(),
                (self.f)(&e, self.dp_from_childs[e.to()].clone()),
            );
        }
        for (i, e) in childs.iter().enumerate().rev() {
            dp_r[i] = self.m.op(
                (self.f)(&e, self.dp_from_childs[e.to()].clone()),
                dp_r[i + 1].clone(),
            );
        }
        for (i, e) in childs.iter().enumerate() {
            let y = (self.f)(
                self.rev_edge[e.to()].unwrap(),
                self.m.op(
                    x.clone(),
                    self.m.op(dp_l[i].clone(), dp_r[i + 1].clone()),
                ),
            );
            self.reroot(e.to(), u, y)
        }
    }
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
        let res = ReRootingDP::calc(&g, M {}, &map);
        assert_eq!(res, [8, 6, 6]);
    }
}
