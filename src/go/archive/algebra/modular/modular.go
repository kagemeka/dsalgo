package modular


import (
	. "kagemeka/general/types"
)

import (
	"fmt"
)



/* cut below */



type Modular struct {
	Value Int
	Mod Int
}


func (
	m *Modular,
) Init() {
	mod := m.Mod
	m.Value %= mod
	m.Value += mod
	m.Value %= mod
}


func (
	m Modular,
) String() string {
	return fmt.Sprint(m.Value)
}


func (
	m *Modular,
) Clone() (
	Modular,
) {
	return Modular(*m)
}


func (
	m *Modular,
) IAdd(
	other Modular,
) {
	m.Value += other.Value
	m.Init()
}


func (
	m Modular,
) Add(
	other Modular,
) Modular {
	m.IAdd(other)
	return m
}


func (
	m Modular,
) Neg() (
	Modular,
){
	m = Modular{
		Value: -m.Value,
		Mod: m.Mod,
	}
	m.Init()
	return m
}


func (
	m *Modular,
) ISub(
	other Modular,
) {
	negOther := other.Neg()
	m.IAdd(negOther)
}


func (
	m Modular,
) Sub(
	other Modular,
) (
	Modular,
) {
	m.ISub(other)
	return m
}


func (
	m *Modular,
) IMul(
	other Modular,
) {
	mod := m.Mod
	m.Value *= other.Value
	m.Value %= mod
}


func (
	m Modular,
) Mul(
	other Modular,
) (
	Modular,
) {
	m.IMul(other)
	return m
}


func (
	m *Modular,
) IDiv(
	other Modular,
) {
	invOther := other.Invert()
	m.IMul(invOther)
}


func (
	m Modular,
) Div(
	other Modular,
) (
	Modular,
) {
	m.IDiv(other)
	return m
}


func (
	m Modular,
) Pow(n Int) (
	Modular,
) {
	mod := m.Mod
	if n == 0 {
		return Modular{1, mod}
	}
	a := m.Pow(n >> 1)
	a.IMul(a)
	if n & 1 == 1 {
		a.IMul(m)
	}
	return a
}


func (
	m *Modular,
) IPow(n Int) {
	m.Value = m.Pow(n).Value
}


func (
	m Modular,
) Invert() (
	Modular,
) {
	return m.Pow(m.Mod - 2)
}


func (
	m Modular,
) Factorial() (
	fact ModSlice,
) {
	n, mod := m.Value, m.Mod
	fact = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		fact[i] = Modular{i, mod}
	}
	fact[0] = Modular{1, mod}
	fact = fact.CumProd()
	return
}


func (
	m Modular,
) InverseFactorial() (
	invFact ModSlice,
) {
	n, mod := m.Value, m.Mod
	fact := m.Factorial()
	invFact = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		invFact[i] = Modular{
			n - i,
			mod,
		}
	}
	invFact[0] = (
		fact[n - 1].
		Invert())
	invFact = invFact.CumProd()
	invFact.Reverse()
	return
}
