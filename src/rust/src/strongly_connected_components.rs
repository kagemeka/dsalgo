//! strongly connected components
/// directed sparse graph. it not necessarily be simple.
pub type G = Vec<Vec<usize>>;
/// label
pub type L = Vec<usize>;
fn toposort(lb: L) -> L {
    let k = *lb.iter().max().unwrap();
    lb.into_iter().map(|l| k - l).collect::<Vec<_>>()
}
/// with tarjan's lowlink algorithm.
pub fn tarjan(g: G) -> L {
    struct D {
        g: G,
        s: Vec<usize>,   // stack
        ord: Vec<usize>, // preorder
        o: usize,
        lo: Vec<usize>, // low preorder
        lb: L,          // label
        l: usize,
    }
    let n = g.len();
    let mut d = D {
        g,
        s: vec![],
        ord: vec![n; n],
        o: 0,
        lo: vec![n; n],
        lb: vec![n; n],
        l: 0,
    };
    fn labeling(d: &mut D, u: usize) {
        d.ord[u] = d.o;
        d.o += 1;
        d.s.push(u);
        let n = d.g.len();
        for v in d.g[u].clone() {
            if d.ord[v] == n {
                labeling(d, v);
                d.lo[u] = d.lo[u].min(d.lo[v]);
            } else if d.lb[v] == n {
                // on stack
                d.lo[u] = d.lo[u].min(d.ord[v]);
            }
        }
        if d.lo[u] < d.ord[u] {
            return;
        }
        loop {
            let v = d.s.pop().unwrap();
            d.lb[v] = d.l;
            if v == u {
                break;
            }
        }
        d.l += 1;
    }
    for i in 0..n {
        if d.ord[i] == n {
            labeling(&mut d, i);
        }
    }
    toposort(d.lb)
}
// TODO:
// tarjan non recurse
/// essentially same as Tarjan's Lowlink algorithm
pub fn path_based(g: G) -> L {
    struct D {
        g: G,
        s: Vec<usize>,
        sl: Vec<usize>, // stack for lowlink
        ord: Vec<usize>,
        o: usize,
        lb: L,
        l: usize,
    }
    let n = g.len();
    let mut d = D {
        g,
        s: vec![],
        sl: vec![],
        ord: vec![n; n],
        o: 0,
        lb: vec![n; n],
        l: 0,
    };
    fn labeling(d: &mut D, u: usize) {
        d.ord[u] = d.o;
        d.o += 1;
        d.s.push(u);
        d.sl.push(u);
        let n = d.g.len();
        for v in d.g[u].clone() {
            if d.ord[v] == n {
                labeling(d, v);
            } else if d.lb[v] == n {
                while d.ord[*d.sl.last().unwrap()] > d.ord[v] {
                    d.sl.pop();
                }
            }
        }
        if d.sl.last().unwrap() != &u {
            return;
        }
        loop {
            let v = d.s.pop().unwrap();
            d.lb[v] = d.l;
            if v == u {
                break;
            }
        }
        d.l += 1;
        d.sl.pop();
    }
    for i in 0..n {
        if d.ord[i] == n {
            labeling(&mut d, i);
        }
    }
    toposort(d.lb)
}
