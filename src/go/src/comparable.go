package dsalgo

type Lt interface {
	Lt(Lt) bool
}

type Eq interface {
	comparable
}

type Comparable interface {
	Lt
	Eq
}
