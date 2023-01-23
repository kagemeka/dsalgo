import 'dart:io';
import 'dart:convert';

class ReadStdinSync {
  Set<int> ng = {-1, 10, 32};

  String call() {
    List<int> bytes = [];
    while (true) {
      var b = stdin.readByteSync();
      if (ng.contains(b)) break;
      bytes.add(b);
    }
    return utf8.decode(bytes);
  }

  int i() => int.parse(this());

  Iterable<String> iter() sync* {
    while (true) {
      var s = this();
      if (s.isEmpty) break;
      yield s;
    }
  }

  String? line() => stdin.readLineSync();
}
