pub fn sa_is(mut a: Vec<usize>) -> Vec<usize> {
    let m = *a.iter().min().unwrap();
    for x in a.iter_mut() {
        *x = *x - m + 1;
    }
    a.push(0);
    let n = a.len();
    let m = a.iter().max().unwrap() + 1;
    let mut is_s = vec![true; n];
    let mut is_lms = vec![false; n];
    let mut lms = Vec::with_capacity(n);
    for i in (1..n).rev() {
        is_s[i - 1] = if a[i - 1] == a[i] { is_s[i] } else { a[i - 1] < a[i] };
        is_lms[i] = !is_s[i - 1] && is_s[i];
        if is_lms[i] {
            lms.push(i);
        }
    }
    lms.reverse();
    let mut bucket = vec![0usize; m];
    for &x in a.iter() {
        bucket[x] += 1;
    }
    let induce = |lms: &Vec<usize>| -> Vec<usize> {
        let mut sa = vec![n; n];
        let mut rank = bucket.clone();
        for i in 0..m - 1 {
            rank[i + 1] += rank[i];
        }
        for &i in lms.iter().rev() {
            rank[a[i]] -= 1;
            sa[rank[a[i]]] = i;
        }
        rank = bucket.clone();
        let mut s = 0usize;
        for i in 0..m {
            rank[i] += s;
            std::mem::swap(&mut s, &mut rank[i]);
        }
        for i in 0..n {
            if sa[i] == n || sa[i] == 0 {
                continue;
            }
            let i = sa[i] - 1;
            if !is_s[i] {
                sa[rank[a[i]]] = i;
                rank[a[i]] += 1;
            }
        }
        rank = bucket.clone();
        for i in 0..m - 1 {
            rank[i + 1] += rank[i];
        }
        for i in (0..n).rev() {
            if sa[i] == n || sa[i] == 0 {
                continue;
            }
            let i = sa[i] - 1;
            if is_s[i] {
                rank[a[i]] -= 1;
                sa[rank[a[i]]] = i;
            }
        }
        sa
    };
    let l = lms.len();
    let lms_idx = induce(&lms)
        .into_iter()
        .filter(|&i| is_lms[i])
        .collect::<Vec<_>>();
    let mut rank = vec![n; n];
    let mut r = 0usize;
    rank[n - 1] = r;
    for i in 0..l - 1 {
        let j = lms_idx[i];
        let k = lms_idx[i + 1];
        for d in 0..n {
            let j_is_lms = is_lms[j + d];
            let k_is_lms = is_lms[k + d];
            if a[j + d] != a[k + d] || j_is_lms ^ k_is_lms {
                r += 1;
                break;
            }
            if d > 0 && j_is_lms | k_is_lms {
                break;
            }
        }
        rank[k] = r;
    }
    rank = rank.into_iter().filter(|&x| x != n).collect();
    let mut lms_order: Vec<usize> = Vec::new();
    if r == l - 1 {
        lms_order.resize(l, n);
        for i in 0..l {
            lms_order[rank[i]] = i;
        }
    } else {
        lms_order = sa_is(rank);
    }
    lms = lms_order.iter().map(|&i| lms[i]).collect();
    let sa = induce(&lms);
    sa[1..].to_vec()
}
pub fn from_str(s: &str) -> Vec<usize> {
    sa_is(s.as_bytes().iter().map(|&x| x as usize).collect())
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn suffix_array() {
        let s = vec![1, 1, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 2, 0, 0];
        let answer = vec![15, 14, 10, 6, 2, 11, 7, 3, 1, 0, 13, 12, 9, 5, 8, 4];
        assert_eq!(sa_is(s), answer,);
    }
}
