func morrisPrattTable<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var lb = [Int](repeating: 0, count: n)  // longest border
  var d = 0
  for i in 1..<n {
    while d != 0 && a[d] != a[i] { d = lb[d - 1] }
    if a[d] == a[i] { d += 1 }
    lb[i] = d
  }
  return lb
}
