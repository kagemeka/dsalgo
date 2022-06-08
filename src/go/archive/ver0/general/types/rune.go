package types 

import (
	"unicode"
)

/* cut below */



type Rune rune


func (
	x Rune,
) LT(
	other Comparable,
) Bool {
	return x < other.(Rune)
}


func (
	x Rune,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Rune) 
}


func (
	x Rune,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Rune,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}


func (
	x Rune,
) Lower() (
	Rune,
) {
	y := rune(x)
	y = unicode.ToLower(y)
	return Rune(y)
}


func (
	x Rune,
) Upper() (
	Rune,
) {
	y := rune(x)
	y = unicode.ToUpper(y)
	return Rune(y)
}