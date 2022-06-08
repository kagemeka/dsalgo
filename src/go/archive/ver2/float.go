package cp 



//



type Float float64


func (
	x Float,
) Less(
	y interface{},
) bool {
	return x < y.(Float)
}