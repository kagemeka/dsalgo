// import ZAlgorithm.swift
func zAlgorithmFindAll<T: Comparable>(_ a: [T], _ pattern: [T]) -> [Int] {
  let p = pattern
  let (n, m) = (a.count, p.count)
  let z = Array(zAlgorithm(p + a)[m...])
  var indices = [Int]()
  for i in 0..<n where z[i] >= m { indices.append(i) }
  return indices
}
