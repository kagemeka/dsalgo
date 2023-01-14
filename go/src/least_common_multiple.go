package dsalgo

func LCM(x, y int) int { return x / GCD(x, y) * y }
