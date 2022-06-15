package dsalgo

func Assert(ok bool) {
	if !ok {
		panic("assertion failed")
	}
}
