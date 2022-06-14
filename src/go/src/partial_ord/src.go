package partial_ord

import . "github.com/kagemeka/dsalgo/src/go/src/primitive_interface"

type PartialOrd interface {
	func(a, b interface{}) bool
}

type PrimitiveOrd interface {
	Integer | Float | ~string
}
