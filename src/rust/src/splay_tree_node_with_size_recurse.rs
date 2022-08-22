pub struct Node<T> {
    left: Option<Box<Self>>,
    right: Option<Box<Self>>,
    size: usize,
    pub value: T,
}
impl<T> Node<T> {
    pub fn new(value: T) -> Box<Self> {
        Box::new(Self { left: None, right: None, size: 1, value })
    }

    pub(crate) fn size(root: Option<&Box<Self>>) -> usize {
        if let Some(root) = root { root.size } else { 0 }
    }

    fn left_size(&self) -> usize { Self::size(self.left.as_ref()) }

    fn update(&mut self) {
        let lsize = Self::size(self.left.as_ref());
        let rsize = Self::size(self.right.as_ref());
        self.size = lsize + rsize + 1;
    }

    // counter-clock-wise
    fn rotate_left(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.right.take().unwrap();
        root.right = new_root.left.take();
        root.update();
        new_root.left = Some(root);
        new_root.update();
        new_root
    }

    // clock-wise
    fn rotate_right(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.left.take().unwrap();
        root.left = new_root.right.take();
        root.update();
        new_root.right = Some(root);
        new_root.update();
        new_root
    }

    fn state(&self, k: usize) -> isize {
        let lsize = self.left_size();
        if k < lsize {
            -1
        } else if k == lsize {
            0
        } else {
            1
        }
    }

    // bring k-th node to the top
    pub fn splay(mut root: Box<Self>, mut k: usize) -> Box<Self> {
        assert!(k < root.size);
        let s = root.state(k);
        if s == 0 {
            return root;
        }
        if s == -1 {
            let mut c = root.left.take().unwrap();
            let cs = c.state(k);
            if cs == 0 {
                root.left = Some(c);
            } else if s * cs == 1 {
                c.left = Some(Self::splay(c.left.take().unwrap(), k));
                root.left = Some(c);
                root = Self::rotate_right(root);
            } else {
                k -= c.left_size() + 1;
                c.right = Some(Self::splay(c.right.take().unwrap(), k));
                c = Self::rotate_left(c);
                root.left = Some(c);
            }
            Self::rotate_right(root)
        } else {
            k -= root.left_size() + 1;
            let mut c = root.right.take().unwrap();
            let cs = c.state(k);
            if cs == 0 {
                root.right = Some(c);
            } else if s * cs == 1 {
                k -= c.left_size() + 1;
                c.right = Some(Self::splay(c.right.take().unwrap(), k));
                root.right = Some(c);
                root = Self::rotate_left(root);
            } else {
                c.left = Some(Self::splay(c.left.take().unwrap(), k));
                c = Self::rotate_right(c);
                root.right = Some(c);
            }
            Self::rotate_left(root)
        }
    }

    pub fn merge(
        l: Option<Box<Self>>, r: Option<Box<Self>>,
    ) -> Option<Box<Self>> {
        if r.is_none() {
            return l;
        }
        let mut r = r.unwrap();
        r = Self::splay(r, 0);
        r.left = l;
        r.update();
        Some(r)
    }

    pub fn split(
        root: Option<Box<Self>>, i: usize,
    ) -> (Option<Box<Self>>, Option<Box<Self>>) {
        let size = Self::size(root.as_ref());
        assert!(i <= size);
        if i == size {
            return (root, None);
        }
        let mut root = root.unwrap();
        root = Self::splay(root, i);
        let l = root.left.take();
        root.update();
        (l, Some(root))
    }

    pub fn insert(
        root: Option<Box<Self>>, i: usize, node: Option<Box<Self>>,
    ) -> Option<Box<Self>> {
        assert!(i <= Self::size(root.as_ref()));
        let (l, r) = Self::split(root, i);
        Self::merge(Self::merge(l, node), r)
    }

    pub fn pop(
        mut root: Box<Self>, i: usize,
    ) -> (Box<Self>, Option<Box<Self>>) {
        root = Self::splay(root, i);
        let new_root = Self::merge(root.left.take(), root.right.take());
        (root, new_root)
    }

    pub fn binary_search<F>(f: F, root: Option<&Box<Self>>) -> usize
    where
        F: Fn(&T) -> bool,
    {
        if root.is_none() {
            return 0;
        }
        let root = root.unwrap();
        if f(&root.value) {
            Self::binary_search(f, root.left.as_ref())
        } else {
            let offset = root.left_size() + 1;
            offset + Self::binary_search(f, root.right.as_ref())
        }
    }
}
#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
