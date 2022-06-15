package dsalgo

type PartialOrd interface {
	func(a, b interface{}) bool
}
