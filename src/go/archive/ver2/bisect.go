package cp 

import (
	"sort"
)

//


type BisectIF interface {
	BisecLeftFunc(
		int,
		interface{},
	) bool
	Get(i int) interface{}
	Len() int
}
						

type Bisect struct {
	data BisectIF
	x interface{}
}


func (
	a Bisect,
) Left(
	x interface{},
) int {
	a.x = x
	return sort.Search(
		a.data.Len(),
		a.leftFunc,
	)
}


func (
	a Bisect,
) leftFunc(
	i int,
) bool {
	return a.data.BisectLeftFunc(
		i,
		a.x,
	)
}


func (
	a Bisect,
) Right(
	x Comparable,
) int {
	a.x = x
	return sort.Search(
		a.data.Len(),
		a.rightFunc,
	)
}


func (
	a Bisect,
) rightFunc(
	i int,
) bool {
	return 
		a.leftFunc(i) && 
		a.Get(i) != a.x
}


func (
	a Bisect,
) Set(
	data BisectIF,
) {
	a.data = data
}
