import 'dart:io';

void main() async {
  const n = 1 << 16;
  var ls = List<String>.filled(
    n,
    '1234567890\n',
  );
  var s = ls.join();
  final filename = (
    '../data/large_input.txt'
  );
  var file = await File(
    filename,
  ).writeAsString(s);
}
