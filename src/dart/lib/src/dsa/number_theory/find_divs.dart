/* cut below */



extension Divisors on int {
  List<int> divs(n) {
    List<int> divs = [];
    for (
      int i = 1;
      i * i <= n;
      i++
    ) {
      if (n % i != 0) continue;
      divs.add(i);
      int j = n ~/ i;
      if (j == i) continue;
      divs.add(j);
    }
    divs.sort();
    return divs;
  }
}
