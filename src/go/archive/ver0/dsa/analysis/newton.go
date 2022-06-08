package analysis



/* cut  below */


type NewtonFunc func(
	x Float,
) (Float)


func (
	f NewtonFunc,
) Derivative(
	x Float,
) (
	d Float,
) {
	const dx = 1
	d = (f(x + dx) - f(x)) / dx
	return
}


func (
	f NewtonFunc,
) Newton(
	x0 Float,
) (
	x Float,
) {
	x = x0
	const maxIter = 1 << 7
	const eps = 1e-9
	for
	i := 0;
	i < maxIter;
	i++ {
		y := f(x)
		der := f.Derivative(x)
		dx := y / der
		x -= dx
		dx = dx.Abs().(Float)
		if dx < eps {
			break
		}
	}
	return
}


func Newton(
	f NewtonFunc,
	x0 Float,
) (
	Float,
) {
	return f.Newton(x0)
}
