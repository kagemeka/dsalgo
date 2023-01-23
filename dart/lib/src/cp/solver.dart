abstract class Solver {
  void prepare() {}
  void solve() {}
}

mixin Run<T extends Solver> {
  void call() {
    var sol = this as T;
    sol.prepare();
    sol.solve();
  }
}
