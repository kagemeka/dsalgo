package geometry 


/* cut below */



type Polygon2D []Vector2D


func (
	p *Polygon2D,
) Push(
	x interface{},
) {
	*p = append(
		*p,
		x.(Vector2D),
	)
}