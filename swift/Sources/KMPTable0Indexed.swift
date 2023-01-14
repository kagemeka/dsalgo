func kmpTable<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var f = [Int](repeating: 0, count: n)  // failure function
  var d = 0
  for i in 1..<n {
    while d != 0 && a[d] != a[i] { d = f[d - 1] }
    if a[d] == a[i] { d += 1 }
    f[i] = d > 0 && i + 1 < n && a[d] == a[i + 1] ? f[d - 1] : d
  }
  return f
}
