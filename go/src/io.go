package dsalgo

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type BufStdScanner struct {
	scanner *bufio.Scanner
}

func NewBufStdScanner() *BufStdScanner {
	const maxBuffer = 1 << 20
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer([]byte{}, maxBuffer)
	scanner.Split(bufio.ScanWords)
	return &BufStdScanner{scanner}
}

func (sc *BufStdScanner) Str() string {
	sc.scanner.Scan()
	return sc.scanner.Text()
}

func (sc *BufStdScanner) Int() int {
	v, _ := strconv.Atoi(sc.Str())
	return v
}

type BufStdWriter struct {
	writer *bufio.Writer
}

// defer writer.Flush()
func NewBufStdWriter() *BufStdWriter {
	return &BufStdWriter{bufio.NewWriter(os.Stdout)}
}

func (writer *BufStdWriter) Write(a ...any) {
	fmt.Fprintln(writer.writer, a...)
}

func (writer *BufStdWriter) Flush() { writer.writer.Flush() }
