protocol BinaryOperation {
  associatedtype F
  associatedtype T
  associatedtype I: BinaryOperationId
  func operate(_ op: F) -> T
}

protocol BinaryOperationId {}
struct Addition: BinaryOperationId {}
struct Multiplication: BinaryOperationId {}
extension Int: BinaryOperation {
  typealias F = Int
  typealias T = Int
  typealias I = Addition
  func operate(_ op: Int) -> Int {
    return self + op
  }
}

protocol IdentityElement {
  associatedtype I: BinaryOperationId
  static func identity() -> Self
}

protocol AssociativeProperty: BinaryOperation, Equatable {
  func assertAssociative(first: Self, second: Self, third: Self) -> Bool
}

extension Modular: Equatable {
  static func == (left: Modular, right: Modular) -> Bool {
    return left.value == right.value
  }
}

extension Modular: BinaryOperation {
  typealias F = Modular
  typealias T = Modular
  typealias I = Addition
  func operate(_ op: Modular) -> Modular {
    return op + self
  }
}

extension Modular: AssociativeProperty
where F == Modular, T == Modular {
  func assertAssociative(first: Modular, second: Modular, third: Modular)
    -> Bool
  {
    return self.operate(first) == (second.operate(third)).operate(first)
  }
}

extension Modular: IdentityElement
where F == Modular, T == Modular, I == Addition {
  static func identity() -> Self {
    return Self.init(0)
  }
}
// extension Modular: BinaryOperation {
//     typealias F = Modular
//     typealias T = Modular
//     typealias I = Multiplication
//     func operate(_ op: Modular) -> Modular {
//         return op * self
//     }
// }

// func pow<T>(x: T, exponent: UInt) -> T
// where T: BinaryOperation {
//     if exponent == 0 {
//         return x.identity()
//     }
//     var result = T.one
//     var base = x
//     while exponent > 0 {
//         if exponent % 2 == 1 {
//             result = result * base
//         }
//         exponent /= 2
//         base = base * base
//     }
//     return result
// }
