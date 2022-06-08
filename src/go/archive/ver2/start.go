package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Problem struct {
	io *IO
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
}


func (
	p *Problem,
) Input() {
}


func (
	p *Problem,
) Solve() {
}



func main() {
	p := new(Problem)
	p.Init()
	// t := p.io.ReadInt()
	t := 1
	for i := 0; i < t; i++ {
		Run(p)
	}
}



type IO struct {
	r *Read
	w *Write
}


func (
	io *IO,
) Init() {
	r, w := new(Read), new(Write)
	r.Init()
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



type Read struct {
	sc *bufio.Scanner
}


func (
	r *Read,
) Init() {
	r.setScanner()
	const buf = 1 << 20
	r.setBuf(buf)
}


func (
	r *Read,
) Int() (
	int,
) {
	s := r.Str()
	i, _ := strconv.Atoi(s)
	return i
}


func (
	r *Read,
) setBuf(
	bufSize int,
) {
	r.sc.Buffer(
		[]byte{},
		bufSize,
	)
}


func (
	r *Read,
) setScanner() {
	sc := bufio.NewScanner(
		os.Stdin,
	)
	sc.Split(
		bufio.ScanWords,
	)
	r.sc = sc
}


func  (
	r *Read,
) Str() (
	string,
) {
	sc  := r.sc
	sc.Scan()
	return sc.Text()
}



type Solver interface {
	Init()
	Input()
	Solve()
}


func Run(
	s Solver,
) {
	s.Input()
	s.Solve()
}



type Write struct {
	writer *bufio.Writer
}


func (
	w *Write,
) All(
	a ...interface{},
) {
	writer := w.writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}


func (
	w *Write,
) Init() {
	w.setWriter()
}


func (
	w *Write,
) setWriter() {
	w.writer = bufio.NewWriter(
		os.Stdout,
	)
}
