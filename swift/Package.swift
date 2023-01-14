// swift-tools-version: 5.6

import PackageDescription

let package = Package(
  name: "dsalgo", products: [.library(name: "dsalgo", targets: ["dsalgo"])],
  dependencies: [],

  targets: [
    .target(
      name: "dsalgo", dependencies: [], resources: [.process("Sources/")]),
    .testTarget(name: "swift", dependencies: ["swift"]),
  ])
