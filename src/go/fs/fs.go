package fs


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


// stdio := NewStdIO()
// defer stdio.Flush()
type StdIO struct {
	scanner *bufio.Scanner
	writer *bufio.Writer
}

func NewStdIO() *StdIO {
	const maxBuffer = 1 << 20
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer([]byte{}, maxBuffer)
	scanner.Split(bufio.ScanWords)
	return &StdIO { 
		scanner: scanner,
		writer: bufio.NewWriter(os.Stdout),
	}
}

func (stdio *StdIO) Scan() string {
	stdio.scanner.Scan()
	return stdio.scanner.Text()
}

func (stdio *StdIO) ScanInt() int {
	v, _ := strconv.Atoi(stdio.Scan())
	return v
}

func (stdio *StdIO) Write(a ...interface{}) {
	fmt.Fprintln(stdio.writer, a...)
}

func (stdio *StdIO) Flush() { stdio.writer.Flush() }
