pub struct UnionFind(Vec<isize>);
impl UnionFind {
    pub fn new(size: usize) -> Self { Self(vec![-1; size]) }

    pub fn size(&self) -> usize { self.0.len() }

    pub fn root(&mut self, u: usize) -> usize {
        return if self.0[u] < 0 {
            u
        } else {
            self.0[u] = self.root(self.0[u] as usize) as isize;
            self.0[u] as usize
        };
    }

    pub fn unite(&mut self, mut u: usize, mut v: usize) {
        u = self.root(u);
        v = self.root(v);
        if u == v {
            return;
        }
        if self.0[u] > self.0[v] {
            (u, v) = (v, u);
        }
        self.0[u] += self.0[v];
        self.0[v] = u as isize;
    }

    pub fn size_of(&mut self, mut u: usize) -> usize {
        u = self.root(u);
        -self.0[u] as usize
    }

    pub fn same(&mut self, u: usize, v: usize) -> bool {
        self.root(u) == self.root(v)
    }

    pub fn labels(&mut self) -> Vec<usize> {
        let n = self.size();
        let mut labels = vec![n; n];
        let mut l = 0;
        for i in 0..n {
            let r = self.root(i);
            if labels[r] == n {
                labels[r] = l;
                l += 1;
            }
            labels[i] = labels[r];
        }
        labels
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_uf() {
        let mut uf = UnionFind::new(10);
        assert_eq!(uf.size_of(0), 1);
        uf.unite(3, 9);
        assert_eq!(uf.size_of(3), 2);
    }
}
