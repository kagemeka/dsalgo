/* cut below */

extension BitCount on int {
  int get bitCount {
    int n = this;
    int cnt = 0;
    while (n > 0) {
      cnt += n & 1;
      n >>= 1;
    }
    return cnt;
  }
}
