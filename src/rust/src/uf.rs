//! Disjoint-Set-Union (DSU) or Union-Find (UF).

pub trait Root {
    fn root(&mut self, u: usize) -> usize;
}

trait Size {
    fn size(&self) -> usize;
}

pub trait Unite {
    fn unite(&mut self, u: usize, v: usize);
}

pub trait SizeOf {
    fn size_of(&mut self, u: usize) -> usize;
}

pub trait Same {
    fn same(&mut self, u: usize, v: usize) -> bool;
}

impl<U: Root> Same for U {
    fn same(&mut self, u: usize, v: usize) -> bool {
        self.root(u) == self.root(v)
    }
}

pub trait Labels {
    fn labels(&mut self) -> Vec<usize>;
}

impl<U: Root + Size> Labels for U {
    /// same label -> same component.
    fn labels(&mut self) -> Vec<usize> {
        let n = self.size();
        let mut label = vec![n; n];
        let mut l = 0;
        for i in 0..n {
            let r = self.root(i);
            if label[r] == n {
                label[r] = l;
                l += 1;
            }
            label[i] = label[r];
        }
        label
    }
}

#[derive(Debug)]
pub struct UF {
    a: Vec<isize>, // neg-size or parent
}

impl UF {
    pub fn new(size: usize) -> Self { Self { a: vec![-1; size] } }
}

impl Size for UF {
    fn size(&self) -> usize { self.a.len() }
}

impl Root for UF {
    fn root(&mut self, u: usize) -> usize {
        if self.a[u] < 0 {
            return u;
        }
        self.a[u] = self.root(self.a[u] as usize) as isize;
        self.a[u] as usize
    }
}

impl Unite for UF {
    fn unite(&mut self, u: usize, v: usize) {
        let mut u = self.root(u);
        let mut v = self.root(v);
        if u == v {
            return;
        }
        if self.a[u] > self.a[v] {
            std::mem::swap(&mut u, &mut v);
        }
        self.a[u] += self.a[v];
        self.a[v] = u as isize;
    }
}

impl SizeOf for UF {
    /// size of the component containing u
    fn size_of(&mut self, u: usize) -> usize {
        let u = self.root(u);
        -self.a[u] as usize
    }
}

use crate::algebraic_structure::*;
pub struct PotentialUF<G: AbelianGroup> {
    a: Vec<isize>, // neg-size or parent
    rp: Vec<G::S>, // relative potential from parent
}

impl<G: AbelianGroup> Size for PotentialUF<G> {
    fn size(&self) -> usize { self.a.len() }
}

impl<G> PotentialUF<G>
where
    G: AbelianGroup,
    G::S: Clone,
{
    pub fn new(size: usize) -> Self {
        Self {
            a: vec![-1; size],
            rp: (0..size).map(|_| G::e()).collect(),
        }
    }

    /// relative potential from the root.
    fn h(&mut self, u: usize) -> G::S {
        self.root(u);
        self.rp[u].clone()
    }

    /// potential v against u.
    pub fn diff(&mut self, u: usize, v: usize) -> Result<G::S, &'static str> {
        if self.root(u) != self.root(v) {
            Err("different components")
        } else {
            Ok(G::op(
                G::inv(self.h(u)),
                self.h(v),
            ))
        }
    }

    pub fn unite(
        &mut self,
        mut u: usize,
        mut v: usize,
        d: G::S, // potential v against u
    ) where
        G::S: PartialEq,
    {
        let mut d = G::op(
            G::op(self.h(u), d),
            G::inv(self.h(v).clone()),
        );
        u = self.root(u);
        v = self.root(v);
        if u == v {
            debug_assert!(d == G::e());
            return;
        }
        if self.a[u] > self.a[v] {
            std::mem::swap(&mut u, &mut v);
            d = G::inv(d);
        }
        self.a[u] += self.a[v];
        self.a[v] = u as isize;
        self.rp[v] = d;
    }
}

impl<G> Root for PotentialUF<G>
where
    G: AbelianGroup,
    G::S: Clone,
{
    fn root(&mut self, u: usize) -> usize {
        if self.a[u] < 0 {
            return u;
        }
        let p = self.a[u] as usize;
        self.a[u] = self.root(p) as isize;
        self.rp[u] = G::op(
            self.rp[u].clone(),
            self.rp[p].clone(),
        );
        self.a[u] as usize
    }
}

impl<G> SizeOf for PotentialUF<G>
where
    G: AbelianGroup,
    G::S: Clone,
{
    fn size_of(&mut self, u: usize) -> usize
    where
        G::S: Clone,
    {
        let u = self.root(u);
        -self.a[u] as usize
    }
}

// TODO:
pub struct RollbackUF {}

// TODO:
pub struct PersitentUF {}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_uf() {
        let mut uf = UF::new(10);
        assert_eq!(uf.size_of(0), 1);
        uf.unite(3, 9);
        assert_eq!(uf.size_of(3), 2);
    }

    #[test]
    fn test_potential_uf() {
        use crate::{algebraic_structure_impl::*, group_theory_id::Additive};
        let mut uf = PotentialUF::<GroupApprox<i32, Additive>>::new(6);
        assert_eq!(uf.size_of(0), 1);
        assert!(uf.diff(0, 5).is_err());
        uf.unite(0, 1, 1);
        uf.unite(5, 4, 2);
        uf.unite(1, 2, 3);
        uf.unite(4, 3, 4);
        uf.unite(2, 3, 5);
        assert_eq!(uf.size_of(4), 6);
        assert_eq!(uf.diff(0, 5), Ok(3));
    }
}
