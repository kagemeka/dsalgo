package primitive_interafce

type UnsingedInteger interface {
	uint | uint8 | uint16 | uint32 | uint64
}

type SignedInteger interface {
	int | int8 | int16 | int32 | int64
}

type Integer interface {
	UnsingedInteger | SignedInteger
}

type Float interface {
	float32 | float64
}
