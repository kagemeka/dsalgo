
/* cut below */



extension Bisect<E> on List<E> {
  int bisectLeft(E element) {
    int lo = 0, hi = length;
    var compare = (
      Comparable.compare
      as Function(E, E)
    );
    while (lo < hi) {
      var x = (lo + hi) ~/ 2;
      if (
        compare(
          element,
          this[x],
        ) > 0
      ) {
        lo = x + 1;
      } else {
        hi = x;
      }
    }
    return lo;
  }


  int bisectRight(E element) {
    int lo = 0, hi = length;
    var compare = (
      Comparable.compare
      as Function(E, E)
    );
    while (lo < hi) {
      var x = (lo + hi) ~/ 2;
      if (
        compare(
          element,
          this[x],
        ) < 0
      ) {
        hi = x;
      } else {
        lo = x + 1;
      }
    }
    return lo;
  }
}
