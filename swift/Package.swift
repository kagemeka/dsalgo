// swift-tools-version: 5.6

import PackageDescription

let package = Package(
  name: "Dsalgo",
  products: [.library(name: "Dsalgo", targets: ["Dsalgo"])],
  dependencies: [],

  targets: [
    .target(
      name: "Dsalgo",
      dependencies: [],
      resources: [.process("Sources/")]
    ), .testTarget(name: "swift", dependencies: ["swift"]),
  ]
)
