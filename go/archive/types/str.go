package types

import (
	"strings"
)

/* cut below */



type Str string


func (
	s Str,
) Int() (
	Int,
) {
	i, _ := strconv.Atoi(
		string(s),
	)
	return Int(i)
}


func (
	s Str,
) Sub(
	l, r Int,
) (
	sub Str,
){
	a := s.RuneSlice()
	a = a[l:r]
	sub = a.Str()
	return
}


func (
	s Str,
) RuneSlice() (
	a RuneSlice,
) {
	a = RuneSlice(s)
	return
}


func (
	s Str,
) Contains(
	t Str,
) (
	Bool,
) {
	bl := strings.Contains(
		string(s),
		string(t),
	)
	return Bool(bl)
}


func (
	x Str,
) LT(
	other Comparable,
) Bool {
	return x < other.(Str)
}


func (
	x Str,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Str)
}


func (
	x Str,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Str,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}


func (
	s *Str,
) Reverse() {
	a := s.RuneSlice()
	a.Reverse()
	*s = a.Str()
}


func (
	s Str,
) Reversed() (
	Str,
) {
	s.Reverse()
	return s
}


func (
	s *Str,
) Sort() {
	a := s.RuneSlice()
	a.Sort()
	*s = a.Str()
}


func (
	s Str,
) Sorted() (
	Str,
) {
	s.Sort()
	return s
}


func (
	s Str,
) Lower() (
	Str,
) {
	t := string(s)
	t = strings.ToLower(t)
	return Str(t)
}


func (
	s Str,
) Upper() (
	Str,
) {
	t := string(s)
	t = strings.ToUpper(t)
	return Str(t)
}
