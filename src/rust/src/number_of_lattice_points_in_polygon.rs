use crate::{
    convex_hull_monotone_chain::convex_hull,
    number_of_lattice_points_on_segment::segment_lattice_points,
    polygon_area_2d::polygon_area,
};
/// by Pick's Theorem
/// S = i + 2/b - 1
/// i := interior lattice points
/// b := boundary lattice points
pub fn polygon_lattice_points(a: &[(i64, i64)]) -> i64 {
    let a = convex_hull(a);
    let n = a.len();
    let s = polygon_area(&a);
    let mut b = 0;
    for i in 0..n {
        let j = (i + 1) % n;
        b += segment_lattice_points(a[i].0, a[i].1, a[j].0, a[j].1) - 1;
    }
    dbg!(b, s);
    let i = (s + 1.0 - b as f64 / 2.).round() as i64;
    i + b
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        // ref: https://twitter.com/e869120/status/1393753066331992065/photo/3
        let cases =
            vec![(vec![(1, 3), (2, 1), (5, 2), (8, 3), (5, 5), (3, 4)], 18)];
        for (a, ans) in cases {
            assert_eq!(polygon_lattice_points(&a), ans);
        }
    }
}
