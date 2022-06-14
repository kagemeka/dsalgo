package cp

import (
	"bufio"
	"fmt"
	. "kagemeka/general/types"
	"os"
)

/* cut below */

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
	if io.Scanner == nil {
		io.SetScanner()
	}
	if io.Reader == nil {
		io.SetReader()
	}
	if io.Writer == nil {
		io.SetWriter()
	}
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
