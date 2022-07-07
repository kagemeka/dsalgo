type L = Vec<usize>;

pub(crate) fn toposort(labels: L) -> L {
    let k = *labels.iter().max().unwrap();
    labels.into_iter().map(|l| k - l).collect::<Vec<_>>()
}
