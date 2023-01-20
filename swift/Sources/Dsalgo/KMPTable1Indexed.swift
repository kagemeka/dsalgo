func kmpTable<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var f = [Int](repeating: 0, count: n + 1)
  var d = -1
  f[0] = d
  for i in 0..<n {
    while d != -1 && a[d] != a[i] { d = f[d] }
    d += 1
    f[i + 1] = i + 1 < n && a[d] == a[i + 1] ? f[d] : d
  }
  return f
}
