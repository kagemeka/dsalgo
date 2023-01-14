func morrisPrattTable<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var lb = [Int](repeating: 0, count: n + 1)
  var d = -1
  lb[0] = d
  for i in 0..<n {
    while d != -1 && a[d] != a[i] { d = lb[d] }
    d += 1
    lb[i + 1] = d
  }
  return lb
}
