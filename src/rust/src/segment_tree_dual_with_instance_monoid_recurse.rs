pub trait Monoid {
    type T;
    fn op(&self, l: Self::T, r: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub struct DualSegtree<G: Monoid> {
    g: G,
    node: Vec<G::T>,
    size: usize,
}
impl<G: Monoid> DualSegtree<G>
where
    G::T: Clone,
{
    pub fn new(g: G, size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let node = vec![g.e(); n << 1];
        Self { g, node, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.node.len() >> 1 }

    fn operate_node(&mut self, i: usize, x: G::T) {
        self.node[i] = self.g.op(self.node[i].clone(), x);
    }

    fn propagate(&mut self, i: usize) {
        self.operate_node(i << 1, self.node[i].clone());
        self.operate_node(i << 1 | 1, self.node[i].clone());
        self.node[i] = self.g.e();
    }

    pub fn get(&mut self, i: usize) -> G::T {
        assert!(i < self.size());
        self._get(i, 0, self.n(), 1).unwrap()
    }

    fn _get(
        &mut self, i: usize, cl: usize, cr: usize, ci: usize,
    ) -> Option<G::T> {
        if cr <= i || i < cl {
            return None;
        }
        if cr - cl == 1 {
            return Some(self.node[ci].clone());
        }
        self.propagate(ci);
        let c = (cl + cr) >> 1;
        if let Some(res) = self._get(i, cl, c, ci << 1) {
            Some(res)
        } else {
            self._get(i, c, cr, ci << 1 | 1)
        }
    }

    pub fn operate(&mut self, l: usize, r: usize, x: G::T) {
        assert!(l <= r && r <= self.size);
        self._operate(l, r, 0, self.n(), 1, x);
    }

    fn _operate(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize, x: G::T,
    ) {
        if cr <= l || r <= cl {
            return;
        }
        if l <= cl && cr <= r {
            self.operate_node(i, x);
            return;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        self._operate(l, r, cl, c, i << 1, x.clone());
        self._operate(l, r, c, cr, i << 1 | 1, x.clone());
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
