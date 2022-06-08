package combinatorics


/* cut below */



// dfs, n >= 63
func Cmbs(
	a []interface{}, 
	r int,
) (
	res [][]interface{},
) {
	n := len(a)
	if r > n || r < 0 {return}
	indices := make([]int, r)
	for i := 0; i < r; i++ {
		indices[i] = i
	}
	res = append(res, a[:r])
	for {
		flg := false
		i := r-1
		for ; i > -1; i-- {
			if indices[i] == i+n-r {
				continue
			}
			flg = true 
			break 
		}
		if !flg {return}
		indices[i]++
		for j := i+1; j < r; j++ {
			indices[j] = indices[j-1]+1
		}
		tmp := make(
			[]interface{}, 
			r,
		)
		for j := 0; j < r; j++ {
			tmp[j] = a[indices[j]]
		}
		res = append(res, tmp)
	}
}