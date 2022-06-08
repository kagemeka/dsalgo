package adhoc


/* cut below */



type DistXFormCDT struct {
	A IntMatrix
	B IntMatrix
	i, j Int
}


func (
	cdt *DistXFormCDT,
) SetMat(
	a IntMatrix,
) {
	cdt.A = a
}


func (
	cdt *DistXFormCDT,
) Prepare(
	inf Int,
) {
	a := cdt.A
	n, m := a.Shape()
	b := cdt.B.Make(n, m, inf)
	cdt.B = b
	for i := Int(0); i < n; i++ {
		cdt.i = i
		cdt.prepareSupport()
	}
}


func (
	cdt *DistXFormCDT,
) prepareSupport() {
	a := cdt.A
	b := cdt.B
	i := cdt.i
	_, m := b.Shape()
	for j := Int(0); j < m; j++ {
		if a[i][j] == 1 {
			continue
		}
		b[i][j] = 0
	}
}


func (
	cdt *DistXFormCDT,
) Taxicab() {
	cdt.CumMin()
	cdt.B.Reverse()
	cdt.CumMin()
	cdt.B.TransPose()
	cdt.CumMin()
	cdt.B.Reverse()
	cdt.CumMin()
	cdt.B.TransPose()
}


func (
	cdt *DistXFormCDT,
) CumMin() {
	b := cdt.B
	n, _ := b.Shape()
	for
	i := Int(0); i < n - 1; i++ {
		cdt.i = i
		cdt.cumMinSupport()
	}
}


func (
	cdt *DistXFormCDT,
) cumMinSupport() {
	b := cdt.B
	i := cdt.i
	_, m := b.Shape()
	for j := Int(0); j < m; j++ {
		b[i + 1][j] = Min(
			b[i + 1][j],
			b[i][j] + 1,
		).(Int)
	}
}
