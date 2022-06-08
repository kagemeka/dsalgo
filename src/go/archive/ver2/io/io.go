package cp

//
type IO struct {
	r *Read
	w *Write
}


func (
	io *IO,
) Init() {
	r := new(Read)
	r.Init()
	w := new(Write)
	w.Init()
	io.r, io.w = r, w
}


func (
	io *IO,
) Read() (
	string,
) {
	return io.r.Str()
}


func (
	io *IO,
) ReadInt() (
	int,
) {
	return io.r.Int()
}


func (
	io *IO,
) Write(
	a ...interface{},
) {
	io.w.All(a...)
}
