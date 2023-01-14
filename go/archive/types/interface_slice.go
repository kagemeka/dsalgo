package types


import (
	"strings"
)


/* cut below */



type IS []interface{}


func SliceFormat(
	n int,
	sep string,
) (
	format string,
) {
	f := make(
		[]string,
		n,
	)
	for i := 0; i < n; i++ {
		f[i] = "%v"
	}
	format = strings.Join(
		f,
		sep,
	)
	return
}
