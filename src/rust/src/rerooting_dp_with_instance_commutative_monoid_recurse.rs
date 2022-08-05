pub trait Monoid {
    type T;
    fn op(&self, _: Self::T, _: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub trait Edge {
    fn to(&self) -> usize;
}
pub trait Reverse {
    fn rev(&self) -> Self;
}
pub struct ReRootingDP<'a, M: Monoid, E, F> {
    g: &'a [Vec<E>],
    m: M,
    f: F,
    dp_from_childs: Vec<M::T>,
    dp_from_parent: Vec<M::T>,
    dp: Vec<M::T>,
}
impl<'a, M: Monoid, E, F: Fn(&E, M::T) -> M::T> ReRootingDP<'a, M, E, F>
where
    M::T: Clone + std::fmt::Debug,
    E: Clone + Edge + Reverse,
{
    fn new(g: &'a [Vec<E>], m: M, f: F) -> Self {
        let n = g.len();
        let dp_from_childs = vec![m.e(); n];
        let dp_from_parent = vec![m.e(); n];
        let dp = vec![m.e(); n];
        Self { g, m, f, dp_from_childs, dp_from_parent, dp }
    }

    pub fn calc(g: &'a [Vec<E>], m: M, f: F) -> Vec<M::T> {
        let mut wrapper = Self::new(g, m, f);
        wrapper.tree_dp(0, 0);
        wrapper.reroot(0, 0);
        wrapper.merge_parent_and_childs();
        wrapper.dp
    }

    fn tree_dp(&mut self, u: usize, parent: usize) {
        for e in self.g[u].iter() {
            let v = e.to();
            if v == parent {
                continue;
            }
            self.tree_dp(v, u);
            self.dp_from_childs[u] = self.m.op(
                self.dp_from_childs[u].clone(),
                (self.f)(&e, self.dp_from_childs[v].clone()),
            );
        }
    }

    fn reroot(&mut self, u: usize, parent: usize) {
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
            self.dp_from_parent[e.to()] = (self.f)(
                &e.rev(),
                self.m.op(
                    self.dp_from_parent[u].clone(),
                    self.m.op(dp_l[i].clone(), dp_r[i + 1].clone()),
                ),
            );
            self.reroot(e.to(), u)
        }
    }

    fn merge_parent_and_childs(&mut self) {
        for i in 0..self.g.len() {
            self.dp[i] = self.m.op(
                self.dp_from_childs[i].clone(),
                self.dp_from_parent[i].clone(),
            );
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
            from: usize,
            to: usize,
            weight: u64,
        }
        impl E {
            pub fn new(from: usize, to: usize, weight: u64) -> Self {
                Self { from, to, weight }
            }
        }
        impl Edge for E {
            fn to(&self) -> usize { self.to }
        }
        impl Reverse for E {
            fn rev(&self) -> Self { Self::new(self.to, self.from, self.weight) }
        }
        let g = vec![
            vec![E::new(0, 1, 2)],
            vec![E::new(1, 0, 2), E::new(1, 2, 3)],
            vec![E::new(2, 1, 3)],
        ];
        let d = vec![1, 2, 3];
        let map = |e: &E, x: u64| -> u64 { e.weight + x.max(d[e.to()]) };
        let res = ReRootingDP::calc(&g, M {}, &map);
        assert_eq!(res, [8, 6, 6]);
    }
}
