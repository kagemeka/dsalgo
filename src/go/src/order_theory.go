package dsalgo

type Ord interface {
	Less(interface{}) bool
}

type PartialOrd interface {
	func(a, b interface{}) bool
}

type PrimitiveOrd interface {
	Integer | Float | ~string
}
