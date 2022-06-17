package dsalgo

type Magma[S any] interface {
	op(S, S) S
}

type Semigroup[S any] interface {
	Magma[S]
}

type Monoid[S any] interface {
	Semigroup[S]
	identity() S
}

type Group[S any] interface {
	Monoid[S]
	invert(S) S
}
