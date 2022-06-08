package geometry 


/* cut below */



type LineSegment2D struct {
	V0, V1 Vector2D
}


func (
	s LineSegment2D,
) Intersect(
	other LineSegment2D,
) (
	ok Bool,
) {
	bl0 := s.Across(other)
	bl1 := other.Across(s)
	ok = bl0 && bl1
	return
}


func (
	s LineSegment2D,
) Across (
	other LineSegment2D,
) (
	ok Bool,
) {
	o0 := other.Orientation(
		s.V0,
	)
	o1 := other.Orientation(
		s.V1,
	)
	ok = o0 * o1 <= 0
	return
}


func (
	s LineSegment2D,
) Orientation(
	v Vector2D,
) (
	o Int,
) {
	t := Triangle2D{
		s.V0,
		s.V1,
		v,
	}
	a := t.SignedArea()
	if a < 0 {return -1}
	if a == 0 {return 0}
	if a > 0 {return 1}
	return
}