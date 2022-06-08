package cp

//

type Bool bool


func (
	x Bool,
) Int() int {
	if x { return 1 }
	return 0
}
