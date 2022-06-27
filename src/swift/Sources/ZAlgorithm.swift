func zAlgorithm<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var lcp = [Int](repeating: 0, count: n)
  var l = 0
  for i in 1..<n {
    let r = l + lcp[l]
    var d = r <= i ? 0 : min(lcp[i - l], r - i)
    while i + d < n && a[i + d] == a[d] { d += 1 }
    lcp[i] = d
    if r < i + d { l = i }
  }
  lcp[0] = n
  return lcp
}
