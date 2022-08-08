use crate::bit_length_with_count_leading_zeros_usize::bit_length;
pub trait Ops {
    type S;
    type F;
    fn op(&self, a: Self::S, b: Self::S) -> Self::S;
    fn e(&self) -> Self::S;
    fn compose(&self, f: Self::F, g: Self::F) -> Self::F;
    fn id(&self) -> Self::F;
    fn map(&self, f: Self::F, x: Self::S) -> Self::S;
}
#[derive(Debug)]
pub struct LazySegtree<O: Ops> {
    ops: O,
    data: Vec<O::S>,
    lazy: Vec<O::F>,
    size: usize,
}
impl<O: Ops> LazySegtree<O>
where
    O::S: Clone,
    O::F: Clone,
{
    pub fn new(ops: O, size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![ops.e(); n << 1];
        let lazy = vec![ops.id(); n];
        Self { ops, data, lazy, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.lazy.len() }

    fn height(&self) -> usize { bit_length(self.n()) }

    fn merge(&mut self, i: usize) {
        self.data[i] = self
            .ops
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    fn apply_node(&mut self, i: usize, f: O::F) {
        self.data[i] = self.ops.map(f.clone(), self.data[i].clone());
        if i < self.n() {
            self.lazy[i] = self.ops.compose(f, self.lazy[i].clone());
        }
    }

    fn propagate(&mut self, i: usize) {
        let f = self.lazy[i].clone();
        self.apply_node(i << 1, f.clone());
        self.apply_node(i << 1 | 1, f);
        self.lazy[i] = self.ops.id();
    }

    fn pull(&mut self, i: usize) {
        for j in (1..self.height()).rev() {
            self.propagate(i >> j);
        }
    }

    fn merge_above(&mut self, mut i: usize) {
        while i > 1 {
            i >>= 1;
            self.merge(i);
        }
    }

    pub fn apply(&mut self, l: usize, r: usize, f: O::F) {
        assert!(l <= r && r <= self.size);
        self._apply(l, r, 0, self.n(), 1, f);
    }

    fn _apply(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize, f: O::F,
    ) {
        if cr <= l || r <= cl {
            return;
        }
        if l <= cl && cr <= r {
            self.apply_node(i, f);
            return;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        self._apply(l, r, cl, c, i << 1, f.clone());
        self._apply(l, r, c, cr, i << 1 | 1, f);
        self.merge(i);
    }

    pub fn set(&mut self, mut i: usize, x: O::S) {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i] = x;
        self.merge_above(i);
    }

    pub fn fold(&mut self, l: usize, r: usize) -> O::S {
        assert!(l <= r && r <= self.size);
        self._fold(l, r, 0, self.n(), 1)
    }

    fn _fold(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize,
    ) -> O::S {
        if cr <= l || r <= cl {
            return self.ops.e();
        }
        if l <= cl && cr <= r {
            return self.data[i].clone();
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        let vl = self._fold(l, r, cl, c, i << 1);
        let vr = self._fold(l, r, c, cr, i << 1 | 1);
        self.ops.op(vl, vr)
    }

    pub fn max_right<G>(&mut self, is_ok: &G, l: usize) -> usize
    where
        G: Fn(&O::S) -> bool,
    {
        assert!(l <= self.size);
        self._max_right(is_ok, l, 0, self.n(), &mut self.ops.e(), 1)
    }

    fn _max_right<G>(
        &mut self, is_ok: &G, l: usize, cl: usize, cr: usize, v: &mut O::S,
        i: usize,
    ) -> usize
    where
        G: Fn(&O::S) -> bool,
    {
        if cr <= l {
            return l;
        }
        if self.size <= cl {
            return self.size;
        }
        let nv = self.ops.op(v.clone(), self.data[i].clone());
        if l <= cl && cr <= self.size && is_ok(&nv) {
            *v = nv;
            return cr;
        }
        if cr - cl == 1 {
            return cl;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        let r = self._max_right(is_ok, l, cl, c, v, i << 1);
        if r < c || r == self.size {
            return r;
        }
        self._max_right(is_ok, l, c, cr, v, i << 1 | 1)
    }

    pub fn min_left<G>(&mut self, is_ok: &G, r: usize) -> usize
    where
        G: Fn(&O::S) -> bool,
    {
        assert!(r <= self.size);
        self._min_left(is_ok, r, 0, self.n(), &mut self.ops.e(), 1)
    }

    fn _min_left<G>(
        &mut self, is_ok: &G, r: usize, cl: usize, cr: usize, v: &mut O::S,
        i: usize,
    ) -> usize
    where
        G: Fn(&O::S) -> bool,
    {
        if cl >= r {
            return r;
        }
        let nv = self.ops.op(self.data[i].clone(), v.clone());
        if cr <= r && is_ok(&nv) {
            *v = nv;
            return cl;
        }
        if cr - cl == 1 {
            return cr;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        let l = self._min_left(is_ok, r, c, cr, v, i << 1 | 1);
        if l > c || l == 0 {
            return l;
        }
        self._min_left(is_ok, r, cl, c, v, i << 1)
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
