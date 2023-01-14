package types


/* cut below */



type Bool bool


func (
	b Bool,
) Int() (
	Int,
) {
	if b {return 1}
	return 0
}
