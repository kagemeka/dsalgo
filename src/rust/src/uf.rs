//! Disjoint-Set-Union (DSU) or Union-Find (UF).

pub trait Root {
    fn root(&mut self, u: usize) -> usize;
}

pub trait Unite {
    fn unite(&mut self, u: usize, v: usize);
}

pub trait Size {
    fn size_of(&mut self, u: usize) -> usize;
}

#[derive(Debug)]
pub struct UF {
    a: Vec<isize>, // neg-size or parent
}

impl UF {
    fn size(&self) -> usize { self.a.len() }

    pub fn new(size: usize) -> Self { Self { a: vec![-1; size] } }
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

impl Size for UF {
    /// size of the component containing u
    fn size_of(&mut self, u: usize) -> usize {
        let u = self.root(u);
        -self.a[u] as usize
    }
}

/// extensions
impl UF {
    /// same label -> same component.
    pub fn labels(&mut self) -> Vec<usize> {
        let n = Self::size(self);
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

    pub fn same(&mut self, u: usize, v: usize) -> bool {
        self.root(u) == self.root(v)
    }
}

// TODO:
pub struct RollbackUF {}

// TODO:
pub struct PersitentUF {}

// TODO: refactor group theory
pub struct PotentialUF<
    S: crate::group_theory::AbelianGroup<I> + Copy,
    I: crate::group_theory::BinaryOperationIdentifier,
> {
    phantom_i: std::marker::PhantomData<I>,
    data: Vec<isize>,
    potential_from_parent: Vec<S>,
}

impl<S, I> PotentialUF<S, I>
where
    S: crate::group_theory::AbelianGroup<I> + Copy,
    I: crate::group_theory::BinaryOperationIdentifier,
{
    pub fn new(size: usize) -> Self
    where
        S: Clone,
    {
        Self {
            phantom_i: std::marker::PhantomData,
            data: vec![-1; size],
            potential_from_parent: vec![S::identity(); size],
        }
    }

    pub fn size(&self) -> usize { self.data.len() }

    pub fn find_root(&mut self, node: usize) -> usize {
        assert!(node < self.size());
        if self.data[node] < 0 {
            return node;
        }
        let parent = self.data[node] as usize;
        self.data[node] = self.find_root(parent) as isize;
        // self.potential_from_parent[node] = S::operate(
        //     &self.potential_from_parent[node],
        //     &self.potential_from_parent[parent],
        // );
        self.potential_from_parent[node] = self.potential_from_parent[node]
            .operate(self.potential_from_parent[parent]);
        self.data[node] as usize
    }

    pub fn potential(&mut self, node: usize) -> S {
        self.find_root(node);
        self.potential_from_parent[node]
        // S::operate(&S::identity(),
        // self.potential_from_parent[node])
    }

    pub fn unite(
        &mut self,
        mut left_node: usize,
        mut right_node: usize,
        potential_left_to_right: S,
    ) where
        S: PartialEq + std::fmt::Debug,
    {
        assert!(left_node < self.size() && right_node < self.size());
        // let mut potential_left_to_right = S::operate(
        //     &S::operate(&self.potential_from_parent[left_node],
        // potential_left_to_right),     &S::invert(&self.
        // potential_from_parent[right_node]), );
        let mut potential_left_to_right = self.potential_from_parent[left_node]
            .operate(potential_left_to_right)
            .operate(self.potential_from_parent[right_node].invert());
        left_node = self.find_root(left_node);
        right_node = self.find_root(right_node);
        if left_node == right_node {
            assert_eq!(
                potential_left_to_right,
                S::identity()
            );
            return;
        }
        if self.data[left_node] > self.data[right_node] {
            (left_node, right_node) = (right_node, left_node);
            // potential_left_to_right =
            // S::invert(&potential_left_to_right);
            potential_left_to_right = potential_left_to_right.invert();
        }
        self.data[left_node] += self.data[right_node];
        self.data[right_node] = left_node as isize;
        self.potential_from_parent[right_node] = potential_left_to_right;
    }

    pub fn size_of(&mut self, node: usize) -> usize {
        assert!(node < self.size());
        let root = self.find_root(node);
        -self.data[root] as usize
    }

    pub fn potential_difference(
        &mut self,
        from: usize,
        to: usize,
    ) -> Option<S> {
        if self.find_root(from) != self.find_root(to) {
            None
        } else {
            Some(self.potential(from).invert().operate(self.potential(to)))
            // Some(S::operate(
            //     &S::invert(&self.potential(from)),
            //     &self.potential(to),
            // ))
        }
    }
}

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
        use crate::group_theory::Additive;
        let mut uf = super::PotentialUF::<i32, Additive>::new(10);
        assert_eq!(uf.size_of(0), 1);
        // uf.unite(3, 9, &5);
        uf.unite(3, 9, 5);
        assert_eq!(uf.size_of(3), 2);
        assert_eq!(
            uf.potential_difference(3, 9),
            Some(5)
        );
        assert_eq!(
            uf.potential_difference(1, 3),
            None
        );
    }
}
