import 'solver.dart';
import 'read_stdin_async.dart';

// cut below

class Problem with Run<Problem> implements Solver {
  var read = ReadStdinAsync();

  @override
  void prepare() async {
    await read.prepare();
    print(read());
  }

  @override
  void solve() {}
}

void main() async {
  var p = Problem();
  p();
}
