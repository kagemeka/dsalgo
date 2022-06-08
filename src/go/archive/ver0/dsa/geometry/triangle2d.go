package geometry


/* cut below */



type Triangle2D struct {
	V0, V1, V2 Vector2D
}


func (
	t Triangle2D,
) SignedArea() (
	area Float,
) {
	v1 := t.V1.Sub(t.V0)
	v2 := t.V2.Sub(t.V0)
	cross := v1.Cross(v2)
	switch cross.(type) {
	case Int:
		area = Float(
			cross.(Int),
		)
	case Float:
		area = cross.(Float)
	}
	area /= 2
	return
}


func (
	t Triangle2D,
) Area() (
	Float,
) {
	s :=
		t.SignedArea().
		Abs().
		(Float)
	return s
}
