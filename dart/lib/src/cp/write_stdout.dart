import 'dart:io';

class WriteStdout {
  void call(Object x) {
    print(x);
  }

  void iter(
    Iterable<dynamic> a,
  ) {
    stdout.writeAll(a, '\n');
    print('');
  }

  void iterln(
    Iterable<dynamic> a,
  ) {
    stdout.writeAll(a, ' ');
    print('');
  }
}
