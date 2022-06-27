protocol Modulus {
  static var value: Int { get }
}

final class Modular<M> where M: Modulus {
  private var value: Int

  init<T>(_ value: T) where T: BinaryInteger {
    self.value = Self.normalize(value)
  }

  private static func normalize<T>(_ value: T) -> Int
  where T: BinaryInteger {
    var value = Int(value) % M.value
    if value < 0 {
      value += M.value
    }
    return value
  }
}

struct Mod1000000007: Modulus {
  static let value = 1_000_000_007
}

typealias Modular1000000007 = Modular<Mod1000000007>

struct Mod998244353: Modulus {
  static let value = 998_244_353
}

typealias Modular998244353 = Modular<Mod998244353>

// Dynamic Modulus Sample struct.
// internal static value is gonna be changed only once by the user at runtime.
// you can define new Dynamic Modular in the scope of your own source codes.
struct DynamicMod: Modulus {
  private static var isSet = false
  private static var internalValue: Int?
  static var value: Int {
    get {
      assert(isSet, "value is not set")
      return self.internalValue!
    }
    set {
      assert(!isSet, "value is already set")
      assert(
        2 <= newValue && newValue < 1 << 31,
        "2 <= value < 2^31 should be satisfied."
      )
      self.internalValue = newValue
      self.isSet = true
    }
  }

}

typealias DynamicModular = Modular<DynamicMod>

extension Modular: CustomStringConvertible {
  var description: String {
    return String(self.value)
  }
}

extension Modular {
  static func + (left: Modular, right: Modular) -> Modular {
    return Modular(left.value + right.value)
  }

  static func += (left: inout Modular, right: Modular) {
    left.value += right.value
    if left.value >= M.value {
      left.value -= M.value
    }
  }

  static prefix func - (self: Modular) -> Modular {
    return Modular(M.value - self.value)
  }

  static func * (left: Modular, right: Modular) -> Modular {
    return Modular(left.value * right.value)
  }

  static func *= (left: inout Modular, right: Modular) {
    left.value = left.value * right.value % M.value
  }

}
