import 'dart:io';

void main() {
  var lines = <String>[];
  while (true) {
    var line = stdin.readLineSync();
    if (line == null) {
      break;
    }
    lines.add(line);
  }
  print(lines.length);
}

class ReadStdinSync {
  int a = 1;

  String call() {
    return '';
  }
}
