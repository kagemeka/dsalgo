private func readStrings() -> [String] {
  return readLine()!.split(separator: " ").map { String($0) }
}
private class Scanner {
  private var tokens: [String] = []
  init() {}
  func string() -> String {
    while tokens.isEmpty {
      tokens = readStrings().reversed()
    }
    return tokens.popLast()!
  }
  func strings(size: Int) -> [String] {
    return (0..<size).map { _ in string() }
  }
  func int() -> Int {
    return Int(string())!
  }
  func ints(size: Int) -> [Int] {
    return (0..<size).map { _ in int() }
  }
  func intMatrix(h: Int, w: Int) -> [[Int]] {
    return (0..<h).map { _ in (0..<w).map { _ in int() } }
  }

}
