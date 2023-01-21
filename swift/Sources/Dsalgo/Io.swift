import Foundation

private func readStrings() -> [String] {
  return readLine()!.split(separator: " ").map { String($0) }
}
private class Scanner {
  private var tokens: [String] = []
  init() {}
  func str() -> String {
    while tokens.isEmpty { tokens = readStrings().reversed() }
    return tokens.popLast()!
  }
  func strs(_ n: Int) -> [String] { return (0..<n).map { _ in str() } }
  func int() -> Int { return Int(str())! }
  func ints(_ n: Int) -> [Int] { return (0..<n).map { _ in int() } }
  func intMatrix(_ h: Int, _ w: Int) -> [[Int]] {
    return (0..<h).map { _ in (0..<w).map { _ in int() } }
  }
}

private func printArr<T>(_ a: [T]) {
  let n = a.count
  for i in 0..<n { print(a[i], terminator: i == n - 1 ? "\n" : " ") }
}
