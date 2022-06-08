package vector 

import (
	. "kagemeka/general/types"
)


/* cut below */



type Vector2D struct {
	X, Y Numeric
}


func (
	v Vector2D,
) Norm() (
	norm Float,
) {
	norm = v.SqNorm().Root(2)
	return
}


func (
	v Vector2D,
) SqNorm() (
	Numeric,
) {
	x2 := v.X.Pow(2)
	y2 := v.Y.Pow(2)
	return x2.Add(y2)
}


func (
	v *Vector2D,
) IAdd(
	other Vector2D,
) {
	v.X = v.X.Add(other.X)
	v.Y = v.Y.Add(other.Y)
}


func (
	v Vector2D,
) Add(
	other Vector2D,
) (
	Vector2D,
) {
	v.IAdd(other)
	return v
}


func (
	v Vector2D,
) Neg() (
	Vector2D,
) {
	return Vector2D{
		v.X.Neg(),
		v.Y.Neg(),
	}
}


func (
	v *Vector2D,
) ISub(
	other Vector2D,
) {
	v.X = v.X.Sub(other.X)
	v.Y = v.Y.Sub(other.Y)
}


func (
	v Vector2D,
) Sub(
	other Vector2D,
) (
	Vector2D,
) {
	v.ISub(other)
	return v
}


func (
	v *Vector2D,
) IMul(
	other Vector2D,
) {
	v.X = v.X.Mul(other.X)
	v.Y = v.Y.Mul(other.Y)
}


func (
	v Vector2D,
) Mul(
	other Vector2D,
) (
	Vector2D,
) {
	v.IMul(other)
	return v
}


func (
	v Vector2D,
) Dot(
	other Vector2D,
) (
	Numeric,
) {
	x := v.X.Mul(other.X)
	y := v.Y.Mul(other.Y)
	return x.Add(y)
}


func (
	v Vector2D,
) Cross(
	other Vector2D,
) (
	Numeric,
) {
	a := v.X.Mul(other.Y)
	b := v.Y.Mul(other.X)
	return a.Sub(b)
}