// import KMPTable0Indexed

func kmpFindAll<T: Comparable>(_ a: [T], _ pattern: [T]) -> [Int] {
  let p = pattern
  let (n, m) = (a.count, p.count)
  let f = kmpTable(p)
  var j = 0
  var indices = [Int]()
  for i in 0..<n {
    while j > 0 && p[j] != a[i] { j = f[j - 1] }
    if p[j] == a[i] { j += 1 }
    if j == m {
      indices.append(i + 1 - m)
      j = f[m - 1]
    }
  }
  return indices
}
