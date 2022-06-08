package cp


//



type Runes []rune


func (
	a Runes,
) Len() int {
	return len(a)
}


func (
	a Runes,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}
