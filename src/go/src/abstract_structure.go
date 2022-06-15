package dsalgo

type Monoid struct {
	Op func(a, b interface{}) interface{}
	E  func() interface{}
}

type Group struct {
	Op      func(a, b interface{}) interface{}
	E       func() interface{}
	Inverse func(interface{}) interface{}
}
