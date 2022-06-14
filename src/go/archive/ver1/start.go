package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
)

type IS []interface{}

func (
	a *IS,
) From(
	b Slice,
) {
	n := b.Len()
	*a = make(IS, n)
	for i := 0; i < n; i++ {
		(*a)[i] = b.Get(i)
	}
	return
}

func (
	a IS,
) Format() (
	format Str,
) {
	n := len(a)
	var v Str = "%v"
	var s Strs
	s = Make(s, v, n).(Strs)
	sep := a.FormatSep()
	format = s.Join(sep)
	return
}

func (
	a IS,
) FormatSep() (
	sep Str,
) {
	n := len(a)
	if n == 0 {
		return
	}
	v := a[0]
	switch v.(type) {
	case Slice:
		sep = "\n"
	default:
		sep = " "
	}
	return
}

func (
	a IS,
) String() string {
	f := string(a.Format())
	return fmt.Sprintf(f, a...)
}

type Bool bool

func (
	b Bool,
) Int() Int {
	if b {
		return 1
	}
	return 0
}

type Bools []Bool

func (
	a Bools,
) Make(
	n int,
) interface{} {
	a = make(Bools, n)
	return a
}

func (
	a Bools,
) Any() (
	ok Bool,
) {
	for _, x := range a {
		if !x {
			continue
		}
		return true
	}
	return
}

func (
	a Bools,
) All() (
	ok Bool,
) {
	for _, x := range a {
		if x {
			continue
		}
		return
	}
	return true
}

type Int int

func (
	x Int,
) Str() Str {
	s := strconv.Itoa(
		int(x),
	)
	return Str(s)
}

func (
	n Int,
) BitLen() (
	l int,
) {
	for n > 0 {
		l++
		n >>= 1
	}
	return
}

func (
	n Int,
) BitCnt() (
	cnt Int,
) {
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}

func (
	x Int,
) Add(
	other interface{},
) (
	res interface{},
) {
	switch y := other.(type) {
	case Int:
		res = x + y
	case Float:
		res = Float(x) + y
	}
	return
}

func (
	x Int,
) AddIdentity() interface{} {
	return Int(0)
}

func (
	x Int,
) AddInv() interface{} {
	return -x
}

func (
	x Int,
) Mul(
	other interface{},
) (
	res interface{},
) {
	switch y := other.(type) {
	case Int:
		res = x * y
	case Float:
		res = Float(x) * y
	}
	return
}

func (
	x Int,
) MulIdentity() (
	e interface{},
) {
	e = Int(1)
	return
}

func (
	x Int,
) MulInv() interface{} {
	return 1 / Float(x)
}

func (
	x Int,
) Pow(
	n int,
) Int {
	return Pow(x, n).(Int)
}

func (
	x Int,
) Divmod(
	rhs Int,
) (
	q Int, r Int,
) {
	q = x / rhs
	r = x % rhs
	if r*rhs >= 0 {
		return
	}
	q--
	r += rhs
	return
}

func (
	x Int,
) LT(
	other interface{},
) bool {
	return x < other.(Int)
}

func (
	n Int,
) Divisors() (
	divs Ints,
) {
	for i := Int(1); i*i <= n; i++ {
		if n%i != 0 {
			continue
		}
		divs.Push(i)
		j := n / i
		if j == i {
			continue
		}
		divs.Push(j)
	}
	sort.Sort(divs)
	return
}

func (
	i Int,
) NxtCmb() (
	j Int,
) {
	x := i & -i
	y := i + x
	j = i & ^y
	j /= x
	j >>= 1
	j |= y
	return
}

func (
	i Int,
) GCD(
	j Int,
) (
	gcd Int,
) {
	if j == 0 {
		gcd = Abs(i).(Int)
		return
	}
	gcd = j.GCD(i % j)
	return
}

func (
	i Int,
) EGCD(
	j Int,
) (
	gcd, x, y Int,
) {
	if j == 0 {
		gcd = Abs(i).(Int)
		x = 1
		y = 0
		return
	}
	q, r := i.Divmod(j)
	gcd, y, x = j.EGCD(r)
	y -= q * x
	return
}

func (
	i Int,
) LCM(
	j Int,
) (
	lcm Int,
) {
	gcd := i.GCD(j)
	lcm = i / gcd * j
	lcm = Abs(lcm).(Int)
	return
}

func (
	x Int,
) AddCommutative() {
}

func (
	x Int,
) MulCommutative() {
}

type Float float64

func (
	x Float,
) Add(
	other interface{},
) (
	res interface{},
) {
	switch y := other.(type) {
	case Int:
		res = x + Float(y)
	case Float:
		res = x + y
	}
	return
}

func (
	x Float,
) AddIdentity() interface{} {
	return Float(0)
}

func (
	x Float,
) AddInv() interface{} {
	return -x
}

func (
	x Float,
) Mul(
	other interface{},
) (
	res interface{},
) {
	switch y := other.(type) {
	case Int:
		res = x * Float(y)
	case Float:
		res = x * y
	}
	return
}

func (
	x Float,
) MulIdentity() (
	e interface{},
) {
	e = Float(1)
	return
}

func (
	x Float,
) MulInv() interface{} {
	return 1 / x
}

func (
	x Float,
) Pow(
	n int,
) Float {
	return Pow(x, n).(Float)
}

func (
	x Float,
) AddCommutative() {
}

func (
	x Float,
) MulCommutative() {
}

func (
	x Float,
) LT(
	other interface{},
) bool {
	return x < other.(Float)
}

type Floats []Float

func (
	a Floats,
) Len() int {
	return len(a)
}

func (
	a Floats,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a *Floats,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Float),
	)
}

func (
	a Floats,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}

type Str string

func (
	s Str,
) Int() Int {
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
) {
	a := Runes(s)
	a = a[l:r]
	sub = a.Str()
	return
}

func (
	s Str,
) Contains(
	t Str,
) Bool {
	bl := strings.Contains(
		string(s),
		string(t),
	)
	return Bool(bl)
}

func (
	x Str,
) LT(
	other interface{},
) bool {
	return x < other.(Str)
}

func (
	s *Str,
) Reverse() {
	a := Runes(*s)
	Reverse(a)
	*s = a.Str()
}

func (
	s *Str,
) Sort() {
	a := Runes(*s)
	sort.Sort(a)
	*s = a.Str()
}

func (
	s Str,
) Lower() Str {
	t := string(s)
	t = strings.ToLower(t)
	return Str(t)
}

func (
	s Str,
) Upper() Str {
	t := string(s)
	t = strings.ToUpper(t)
	return Str(t)
}

type Strs []Str

func (
	a Strs,
) Len() int {
	return len(a)
}

func (
	a Strs,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a Strs,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a Strs,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a Strs,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(Strs)
	a.Push(x)
	return a
}

func (
	a *Strs,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Str),
	)
}

func (
	a Strs,
) Make(
	n int,
) interface{} {
	a = make(Strs, n)
	return a
}

func (
	a Strs,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Str)
}

func (
	s Strs,
) Join(
	sep Str,
) Str {
	t := strings.Join(
		s.Standard(),
		string(sep),
	)
	return Str(t)
}

func (
	a Strs,
) Standard() (
	b []string,
) {
	n := len(a)
	b = make([]string, n)
	for i := 0; i < n; i++ {
		b[i] = string(a[i])
	}
	return
}

func (
	a Strs,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

type Rune rune

func (
	x Rune,
) LT(
	other interface{},
) bool {
	return x < other.(Rune)
}

func (
	x Rune,
) Lower() Rune {
	y := rune(x)
	y = unicode.ToLower(y)
	return Rune(y)
}

func (
	x Rune,
) Upper() Rune {
	y := rune(x)
	y = unicode.ToUpper(y)
	return Rune(y)
}

type Runes []Rune

func (
	a Runes,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a Runes,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a Runes,
) Make(
	n int,
) interface{} {
	a = make(Runes, n)
	return a
}

func (
	a Runes,
) Standard() (
	b []rune,
) {
	n := len(a)
	b = make(
		[]rune,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = rune(a[i])
	}
	return
}

func (
	a Runes,
) Str() Str {
	b := a.Standard()
	return Str(b)
}

func (
	a Runes,
) Len() int {
	return len(a)
}

func (
	a Runes,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}

func (
	a Runes,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a *Runes,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Rune),
	)
}

func (
	a Runes,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(Runes)
	a.Push(x)
	return a
}

func (
	a Runes,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Rune)
}

func (
	a Runes,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

type RuneMatrix []Runes

func (
	a RuneMatrix,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a RuneMatrix,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a RuneMatrix,
) Make(
	n int,
) interface{} {
	a = make(RuneMatrix, n)
	return a
}

func (
	a RuneMatrix,
) Len() int {
	return len(a)
}

func (
	a RuneMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a *RuneMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Runes),
	)
}

func (
	a RuneMatrix,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(RuneMatrix)
	a.Push(x)
	return a
}

func (
	a RuneMatrix,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Runes)
}

func (
	a RuneMatrix,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a RuneMatrix,
) Flatten() (
	b Runes,
) {
	a = Clone(a).(RuneMatrix)
	s := Shape(a)
	n, m := s[0], s[1]
	b = make(Runes, 0, n*m)
	for i := 0; i < n; i++ {
		b = append(b, a[i]...)
	}
	return
}

type AddSemiGroup interface {
	Add(interface{}) interface{}
}

func Add(
	x, y AddSemiGroup,
) (
	res AddSemiGroup,
) {
	res = x.Add(y).(AddSemiGroup)
	return
}

func Sum(
	a ...AddMonoid,
) (
	s AddMonoid,
) {
	s = (s.AddIdentity().(AddMonoid))
	for _, x := range a {
		s = s.Add(x).(AddMonoid)
	}
	return
}

type AddMonoid interface {
	AddSemiGroup
	AddIdentity() interface{}
}

type AddGroup interface {
	AddMonoid
	AddInv() interface{}
}

func Sub(
	x AddGroup,
	other AddGroup,
) (
	res AddGroup,
) {
	y := other.AddInv()
	res = x.Add(y).(AddGroup)
	return
}

type AddAbelianGroup interface {
	AddGroup
	AddCommutative()
}

type MulSemiGroup interface {
	Mul(
		interface{},
	) interface{}
}

func Mul(
	x, y MulSemiGroup,
) (
	res MulSemiGroup,
) {
	res = x.Mul(y).(MulSemiGroup)
	return
}

type MulMonoid interface {
	MulSemiGroup
	MulIdentity() interface{}
}

func Pow(
	x MulMonoid,
	n int,
) (
	y MulMonoid,
) {
	if n == 0 {
		e := x.MulIdentity()
		return e.(MulMonoid)
	}
	y = Pow(x, n>>1)
	y = y.Mul(y).(MulMonoid)
	if n&1 == 1 {
		y = y.Mul(x).(MulMonoid)
	}
	return y
}

type Ring interface {
	AddAbelianGroup
	MulMonoid
}

type MulGroup interface {
	MulMonoid
	MulInv() interface{}
}

func Div(
	x MulGroup,
	other MulGroup,
) (
	res MulGroup,
) {
	y := other.MulInv()
	res = x.Mul(y).(MulGroup)
	return
}

type MulAbelianGroup interface {
	MulGroup
	MulCommutative()
}

type Field interface {
	AddAbelianGroup
	MulAbelianGroup
}

type Real interface {
	Field
	Comparable
}

func Abs(
	x Real,
) Real {
	y := x.AddIdentity().(Real)
	if LE(x, y) {
		return x.AddInv().(Real)
	}
	return x
}

type Comparable interface {
	LT(interface{}) bool
}

func LT(
	x, y Comparable,
) bool {
	return x.LT(y)
}

func LE(
	x, y Comparable,
) bool {
	return LT(x, y) || x == y
}

func GE(
	x, y Comparable,
) bool {
	return !LT(x, y)
}

func GT(
	x, y Comparable,
) bool {
	return !LE(x, y)
}

func Max(
	a ...Comparable,
) (
	mx Comparable,
) {
	mx = a[0]
	for _, x := range a {
		if LE(x, mx) {
			continue
		}
		mx = x
	}
	return
}

func Min(
	a ...Comparable,
) (
	mn Comparable,
) {
	mn = a[0]
	for _, x := range a {
		if GE(x, mn) {
			continue
		}
		mn = x
	}
	return
}

type Slice interface {
	Len() int
	Get(i int) interface{}
	Swap(int, int)
	Pushed(
		interface{},
	) interface{}
	Sub(int, int) interface{}
	Set(
		int,
		interface{},
	)
	Make(
		int,
	) interface{}
}

func Reverse(
	s Slice,
) {
	n := s.Len()
	for i := 0; i < n/2; i++ {
		s.Swap(i, n-i-1)
	}
}

func Make(
	a interface{},
	v interface{},
	shape ...int,
) interface{} {
	var s Slice
	switch x := a.(type) {
	case Slice:
		s = x
	default:
		return v
	}
	n := shape[0]
	s = s.Make(n).(Slice)
	for i := 0; i < n; i++ {
		x := s.Get(i)
		x = Make(
			x,
			v,
			shape[1:]...,
		)
		s.Set(i, x)
	}
	return s
}

func Shape(
	s Slice,
) (
	shape []int,
) {
	n := s.Len()
	shape = append(shape, n)
	if n == 0 {
		return
	}
	switch x := s.Get(0).(type) {
	case Slice:
		shape = append(
			shape,
			Shape(x)...,
		)
	}
	return
}

func Clone(
	a interface{},
) interface{} {
	var s Slice
	switch x := a.(type) {
	case Slice:
		s = x
	default:
		return x
	}
	n := s.Len()
	t := s.Make(n).(Slice)
	for i := 0; i < n; i++ {
		x := s.Get(i)
		x = Clone(x)
		t.Set(i, x)
	}
	return t
}

func Get(
	s Slice,
	indices ...int,
) interface{} {
	i := indices[0]
	x := s.Get(i)
	if len(indices) == 1 {
		return x
	}
	s = x.(Slice)
	x = Get(
		s,
		indices[1:]...,
	)
	return x
}

type TransPose struct {
	S               Slice
	axes            []int
	shape, tgtShape []int
	indices         []int
	axis            int
	x               interface{}
}

func (
	t *TransPose,
) Set(
	s Slice,
) {
	t.S = s
	t.shape = Shape(s)
}

func (
	t *TransPose,
) initIndices() {
	n := len(t.shape)
	indices := make([]int, n)
	for i := 0; i < n; i++ {
		indices[i] = -1
	}
	t.indices = indices
}

func (
	t *TransPose,
) calcTgtShape() {
	axes := t.axes
	shape := t.shape
	n := len(shape)
	tgtShape := make([]int, n)
	for i := 0; i < n; i++ {
		j := axes[i]
		tgtShape[i] = shape[j]
	}
	t.tgtShape = tgtShape
}

func (
	t *TransPose,
) Gen(
	axes ...int,
) Slice {
	t.axes = axes
	t.initIndices()
	t.axis = 0
	t.calcTgtShape()
	t.x = t.S
	t.genSupport()
	return t.x.(Slice)
}

func (
	t *TransPose,
) genSupport() {
	shape := t.tgtShape
	axis := t.axis
	indices := t.indices
	if axis == len(shape) {
		s := t.S
		t.x = Get(s, indices...)
		return
	}
	n := shape[axis]
	srcAxis := t.axes[axis]
	x := t.x.(Slice)
	x = x.Make(n).(Slice)
	for i := 0; i < n; i++ {
		indices[srcAxis] = i
		t.axis = axis + 1
		t.x = x.Get(i)
		t.genSupport()
		x.Set(i, t.x)
	}
	t.x = x
}

func Dot(
	a, b Slice,
) interface{} {
	sA := Shape(a)
	sB := Shape(b)
	dimA := len(sA)
	dimB := len(sB)
	if dimA == 1 && dimB == 1 {
		return dot1D(a, b)
	}
	if dimA == 1 {
		return dot12(a, b)
	}
	return dot2D(a, b)
}

func dot2D(
	a, b Slice,
) interface{} {
	tp := TransPose{}
	tp.Set(b)
	b = tp.Gen(1, 0)
	n := a.Len()
	c := a.Make(n).(Slice)
	for i := 0; i < n; i++ {
		x := a.Get(i).(Slice)
		v := Dot(x, b)
		c.Set(i, v)
	}
	return c
}

func dot12(
	a, b Slice,
) interface{} {
	n := b.Len()
	c := a.Make(n).(Slice)
	for i := 0; i < n; i++ {
		x := b.Get(i).(Slice)
		v := Dot(a, x)
		c.Set(i, v)
	}
	return c
}

func dot1D(
	a, b Slice,
) interface{} {
	n := a.Len()
	c := a.Make(n).(Slice)
	for i := 0; i < n; i++ {
		x := a.Get(i).(Ring)
		y := b.Get(i).(Ring)
		v := x.Mul(y)
		c.Set(i, v)
	}
	c = CumSum(c)
	return c.Get(n - 1)
}

type Permutations struct {
	S  Slice
	Ch chan Slice
	r  int
	i  int
}

func (
	p *Permutations,
) Set(
	s Slice,
) {
	p.S = s
	const bufSize = 1 << 0
	p.Ch = make(
		chan Slice,
		bufSize,
	)
}

func (
	p *Permutations,
) Gen(
	r int,
) {
	p.r = r
	p.i = 0
	p.genSupport()
	close(p.Ch)
}

func (
	p *Permutations,
) genSupport() {
	s := p.S
	r := p.r
	i := p.i
	if i == r {
		var ch chan<- Slice
		ch = p.Ch
		ch <- s.Sub(0, r).(Slice)
		return
	}
	n := s.Len()
	for j := i; j < n; j++ {
		s = Clone(s).(Slice)
		s.Swap(i, j)
		p.S = s
		p.i = i + 1
		p.genSupport()
	}
}

func Permute(
	s Slice,
	r int,
) (
	ch <-chan Slice,
) {
	p := new(Permutations)
	p.Set(s)
	go p.Gen(r)
	ch = p.Ch
	return
}

type Product struct {
	S  Slice
	Ch chan Slice
	r  int
	a  Slice
}

func (
	p *Product,
) Set(
	s Slice,
) {
	p.S = s
	const bufSize = 1 << 0
	p.Ch = make(
		chan Slice,
		bufSize,
	)
	a := Clone(s).(Slice)
	p.a = a.Sub(0, 0).(Slice)
}

func (
	p *Product,
) Gen(
	r int,
) {
	p.r = r
	p.genSupport()
	close(p.Ch)
}

func (
	p *Product,
) genSupport() {
	r := p.r
	a := p.a
	n := a.Len()
	if n == r {
		var ch chan<- Slice
		ch = p.Ch
		ch <- a
		return
	}
	s := p.S
	n = s.Len()
	for i := 0; i < n; i++ {
		b := Clone(a).(Slice)
		x := s.Get(i)
		p.a = b.Pushed(x).(Slice)
		p.genSupport()
	}
}

func Prod(
	s Slice,
	r int,
) (
	ch <-chan Slice,
) {
	p := new(Product)
	p.Set(s)
	go p.Gen(r)
	ch = p.Ch
	return
}

func BisectLeft(
	a Slice,
	x interface{},
) (
	i int,
) {
	n := a.Len()
	f := func(
		i int,
	) bool {
		y := a.Get(i).(Comparable)
		return bool(
			GE(y, x.(Comparable)),
		)
	}
	i = sort.Search(n, f)
	return
}

func BisectRight(
	a Slice,
	x interface{},
) (
	i int,
) {
	n := a.Len()
	f := func(
		i int,
	) bool {
		y := a.Get(i).(Comparable)
		return bool(
			GT(y, x.(Comparable)),
		)
	}
	i = sort.Search(n, f)
	return
}

func LIS(
	a Slice,
	inf interface{},
) (
	lis Slice,
) {
	n := a.Len()
	lis = Make(
		a,
		inf,
		n,
	).(Slice)
	for i := 0; i < n; i++ {
		x := a.Get(i)
		j := BisectLeft(lis, x)
		lis.Set(j, x)
	}
	i := BisectLeft(lis, inf)
	lis = lis.Sub(
		0,
		i,
	).(Slice)
	return
}

func Accumulate(
	a Slice,
	f func(
		x, y interface{},
	) interface{},
) (
	b Slice,
) {
	b = Clone(a).(Slice)
	n := b.Len()
	for i := 0; i < n-1; i++ {
		x := b.Get(i)
		y := b.Get(i + 1)
		b.Set(i+1, f(x, y))
	}
	return
}

func CumMax(
	a Slice,
) (
	b Slice,
) {
	f := func(
		x, y interface{},
	) (
		z interface{},
	) {
		z = Max(
			x.(Comparable),
			y.(Comparable),
		)
		return
	}
	b = Accumulate(a, f)
	return
}

func CumMin(
	a Slice,
) (
	b Slice,
) {
	f := func(
		x, y interface{},
	) (
		z interface{},
	) {
		z = Min(
			x.(Comparable),
			y.(Comparable),
		)
		return
	}
	b = Accumulate(a, f)
	return
}

func CumSum(
	a Slice,
) (
	b Slice,
) {
	f := func(
		x, y interface{},
	) (
		z interface{},
	) {
		z = y.(AddSemiGroup).Add(x)
		return
	}
	b = Accumulate(a, f)
	return
}

func CumProd(
	a Slice,
) (
	b Slice,
) {
	f := func(
		x, y interface{},
	) (
		z interface{},
	) {
		z = y.(MulSemiGroup).Mul(x)
		return
	}
	b = Accumulate(a, f)
	return
}

type Reals []Real

func (
	a Reals,
) Make(
	n int,
) interface{} {
	a = make(Reals, n)
	return a
}

func (
	a Reals,
) Len() int {
	return len(a)
}

func (
	a Reals,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a Reals,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a Reals,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a Reals,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(Reals)
	a.Push(x)
	return a
}

func (
	a *Reals,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Real),
	)
}

func (
	a Reals,
) Ints() (
	b []int,
) {
	n := len(a)
	b = make([]int, n)
	for i := 0; i < n; i++ {
		b[i] = int(a[i].(Int))
	}
	return
}

func (
	a Reals,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a Reals,
) Less(
	i, j int,
) bool {
	return LE(a[i], a[j])
}

func (
	a Reals,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Real)
}

func (
	a Reals,
) Max() Real {
	b := CumMax(a).(Reals)
	n := len(a)
	return b[n-1]
}

func (
	a Reals,
) Min() Real {
	b := CumMin(a).(Reals)
	n := len(a)
	return b[n-1]
}

func (
	a *Reals,
) PopFront() (
	x interface{},
) {
	x = (*a)[0]
	*a = (*a)[1:]
	return
}

func (
	a Reals,
) Sum() (
	s Real,
) {
	s = Int(0)
	n := len(a)
	for i := 0; i < n; i++ {
		s = s.Add(a[i]).(Real)
	}
	return
}

func (
	a Reals,
) Add(
	other interface{},
) interface{} {
	c := Clone(a).(Reals)
	b := other.(Reals)
	n := len(a)
	for i := 0; i < n; i++ {
		x := a[i].Add(b[i]).(Real)
		c[i] = x
	}
	return c
}

func (
	a Reals,
) AddIdentity() interface{} {
	n := len(a)
	b := Make(
		a,
		Int(0),
		n,
	).(Reals)
	return b
}

type Ints []Int

func (
	a Ints,
) Make(
	n int,
) interface{} {
	a = make(Ints, n)
	return a
}

func (
	a Ints,
) Len() int {
	return len(a)
}

func (
	a Ints,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a Ints,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a Ints,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a Ints,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(Ints)
	a.Push(x)
	return a
}

func (
	a *Ints,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Int),
	)
}

func (
	a Ints,
) Standard() (
	b []int,
) {
	n := len(a)
	b = make([]int, n)
	for i := 0; i < n; i++ {
		b[i] = int(a[i])
	}
	return
}

func (
	a Ints,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a Ints,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}

func (
	a Ints,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Int)
}

func (
	a Ints,
) Max() Int {
	b := CumMax(a).(Ints)
	n := len(a)
	return b[n-1]
}

func (
	a Ints,
) Min() Int {
	b := CumMin(a).(Ints)
	n := len(a)
	return b[n-1]
}

func (
	a *Ints,
) PopFront() (
	x Int,
) {
	x = (*a)[0]
	*a = (*a)[1:]
	return
}

func (
	a Ints,
) Add(
	other interface{},
) interface{} {
	c := Clone(a).(Ints)
	b := other.(Ints)
	n := len(a)
	for i := 0; i < n; i++ {
		x := a[i].Add(b[i]).(Int)
		c[i] = x
	}
	return c
}

type IntMatrix []Ints

func (
	a IntMatrix,
) Len() int {
	return len(a)
}

func (
	a IntMatrix,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a IntMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a IntMatrix,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a *IntMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Ints),
	)
}

func (
	a IntMatrix,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(IntMatrix)
	a.Push(x)
	return a
}

func (
	a IntMatrix,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Ints)
}

func (
	a IntMatrix,
) Make(
	n int,
) interface{} {
	a = make(IntMatrix, n)
	return a
}

func (
	a IntMatrix,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a IntMatrix,
) T() IntMatrix {
	tp := TransPose{}
	tp.Set(a)
	a = tp.Gen(1, 0).(IntMatrix)
	return a
}

func (
	a IntMatrix,
) CumSum() IntMatrix {
	a = a.CumSum0()
	a = a.CumSum1()
	return a
}

func (
	a IntMatrix,
) CumSum0() IntMatrix {
	a = CumSum(a).(IntMatrix)
	return a
}

func (
	a IntMatrix,
) CumSum1() IntMatrix {
	a = a.T()
	a = a.CumSum0()
	a = a.T()
	return a
}

func (
	a IntMatrix,
) Mul(
	other interface{},
) interface{} {
	b := other.(IntMatrix)
	return Dot(a, b)
}

func (
	a IntMatrix,
) MulIdentity() interface{} {
	n := len(a)
	e := Make(
		a,
		Int(0),
		n, n,
	).(IntMatrix)
	for i := 0; i < n; i++ {
		e[i][i] = Int(1)
	}
	return e
}

type Bit int

func (
	x Bit,
) Inv() interface{} {
	return ^x
}

func (
	x Bit,
) Add(
	other interface{},
) (
	res interface{},
) {
	y := other.(Bit)
	res = x ^ y
	return
}

func (
	x Bit,
) AddIdentity() interface{} {
	return Bit(0)
}

func (
	x Bit,
) AddInv() interface{} {
	return x
}

func (
	x Bit,
) Mul(
	other interface{},
) (
	res interface{},
) {
	y := other.(Bit)
	res = x & y
	return
}

func (
	x Bit,
) MulIdentity() (
	e interface{},
) {
	e = Bit(^0)
	return
}

type Bits []Bit

type BitMatrix []Bits

func (
	a BitMatrix,
) Len() int {
	return len(a)
}

func (
	a BitMatrix,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a BitMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a BitMatrix,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a *BitMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Bits),
	)
}

func (
	a BitMatrix,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(BitMatrix)
	a.Push(x)
	return a
}

func (
	a BitMatrix,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Bits)
}

func (
	a BitMatrix,
) Make(
	n int,
) interface{} {
	a = make(BitMatrix, n)
	return a
}

func (
	a BitMatrix,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a BitMatrix,
) T() BitMatrix {
	tp := TransPose{}
	tp.Set(a)
	a = tp.Gen(1, 0).(BitMatrix)
	return a
}

func (
	a BitMatrix,
) Mul(
	other interface{},
) interface{} {
	b := other.(BitMatrix)
	return Dot(a, b)
}

func (
	a BitMatrix,
) MulIdentity() interface{} {
	n := len(a)
	e := Make(
		a,
		Bit(0),
		n, n,
	).(BitMatrix)
	for i := 0; i < n; i++ {
		e[i][i] = Bit(1)
	}
	return e
}

type Vector2D struct {
	X, Y Real
}

func (
	v Vector2D,
) Norm() (
	norm Real,
) {
	norm = Root(
		v.SqNorm(),
		2,
	)
	return
}

func (
	v Vector2D,
) SqNorm() Real {
	x2 := Pow(v.X, 2).(Real)
	y2 := Pow(v.Y, 2).(Real)
	return x2.Add(y2).(Real)
}

func (
	v Vector2D,
) Add(
	other interface{},
) interface{} {
	y := other.(Vector2D)
	v.X = v.X.Add(y.X).(Real)
	v.Y = v.Y.Add(y.Y).(Real)
	return v
}

func (
	v Vector2D,
) AddIdentity() interface{} {
	x := Float(0)
	v = Vector2D{x, x}
	return v
}

func (
	v Vector2D,
) AddInv() interface{} {
	v = Vector2D{
		v.X.AddInv().(Real),
		v.Y.AddInv().(Real),
	}
	return v
}

func (
	v Vector2D,
) Times(
	c Real,
) Vector2D {
	v.X = v.X.Mul(c).(Real)
	v.Y = v.Y.Mul(c).(Real)
	return v
}

func (
	v Vector2D,
) Dot(
	other Vector2D,
) Real {
	x := v.X.Mul(other.X).(Real)
	y := v.Y.Mul(other.Y).(Real)
	return x.Add(y).(Real)
}

func (
	v Vector2D,
) Cross(
	other Vector2D,
) Real {
	a := v.X.Mul(other.Y).(Real)
	b := v.Y.Mul(other.X).(Real)
	return Sub(a, b).(Real)
}

func (
	v Vector2D,
) Arg() Float {
	v = Sub(
		v,
		v.AddIdentity().(Vector2D),
	).(Vector2D)
	x := v.X.(Float)
	y := v.Y.(Float)
	th := math.Atan2(
		float64(y),
		float64(x),
	)
	return Float(th)
}

func (
	v Vector2D,
) CW(
	other Vector2D,
) (
	ok bool,
) {
	c := v.Cross(other)
	ok = LT(
		c,
		c.AddIdentity().(Real),
	)
	return
}

func (
	v Vector2D,
) Parallel(
	other Vector2D,
) (
	ok bool,
) {
	c := v.Cross(other)
	zero := c.AddIdentity()
	ok = c == zero
	return
}

func (
	v Vector2D,
) CCW(
	other Vector2D,
) (
	ok bool,
) {
	c := v.Cross(other)
	ok = GT(
		c,
		c.AddIdentity().(Real),
	)
	return
}

func (
	v Vector2D,
) Inner(
	other Vector2D,
) (
	ok bool,
) {
	d := v.Dot(other)
	zero := d.AddIdentity()
	ok = GT(
		d,
		zero.(Real),
	)
	return
}

func (
	v Vector2D,
) Perpendicular(
	other Vector2D,
) (
	ok bool,
) {
	d := v.Dot(other)
	zero := d.AddIdentity()
	ok = d == zero
	return
}

func (
	v Vector2D,
) Outer(
	other Vector2D,
) (
	ok bool,
) {
	d := v.Dot(other)
	zero := d.AddIdentity()
	ok = LT(
		d,
		zero.(Real),
	)
	return
}

func (
	v Vector2D,
) Acute(
	other Vector2D,
) (
	ok bool,
) {
	ok = v.CCW(
		other,
	) && v.Inner(
		other,
	)
	return
}

func (
	v Vector2D,
) Right(
	other Vector2D,
) (
	ok bool,
) {
	ok = v.Perpendicular(
		other,
	) && v.CCW(
		other,
	)
	return
}

func (
	v Vector2D,
) Obtuse(
	other Vector2D,
) (
	ok bool,
) {
	ok = v.CCW(
		other,
	) && v.Outer(
		other,
	)
	return
}

func (
	v Vector2D,
) SameDir(
	other Vector2D,
) (
	ok bool,
) {
	ok = v.Parallel(
		other,
	) && v.Inner(
		other,
	)
	return
}

func (
	v Vector2D,
) OppositeDir(
	other Vector2D,
) (
	ok bool,
) {
	ok = v.Parallel(
		other,
	) && v.Outer(
		other,
	)
	return
}

type Triangle2D struct {
	V0, V1, V2 Vector2D
}

func (
	t Triangle2D,
) SignedArea() (
	area Float,
) {
	v1 := Sub(
		t.V1,
		t.V0,
	).(Vector2D)
	v2 := Sub(
		t.V2,
		t.V0,
	).(Vector2D)
	cross := v1.Cross(v2)
	switch v := cross.(type) {
	case Int:
		area = Float(v) / 2
	case Float:
		area = v / 2
	}
	return
}

func (
	t Triangle2D,
) Area() Float {
	s := t.SignedArea()
	return Abs(s).(Float)
}

type LineSegment2D struct {
	V0, V1 Vector2D
}

func (
	s LineSegment2D,
) Intersect(
	other LineSegment2D,
) (
	ok Bool,
) {
	bl0 := s.Across(other)
	bl1 := other.Across(s)
	ok = bl0 && bl1
	return
}

func (
	s LineSegment2D,
) Across(
	other LineSegment2D,
) (
	ok Bool,
) {
	o0 := other.Orientation(
		s.V0,
	)
	o1 := other.Orientation(
		s.V1,
	)
	ok = o0*o1 <= 0
	return
}

func (
	s LineSegment2D,
) Orientation(
	v Vector2D,
) (
	o Int,
) {
	t := Triangle2D{
		s.V0,
		s.V1,
		v,
	}
	a := t.SignedArea()
	if a < 0 {
		return -1
	}
	if a == 0 {
		return 0
	}
	if a > 0 {
		return 1
	}
	return
}

type Modular struct {
	Value int
	Mod   int
}

func (
	m *Modular,
) Init() {
	mod := m.Mod
	v := m.Value
	v %= mod
	v += mod
	v %= mod
	m.Value = v
}

func (
	m Modular,
) String() string {
	return fmt.Sprint(m.Value)
}

func (
	m *Modular,
) Clone() Modular {
	return Modular(*m)
}

func (
	x Modular,
) Add(
	other interface{},
) interface{} {
	y := other.(Modular)
	x.Value += y.Value
	x.Init()
	return x
}

func (
	x Modular,
) AddIdentity() interface{} {
	mod := x.Mod
	return Modular{0, mod}
}

func (
	m Modular,
) AddInv() interface{} {
	m = Modular{
		Value: -m.Value,
		Mod:   m.Mod,
	}
	m.Init()
	return m
}

func (
	x Modular,
) Mul(
	other interface{},
) interface{} {
	y := other.(Modular)
	x.Value *= y.Value
	x.Init()
	return x
}

func (
	x Modular,
) MulIdentity() interface{} {
	mod := x.Mod
	return Modular{1, mod}
}

func (
	x Modular,
) MulInv() interface{} {
	n := int(x.Mod) - 2
	return x.Pow(n)
}

func (
	m Modular,
) Pow(n int) Modular {
	return Pow(m, n).(Modular)
}

func (
	m Modular,
) Factorial() (
	fact Mods,
) {
	n, mod := m.Value, m.Mod
	fact = make(Mods, n)
	for i := 0; i < n; i++ {
		fact[i] = Modular{i, mod}
	}
	fact[0] = Modular{1, mod}
	fact = CumProd(fact).(Mods)
	return
}

func (
	m Modular,
) InvFactorial() (
	iFact Mods,
) {
	n, mod := m.Value, m.Mod
	fact := m.Factorial()
	iFact = make(Mods, n)
	for i := 0; i < n; i++ {
		iFact[i] = Modular{
			n - i,
			mod,
		}
	}
	x := fact[n-1].MulInv()
	iFact[0] = x.(Modular)
	iFact = CumProd(iFact).(Mods)
	Reverse(iFact)
	return
}

func (
	x Modular,
) AddCommutative() {
}

func (
	x Modular,
) MulCommutative() {
}

type Mods []Modular

func (
	a Mods,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a Mods,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Modular)
}

func (
	a Mods,
) Make(
	n int,
) interface{} {
	a = make(Mods, n)
	return a
}

func (
	a Mods,
) Len() int {
	return len(a)
}

func (
	a Mods,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a Mods,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a *Mods,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Modular),
	)
}

func (
	a Mods,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(Mods)
	a.Push(x)
	return a
}

type ModMatrix []Mods

func (
	a ModMatrix,
) Len() int {
	return len(a)
}

func (
	a ModMatrix,
) Get(
	i int,
) interface{} {
	return a[i]
}

func (
	a ModMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a ModMatrix,
) Sub(
	i, j int,
) interface{} {
	return a[i:j]
}

func (
	a *ModMatrix,
) Push(
	x interface{},
) {
	*a = append(
		*a,
		x.(Mods),
	)
}

func (
	a ModMatrix,
) Pushed(
	x interface{},
) interface{} {
	a = Clone(a).(ModMatrix)
	a.Push(x)
	return a
}

func (
	a ModMatrix,
) Set(
	i int,
	x interface{},
) {
	a[i] = x.(Mods)
}

func (
	a ModMatrix,
) Make(
	n int,
) interface{} {
	a = make(ModMatrix, n)
	return a
}

func (
	a ModMatrix,
) String() string {
	var s IS
	s.From(a)
	return s.String()
}

func (
	a ModMatrix,
) T() ModMatrix {
	tp := TransPose{}
	tp.Set(a)
	a = tp.Gen(1, 0).(ModMatrix)
	return a
}

func (
	a ModMatrix,
) Mul(
	other interface{},
) interface{} {
	b := other.(ModMatrix)
	return Dot(a, b)
}

func (
	a ModMatrix,
) MulIdentity() interface{} {
	n := len(a)
	mod := a[0][0].Mod
	e := Make(
		a,
		Modular{0, mod},
		n, n,
	).(ModMatrix)
	for i := 0; i < n; i++ {
		e[i][i] = Modular{1, mod}
	}
	return e
}

type ModChoose struct {
	Fact, InvFact Mods
	Mod           int
}

func (
	c *ModChoose,
) Init(n Modular) {
	c.Fact, c.InvFact =
		n.Factorial(),
		n.InvFactorial()
	c.Mod = n.Mod
}

func (
	c *ModChoose,
) Calc(n, r Int) Modular {
	if r < 0 || r > n {
		return Modular{0, c.Mod}
	}
	v := c.Fact[n]
	v = v.Mul(
		c.InvFact[r],
	).(Modular)
	v = v.Mul(
		c.InvFact[n-r],
	).(Modular)
	return v
}

func (
	c *ModChoose,
) Calculator() (
	choose func(
		n, r Int,
	) Modular,

) {
	return c.Calc
}

type PII [2]int

type Binom map[PII]Modular

type Choose struct {
	cache Binom
	mod   int
}

func (
	c *Choose,
) Init(
	mod int,
) {
	c.cache = make(Binom)
	c.mod = mod
}

func (
	c *Choose,
) Calc(
	n, r int,
) (
	v Modular,
) {
	mod := c.mod
	if r > n || r < 0 {
		return Modular{0, mod}
	}
	if r == 0 {
		return Modular{1, mod}
	}
	i := PII{n, r}
	cache := c.cache
	if v, ok := cache[i]; ok {
		return v
	}
	v = c.Calc(n-1, r)
	v = v.Add(
		c.Calc(n-1, r-1),
	).(Modular)
	cache[i] = v
	return
}

func (
	c *Choose,
) Calculator() func(
	n, r int,
) Modular {
	return c.Calc
}

type NChoose struct {
	Values Mods
}

func (
	c *NChoose,
) Init(
	n int,
	r Modular,
) {
	ifac := r.InvFactorial()
	l := len(ifac)
	mod := r.Mod
	nChoose := Make(
		c.Values,
		Modular{1, mod},
		int(l),
	).(Mods)
	for i := 0; i < l-1; i++ {
		x := Modular{n - i, mod}
		x = nChoose[i].Mul(
			x,
		).(Modular)
		nChoose[i+1] = x
	}
	for i := 0; i < l; i++ {
		x := nChoose[i].Mul(
			ifac[i],
		).(Modular)
		nChoose[i] = x
	}
	c.Values = nChoose
}

func (
	c *NChoose,
) Get(
	i Int,
) (
	v Modular,
) {
	v = c.Values[i]
	return
}

type DisjointSet struct {
	Parent Ints
	Rank   Ints
	Size   Ints
}

func (
	ds *DisjointSet,
) Init(
	n Int,
) {
	parent := make(Ints, n)
	for i := Int(0); i < n; i++ {
		parent[i] = i
	}
	rank := ds.Rank.Make(
		int(n),
	).(Ints)
	size := Make(
		new(Ints),
		Int(1),
		int(n),
	).(Ints)
	ds.Parent = parent
	ds.Rank = rank
	ds.Size = size
}

func (
	ds *DisjointSet,
) Find(
	u Int,
) (
	root Int,
) {
	parent := ds.Parent
	v := parent[u]
	if v == u {
		root = u
		return
	}
	root = ds.Find(v)
	parent[u] = root
	return
}

func (
	ds *DisjointSet,
) Unite(
	u, v Int,
) {
	u = ds.Find(u)
	v = ds.Find(v)
	if u == v {
		return
	}
	u, v = ds.sort(u, v)
	rank := ds.Rank
	parent := ds.Parent
	size := ds.Size
	parent[v] = u
	size[u] += size[v]
	rank[u] = Max(
		rank[u],
		rank[v]+1,
	).(Int)
}

func (
	ds *DisjointSet,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	rank := ds.Rank
	if rank[u] < rank[v] {
		u, v = v, u
	}
	return u, v
}

func (
	ds *DisjointSet,
) Same(
	u, v Int,
) Bool {
	u = ds.Find(u)
	v = ds.Find(v)
	return u == v
}

type PrimeNum struct {
	Values  Ints
	IsPrime Bools
	n, i    Int
}

func (
	pn *PrimeNum,
) Init(
	n Int,
) {
	pn.n = n
	pn.SieveOfEratosthenes()
	pn.Sparse()
}

func (
	pn *PrimeNum,
) SieveOfEratosthenes() {
	n := pn.n
	isPrime := Make(
		new(Bools),
		Bool(true),
		int(n),
	).(Bools)
	isPrime[0] = false
	isPrime[1] = false
	pn.IsPrime = isPrime
	for i := Int(0); i*i < n; i++ {
		if !isPrime[i] {
			continue
		}
		pn.i = i
		pn.sieveSupport()
	}
}

func (
	pn *PrimeNum,
) sieveSupport() {
	n, i := pn.n, pn.i
	isPrime := pn.IsPrime
	for j := Int(i * 2); j < n; j += i {
		isPrime[j] = false
	}
}

func (
	pn *PrimeNum,
) Sparse() {
	primeNums := make(Ints, 0)
	isPrime := pn.IsPrime
	for i, ok := range isPrime {
		if !ok {
			continue
		}
		primeNums = append(
			primeNums,
			Int(i),
		)
	}
	pn.Values = primeNums
}

func (
	pn *PrimeNum,
) Get(
	i int,
) (
	v Int,
) {
	v = pn.Values[i]
	return
}

type MII map[Int]Int

type Factorization struct {
	primeNums         Ints
	n, p              Int
	factors, fFactors MII
}

func (
	f *Factorization,
) Init(
	n Int,
) {
	pn := new(PrimeNum)
	pn.Init(n)
	f.primeNums = pn.Values
}

func (
	f *Factorization,
) Calc(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.factors = factors
	primeNums := f.primeNums
	for _, p := range primeNums {
		if n < 2 {
			return
		}
		if p*p > n {
			break
		}
		f.n, f.p = n, p
		f.calcSupport()
		n = f.n
	}
	factors[n]++
	return
}

func (
	f *Factorization,
) calcSupport() {
	n, p := f.n, f.p
	factors := f.factors
	for n%p == 0 {
		factors[p]++
		n /= p
	}
	f.n = n
}

func (
	f *Factorization,
) Factorial(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.fFactors = factors
	for i := Int(1); i < n+1; i++ {
		f.n = i
		f.factorialSupport()
	}
	return
}

func (
	f *Factorization,
) factorialSupport() {
	n := f.n
	factors := f.fFactors
	for p, c := range f.Calc(n) {
		factors[p] += c
	}
}

func Root(
	x Real,
	n int,
) (
	root Real,
) {
	y0 := x
	var f NewtonFunc
	f = func(
		x Real,
	) Real {
		y := Pow(x, n).(Real)
		return Sub(y, y0).(Real)
	}
	const x0 = Float(1e13)
	root = f.Newton(x0)
	return
}

type NewtonFunc func(
	x Real,
) Real

func (
	f NewtonFunc,
) Derivative(
	x Real,
) (
	d Real,
) {
	const dx = Float(1)
	y1 := f(Add(x, dx).(Real))
	y0 := f(x)
	dy := Sub(y1, y0).(Real)
	d = Div(dy, dx).(Real)
	return
}

func (
	f NewtonFunc,
) Newton(
	x0 Real,
) (
	x Real,
) {
	x = x0
	const maxIter = 1 << 7
	const eps = Float(1e-9)
	for i := 0; i < maxIter; i++ {
		y := f(x)
		der := f.Derivative(x)
		dx := Div(y, der).(Real)
		x = Sub(x, dx).(Real)
		if LE(Abs(dx), eps) {
			break
		}
	}
	return
}

type Rectangle2D struct {
	V0, V1 Vector2D
}

type Polygon2D []Vector2D

func (
	p *Polygon2D,
) Push(
	x interface{},
) {
	*p = append(
		*p,
		x.(Vector2D),
	)
}

func (
	p Polygon2D,
) Len() int {
	return len(p)
}

func (
	p Polygon2D,
) Less(
	i, j int,
) (
	ok bool,
) {
	v1, v2 := p[i], p[j]
	ok = LE(
		v1.Arg(),
		v2.Arg(),
	)
	return
}

func (
	p Polygon2D,
) Swap(
	i, j int,
) {
	p[i], p[j] = p[j], p[i]
}

type Node struct {
	ID Int
}

func (
	v Node,
) String() string {
	return fmt.Sprint(v.ID)
}

type NodeSlice []Node

type Edge struct {
	ID       Int
	From, To Int
	Weight   Int
	Capacity Int
}

type EdgeSlice []Edge

func (
	edges *EdgeSlice,
) Push(
	e interface{},
) {
	*edges = append(
		*edges,
		e.(Edge),
	)
}

type EdgeMatrix []EdgeSlice

type Graph struct {
	Nodes NodeSlice
	Edges EdgeMatrix
}

func (
	g *Graph,
) Init(n Int) {
	nodes := make(NodeSlice, n)
	edges := make(EdgeMatrix, n)
	for i := Int(0); i < n; i++ {
		e := make(
			EdgeSlice,
			0,
		)
		edges[i] = e
	}
	g.Nodes = nodes
	g.Edges = edges
}

func (
	g *Graph,
) AddEdge(e Edge) {
	u := e.From
	g.Edges[u].Push(e)
}

func (
	g *Graph,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}

func (
	g *Graph,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v
}

func (
	g *Graph,
) Size() (
	n int,
) {
	n = len(g.Nodes)
	return
}

type Tree Graph

func (
	g *Tree,
) Init(n Int) {
	nodes := make(NodeSlice, n)
	edges := make(EdgeMatrix, n)
	for i := Int(0); i < n; i++ {
		e := make(
			EdgeSlice,
			0,
		)
		edges[i] = e
	}
	g.Nodes = nodes
	g.Edges = edges
}

func (
	g *Tree,
) AddEdge(e Edge) {
	u := e.From
	g.Edges[u].Push(e)
}

func (
	g *Tree,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}

func (
	g *Tree,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v
}

func (
	g *Tree,
) Size() (
	n int,
) {
	n = len(g.Nodes)
	return
}

type GraphBFS struct {
	G     Graph
	Level Ints
	Que   Ints
}

func (
	bfs *GraphBFS,
) SetGraph(
	g Graph,
) {
	bfs.G = g
}

func (
	bfs *GraphBFS,
) Prepare(
	src Int,
) {
	n := bfs.G.Size()
	level := Make(
		new(Ints),
		Int(-1),
		n,
	).(Ints)
	level[src] = 0
	que := make(Ints, 0)
	que.Push(src)
	bfs.Level = level
	bfs.Que = que
}

func (
	bfs *GraphBFS,
) Search() {
	que := &bfs.Que
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}

func (
	bfs *GraphBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	lv := &bfs.Level
	for _, e := range g.Edges[u] {
		v := e.To
		if (*lv)[v] != -1 {
			continue
		}
		(*lv)[v] = (*lv)[u] + 1
		que.Push(v)
	}
}

type TreeBFS struct {
	G      Tree
	Root   Int
	Depth  Ints
	Dist   Ints
	Parent Ints
	Que    Ints
}

func (
	bfs *TreeBFS,
) SetGraph(
	g Tree,
) {
	bfs.G = g
}

func (
	bfs *TreeBFS,
) Prepare(
	root Int,
) {
	n := bfs.G.Size()
	depth := Make(
		new(Ints),
		Int(-1),
		n,
	).(Ints)
	depth[root] = 0
	dist := Make(
		new(Ints),
		Int(-1),
		n,
	).(Ints)
	dist[root] = 0
	parent := Make(
		new(Ints),
		Int(-1),
		n,
	).(Ints)
	parent[root] = root
	que := make(
		Ints,
		0,
	)
	que.Push(root)
	bfs.Depth = depth
	bfs.Dist = dist
	bfs.Parent = parent
	bfs.Que = que
}

func (
	bfs *TreeBFS,
) Search() {
	que := &bfs.Que
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}

func (
	bfs *TreeBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	depth := bfs.Depth
	dist := bfs.Dist
	parent := bfs.Parent
	for _, e := range g.Edges[u] {
		v := e.To
		d := e.Weight
		if depth[v] != -1 {
			continue
		}
		depth[v] = depth[u] + 1
		dist[v] = dist[u] + d
		parent[v] = u
		que.Push(v)
	}
}

type DijkstraItem struct {
	Node Int
	Dist Int
}

func (
	x DijkstraItem,
) LT(
	other interface{},
) bool {
	y := other.(DijkstraItem)
	return x.Dist < y.Dist
}

type DijkstraHeap []DijkstraItem

func (
	h DijkstraHeap,
) Len() int {
	return len(h)
}

func (
	h DijkstraHeap,
) Less(
	i, j int,
) bool {
	return h[i].LT(h[j])
}

func (
	h DijkstraHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}

func (
	h *DijkstraHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h,
		x.(DijkstraItem),
	)
}

func (
	h *DijkstraHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}

type Dijkstra struct {
	G           Graph
	Heap        DijkstraHeap
	Dist        Ints
	Paths       Mods
	Predecessor IntMatrix
	src         Int
	inf         Int
	mod         int
	x           DijkstraItem
	e           Edge
}

func (
	di *Dijkstra,
) SetGraph(
	g Graph,
) {
	di.G = g
}

func (
	di *Dijkstra,
) Prepare(
	src Int,
	inf Int,
	mod int,
) {
	di.src = src
	di.inf = inf
	di.mod = mod
	di.InitDist()
	di.InitHeap()
	di.InitPaths()
	di.InitPredecessor()
}

func (
	di *Dijkstra,
) InitHeap() {
	src := di.src
	dist := di.Dist
	h := DijkstraHeap{}
	heap.Init(&h)
	x := DijkstraItem{
		Node: src,
		Dist: dist[src],
	}
	heap.Push(&h, x)
	di.Heap = h
}

func (
	di *Dijkstra,
) InitDist() {
	n := di.G.Size()
	src := di.src
	inf := di.inf
	dist := Make(
		new(Ints),
		inf,
		n,
	).(Ints)
	dist[src] = 0
	di.Dist = dist
}

func (
	di *Dijkstra,
) InitPaths() {
	n := di.G.Size()
	src := di.src
	mod := di.mod
	paths := Make(
		new(Mods),
		Modular{0, mod},
		n,
	).(Mods)
	paths[src] = Modular{1, mod}
	di.Paths = paths
}

func (
	di *Dijkstra,
) InitPredecessor() {
	n := di.G.Size()
	pred := Make(
		new(IntMatrix),
		Int(0),
		n, 0,
	).(IntMatrix)
	di.Predecessor = pred
}

func (
	di *Dijkstra,
) Search() {
	h := &di.Heap
	for h.Len() > 0 {
		di.Open()
		if di.Searched() {
			continue
		}
		di.Explore()
	}
}

func (
	di *Dijkstra,
) Open() {
	h := &di.Heap
	x := (heap.Pop(h).(DijkstraItem))
	di.x = x
}

func (
	di *Dijkstra,
) Searched() Bool {
	x := di.x
	i, d := x.Node, x.Dist
	return d > di.Dist[i]
}

func (
	di *Dijkstra,
) Explore() {
	u := di.x.Node
	edges := di.G.Edges
	for _, e := range edges[u] {
		di.e = e
		di.exploreSupport()
	}
}

func (
	di *Dijkstra,
) exploreSupport() {
	x := di.x
	u, d := x.Node, x.Dist
	e := di.e
	v := e.To
	d += e.Weight
	dist := di.Dist
	paths := di.Paths
	pred := di.Predecessor
	if d > dist[v] {
		return
	}
	if d == dist[v] {
		pred[v].Push(u)
		paths[v] = paths[v].Add(
			paths[u],
		).(Modular)
		return
	}
	pred[v] = Ints{u}
	paths[v] = paths[u]
	dist[v] = d
	x = DijkstraItem{
		Node: v,
		Dist: d,
	}
	heap.Push(&di.Heap, x)
}

type AStarItem struct {
	Node    Int
	C, H, S Int
	Dist    Int
}

func (
	x AStarItem,
) LT(
	other AStarItem,
) bool {
	if x.S != other.S {
		return x.S < other.S
	}
	return x.H < other.H
}

type AStarHeap []AStarItem

func (
	h AStarHeap,
) Len() int {
	return len(h)
}

func (
	h AStarHeap,
) Less(
	i, j int,
) bool {
	return h[i].LT(h[j])
}

func (
	h AStarHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}

func (
	h *AStarHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h,
		x.(AStarItem),
	)
}

func (
	h *AStarHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}

type HeuristicFunc func(
	Int,
) Int

type AStar struct {
	G        Graph
	Heap     AStarHeap
	Cost     Ints
	F        HeuristicFunc
	src, dst Int
	inf      Int
	x        AStarItem
	e        Edge
}

func (
	a *AStar,
) SetGraph(
	g Graph,
) {
	a.G = g
}

func (
	a *AStar,
) SetHeuristicFunc(
	f HeuristicFunc,
) {
	a.F = f
}

func (
	a *AStar,
) Prepare(
	src Int,
	dst Int,
	inf Int,
) {
	a.src, a.dst = src, dst
	a.inf = inf
	a.InitCost()
	a.InitHeap()
}

func (
	a *AStar,
) InitCost() {
	n := a.G.Size()
	src := a.src
	inf := a.inf
	cost := Make(
		new(Ints),
		inf,
		n,
	).(Ints)
	cost[src] = 0
	a.Cost = cost
}

func (
	a *AStar,
) InitHeap() {
	cost := a.Cost
	src := a.src
	h := AStarHeap{}
	heap.Init(&h)
	c := cost[src]
	hc := a.F(src)
	s := c + hc
	x := AStarItem{
		Node: src,
		C:    c,
		H:    hc,
		S:    s,
	}
	heap.Push(&h, x)
	a.Heap = h
}

func (
	a *AStar,
) Search() {
	h := &a.Heap
	for h.Len() > 0 {
		a.Open()
		if a.isDst() {
			return
		}
		if a.Searched() {
			continue
		}
		a.Explore()
	}
}

func (
	a *AStar,
) Open() {
	h := &a.Heap
	x := (heap.Pop(h).(AStarItem))
	a.x = x
}

func (
	a *AStar,
) isDst() Bool {
	x := a.x
	i := x.Node
	return i == a.dst
}

func (
	a *AStar,
) Searched() Bool {
	x := a.x
	i, c := x.Node, x.C
	return c > a.Cost[i]
}

func (
	a *AStar,
) Explore() {
	u := a.x.Node
	edges := a.G.Edges
	for _, e := range edges[u] {
		a.e = e
		a.exploreSupport()
	}
}

func (
	a *AStar,
) exploreSupport() {
	c := a.x.C
	e := a.e
	v := e.To
	c += e.Weight
	cost := a.Cost
	if c >= cost[v] {
		return
	}
	cost[v] = c
	h := a.F(c)
	s := c + h
	x := AStarItem{
		Node: v,
		C:    c,
		H:    h,
		S:    s,
	}
	heap.Push(&a.Heap, x)
}

type FloydWarshall struct {
	G             Graph
	Dist          IntMatrix
	src, mid, dst int
}

func (
	fw *FloydWarshall,
) SetGraph(
	g Graph,
) {
	fw.G = g
}

func (
	fw *FloydWarshall,
) Prepare(
	inf Int,
) {
	n := fw.G.Size()
	dist := Make(
		new(IntMatrix),
		inf,
		n, n,
	).(IntMatrix)
	fw.Dist = dist
	for i := 0; i < n; i++ {
		fw.prepareSupport(i)
	}
	for i := 0; i < n; i++ {
		dist[i][i] = 0
	}
}

func (
	fw *FloydWarshall,
) prepareSupport(
	i int,
) {
	g := &fw.G
	dist := fw.Dist
	for _, e := range g.Edges[i] {
		j := e.To
		d := e.Weight
		dist[i][j] = Min(
			dist[i][j],
			d,
		).(Int)
	}
}

func (
	fw *FloydWarshall,
) Search() {
	n := len(fw.Dist)
	for k := 0; k < n; k++ {
		fw.mid = k
		fw.searchSupport0()
	}
}

func (
	fw *FloydWarshall,
) searchSupport0() {
	n := len(fw.Dist)
	for i := 0; i < n; i++ {
		fw.src = i
		fw.searchSupport1()
	}
}

func (
	fw *FloydWarshall,
) searchSupport1() {
	n := len(fw.Dist)
	k, i := fw.mid, fw.src
	d := fw.Dist
	for j := 0; j < n; j++ {
		d[i][j] = Min(
			d[i][j],
			d[i][k]+d[k][j],
		).(Int)
	}
}

type Dinic struct {
	G          Graph
	Level      Ints
	Src, Sink  Int
	u          Int
	e          Edge
	in, out, f Int
}

func (
	di *Dinic,
) SetGraph(
	g Graph,
) {
	di.G = g
}

func (
	di *Dinic,
) Prepare(
	Src, Sink Int,
) {
	di.Src = Src
	di.Sink = Sink
}

func (
	di *Dinic,
) Search() (
	flow Int,
) {
	sink := di.Sink
	src := di.Src
	const inf = 1 << 60
	di.in = inf
	for {
		di.updateLevel()
		if di.Level[sink] == -1 {
			return
		}
		di.u = src
		di.out = 0
		di.flowToSink()
		flow += di.out
	}
}

func (
	di *Dinic,
) updateLevel() {
	bfs := GraphBFS{}
	bfs.SetGraph(di.G)
	bfs.Prepare(di.Src)
	bfs.Search()
	di.Level = bfs.Level
}

func (
	di *Dinic,
) flowToSink() {
	u := di.u
	if u == di.Sink {
		di.out = di.in
		return
	}
	g := &di.G
	edges := g.Edges[u]
	g.Edges[u] = make(
		EdgeSlice,
		0,
		len(edges),
	)
	for _, e := range edges {
		di.e = e
		di.flowToSinkSupport()
	}
}

func (
	di *Dinic,
) flowToSinkSupport() {
	if !di.checkLevel() {
		return
	}
	di.calcSuccrFlow()
	di.updateEdges()
	di.updateFlow()
}

func (
	di *Dinic,
) updateFlow() {
	di.out += di.f
}

func (
	di *Dinic,
) updateEdges() {
	f := di.f
	e := di.e
	v := e.To
	e.Capacity -= f
	if e.Capacity > 0 {
		di.G.AddEdge(e)
	}
	if f == 0 {
		return
	}
	u := di.u
	e = Edge{
		From:     v,
		To:       u,
		Capacity: f,
	}
	di.G.AddEdge(e)
}

func (
	di *Dinic,
) calcSuccrFlow() {
	u := di.u
	e := di.e
	in := di.in
	out := di.out
	di.u = e.To
	di.in = Min(
		in-out,
		e.Capacity,
	).(Int)
	di.out = 0
	di.flowToSink()
	di.f = di.out
	di.u = u
	di.e = e
	di.in = in
	di.out = out
}

func (
	di *Dinic,
) checkLevel() (
	ok Bool,
) {
	lv := di.Level
	u := di.u
	e := di.e
	v := e.To
	if lv[v] > lv[u] {
		ok = true
		return
	}
	di.G.AddEdge(e)
	return
}

type LCA struct {
	G         Tree
	Parent    Ints
	Ancestors IntMatrix
	Dist      Ints
	Depth     Ints
}

func (
	l *LCA,
) SetTree(
	g Tree,
) {
	l.G = g
}

func (
	l *LCA,
) Prepare(
	root Int,
) {
	bfs := TreeBFS{}
	bfs.SetGraph(l.G)
	bfs.Prepare(root)
	bfs.Search()
	l.Parent = bfs.Parent
	l.Depth = bfs.Depth
	l.Dist = bfs.Dist
}

func (
	l *LCA,
) FindAncestors() {
	n := len(l.G.Nodes)
	ancestors := l.Ancestors
	m := l.Depth.Max().BitLen()
	ancestors = Make(
		ancestors,
		Int(-1),
		m, n,
	).(IntMatrix)
	ancestors[0] = l.Parent
	l.Ancestors = ancestors
	for i := 0; i < m-1; i++ {
		l.nxtAncestor(i)
	}
}

func (
	l *LCA,
) nxtAncestor(
	i int,
) {
	n := Int(len(l.G.Nodes))
	x := l.Ancestors[i]
	y := make(Ints, n)
	for i := Int(0); i < n; i++ {
		y[i] = x[x[i]]
	}
	l.Ancestors[i+1] = y
}

func (
	l *LCA,
) FindDist(
	u, v Int,
) (
	d Int,
) {
	du := l.Dist[u]
	dv := l.Dist[v]
	lca := l.FindLCA(u, v)
	dLCA := l.Dist[lca]
	d = du + dv - 2*dLCA
	return
}

func (
	l *LCA,
) FindLCA(
	u, v Int,
) (
	lca Int,
) {
	u, v = l.sort(u, v)
	du := l.Depth[u]
	dv := l.Depth[v]
	v = l.upStream(
		v,
		dv-du,
	)
	if v == u {
		lca = u
		return
	}
	lca = l.findLCASupport(
		du,
		u,
		v,
	)
	return
}

func (
	l *LCA,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	du := l.Depth[u]
	dv := l.Depth[v]
	if du > dv {
		u, v = v, u
	}
	return u, v
}

func (
	l *LCA,
) upStream(
	v Int,
	d Int,
) Int {
	n := d.BitLen()
	for i := 0; i < n; i++ {
		if ^d>>i&1 == 1 {
			continue
		}
		v = l.Ancestors[i][v]
	}
	return v
}

func (
	l *LCA,
) findLCASupport(
	dep Int,
	u, v Int,
) (
	lca Int,
) {
	n := dep.BitLen()
	ancs := l.Ancestors
	for i := n - 1; i > -1; i-- {
		anc := ancs[i]
		nu, nv := anc[u], anc[v]
		if nu == nv {
			continue
		}
		u, v = nu, nv
	}
	lca = l.Parent[u]
	return
}

type DistXFormCDT struct {
	A    IntMatrix
	B    IntMatrix
	i, j int
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
	s := Shape(a)
	n, m := s[0], s[1]
	cdt.B = Make(
		cdt.B,
		inf,
		n, m,
	).(IntMatrix)
	for i := 0; i < n; i++ {
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
	m := Shape(b)[1]
	for j := 0; j < m; j++ {
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
	Reverse(cdt.B)
	cdt.CumMin()
	cdt.B = cdt.B.T()
	cdt.CumMin()
	Reverse(cdt.B)
	cdt.CumMin()
	cdt.B = cdt.B.T()
}

func (
	cdt *DistXFormCDT,
) CumMin() {
	b := cdt.B
	n := Shape(b)[0]
	for i := 0; i < n-1; i++ {
		cdt.i = i
		cdt.cumMinSupport()
	}
}

func (
	cdt *DistXFormCDT,
) cumMinSupport() {
	b := cdt.B
	i := cdt.i
	m := Shape(b)[1]
	for j := 0; j < m; j++ {
		b[i+1][j] = Min(
			b[i+1][j],
			b[i][j]+1,
		).(Int)
	}
}

type IO struct {
	Scanner *bufio.Scanner
	Reader  *bufio.Reader
	Writer  *bufio.Writer
}

func (
	io *IO,
) SetScanner() {
	scanner := bufio.NewScanner(
		os.Stdin,
	)
	scanner.Split(
		bufio.ScanWords,
	)
	io.Scanner = scanner
}

func (
	io *IO,
) SetScanBuf(
	bufSize int,
) {
	io.Scanner.Buffer(
		[]byte{},
		bufSize,
	)
}

func (
	io *IO,
) SetReader() {
	reader := bufio.NewReader(
		os.Stdin,
	)
	io.Reader = reader
}

func (
	io *IO,
) SetWriter() {
	writer := bufio.NewWriter(
		os.Stdout,
	)
	io.Writer = writer
}

func (
	io *IO,
) Init() {
	io.SetScanner()
	io.SetReader()
	io.SetWriter()
}

func (
	io *IO,
) Scan() Str {
	scanner := io.Scanner
	scanner.Scan()
	s := Str(scanner.Text())
	return s
}

func (
	io *IO,
) ScanInt() Int {
	s := io.Scan()
	return s.Int()
}

func (
	io *IO,
) Write(
	a ...interface{},
) {
	writer := io.Writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}

func (
	io *IO,
) Writef(
	f string,
	a ...interface{},
) {
	writer := io.Writer
	fmt.Fprintf(
		writer,
		f,
		a...,
	)
	writer.Flush()
}

type Solver interface {
	Init()
	Prepare()
	Solve()
}

func Run(s Solver) {
	s.Init()
	s.Prepare()
	s.Solve()
}

type Problem struct {
	io *IO
}

func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	const bufSize = 1 << 7
	io.SetScanBuf(bufSize)
	p.io = io
}

func (
	p *Problem,
) Prepare() {
	io := p.io
}

func (
	p *Problem,
) Solve() {
	io := p.io
}

func main() {
	p := new(Problem)
	Run(p)
}
