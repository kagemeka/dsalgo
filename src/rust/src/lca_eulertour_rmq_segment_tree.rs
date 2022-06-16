use crate::{
    group_theory_id::Min,
    lca_eulertour_rmq::LCAEulerTourRMQ,
    segment_tree::Segtree,
};

#[allow(dead_code)]
type LCAEulerTourRMQSegTree = LCAEulerTourRMQ<Segtree<(usize, usize), Min>>;
