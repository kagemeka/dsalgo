package string


import "kagemeka/dsa/algebra"
import "sort"
import "kagemeka/dsa"


func SAIS(a []int) (sa []int) {
	mn := Min(a...)
	for i, x := range a { a[i] = x - mn + 1 }
	a = append(a, 0)
	n := len(a)
	m := Max(a...) + 1
	isS := make([]bool, n)
	isLms := make([]bool, n)
	lms := make([]int, 0, n)
	for i := 0; i < n; i++ { isS[i] = true }
	for i := n - 2; i > -1; i-- {
		if a[i] == a[i + 1] {
			isS[i] = isS[i + 1]
		} else {
			isS[i] = a[i] < a[i + 1]
		}
	}
	for i := 1; i < n; i++ { isLms[i] = !isS[i - 1] && isS[i] }
	for i := 0; i < n; i++ { if isLms[i] { lms = append(lms, i) } }
	bucket := make([]int, m)
	for _, x := range a { bucket[x]++ }

	induce := func() []int {
		sa := make([]int, n)
		for i := 0; i < n; i++ { sa[i] = -1 }

		saIdx := make([]int, m)
		copy(saIdx, bucket)
		for i := 0; i < m - 1; i++ { saIdx[i + 1] += saIdx[i] }
		for j := len(lms) - 1; j > -1; j-- {
			i := lms[j]
			x := a[i]
			saIdx[x]--
			sa[saIdx[x]] = i
		}

		copy(saIdx, bucket)
		s := 0
		for i := 0; i < m; i++ { s, saIdx[i] = s + saIdx[i], s }
		for j := 0; j < n; j++ {
			i := sa[j] - 1
			if i < 0 || isS[i] { continue }
			x := a[i]
			sa[saIdx[x]] = i
			saIdx[x]++
		}

		copy(saIdx, bucket)
		for i := 0; i < m - 1; i++ { saIdx[i + 1] += saIdx[i] }
		for j := n - 1; j > -1; j-- {
			i := sa[j] - 1
			if i < 0 || !isS[i] { continue }
			x := a[i]
			saIdx[x]--
			sa[saIdx[x]] = i
		}

		return sa
	}

	sa = induce()

	lmsIdx := make([]int, 0, len(sa))
	for _, i := range sa { if isLms[i] { lmsIdx = append(lmsIdx, i) } }
	l := len(lmsIdx)
	rank := make([]int, n)
	for i := 0; i < n; i++ { rank[i] = -1 }
	r := 0; rank[n - 1] = r
	for i := 0; i < l - 1; i++ {
		j, k := lmsIdx[i], lmsIdx[i + 1]
		for d := 0; d < n; d++ {
			jIsLms, kIsLms := isLms[j + d], isLms[k + d]
			if a[j + d] != a[k + d] || jIsLms != kIsLms { r++; break }
			if d > 0 && (jIsLms || kIsLms) { break }
		}
		rank[k] = r
	}
	buf := make([]int, 0, l)
	for _, r := range rank { if r >= 0 { buf = append(buf, r) } }
	var lmsOrder []int
	if r == l - 1 {
		lmsOrder = make([]int, l)
		for i, r := range buf { lmsOrder[r] = i }
	} else {
		lmsOrder = SAIS(buf)
	}
	buf = make([]int, len(lms))
	for i, j := range lmsOrder { buf[i] = lms[j] }
	lms = buf
	return induce()[1:]
}


func SADoubling(a []int) (sa []int) {
	n := len(a)
	ac := new(ArrayCompression)
	rank, k := ac.Compress(a), 1
	key := make([]int, n)
	for {
		for i := 0; i < n; i++ {
			key[i] = rank[i] << 30
			if i + k < n { key[i] |= 1 + rank[i + k] }
		}
		sa = make([]int, n)
		for i := 0; i < n; i++ { sa[i] = i }
		sort.SliceStable(sa, func(i, j int) bool { return key[sa[i]] < key[sa[j]] } )
		rank[sa[0]] = 0
		for i := 0; i < n - 1; i++ {
			rank[sa[i + 1]] = rank[sa[i]]
			if key[sa[i + 1]] > key[sa[i]] { rank[sa[i + 1]]++ }
		}
		k <<= 1
		if k >= n { break }
	}
	return
}


func SADoublingCountsort(a []int) (sa []int) {
	n := len(a)
	countingSortKey := func(a []int) (key []int) {
		cnt := make([]int, n + 2)
		for _, x := range a { cnt[x + 1]++ }
		for i := 0; i < n; i++ { cnt[i + 1] += cnt[i] }
		key = make([]int, n)
		for i := 0; i < n; i++ {
			key[cnt[a[i]]] = i
			cnt[a[i]]++
		}
		return key
	}

	ac := new(ArrayCompression)
	rank, k := ac.Compress(a), 1
	first := make([]int, n)
	second := make([]int, n)
	sa = make([]int, n)
	key := make([]int, n)
	for {
		for i := 0; i < n - k; i++ { second[i] = 1 + rank[i + k] }
		for i := n - k; i < n; i++ { second[i] = 0 }
		rankSecond := countingSortKey(second)
		for i, j := range rankSecond { first[i] = rank[j] }
		rankFirst := countingSortKey(first)
		for i, j := range rankFirst { sa[i] = rankSecond[j] }
		for i := 0; i < n; i++ {
			key[i] = first[rankFirst[i]] << 30 | second[sa[i]]
		}
		rank[sa[0]] = 0
		for i := 0; i < n - 1; i++ {
			rank[sa[i + 1]] = rank[sa[i]]
			if key[i + 1] > key[i] { rank[sa[i + 1]]++ }
		}
		k <<= 1
		if k >= n { break }
	}
	return
}
