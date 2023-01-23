import 'dart:async';
import 'dart:io';
import 'dart:convert';

void main() async {
  var read = ReadStdinAsync();
  await read.prepare();

  print(read._a.length);
  print(read.i());
  // for (var i = 0; i < 1 << 16; i++) {
  //   print(read.int_());
  // }
}

class ReadStdinAsync {
  List<String> _a = [];
  int _i = 0;

  Stream<String> _stream() =>
      stdin.transform(utf8.decoder).transform(LineSplitter());

  void _store(String line) {
    _a[_i] = line;
    _i++;
  }

  String call() => _a[_i++];

  int i() => int.parse(this());

  Future<void> prepare({
    int max = 1 << 16,
  }) async {
    _a = List.filled(max, '');
    _stream().listen(_store);
    int x = 1 << 20;
    x = (max + x - 1) ~/ x;
    x *= (1 << 8);
    var t = Duration(
      milliseconds: x,
    );
    await Future.delayed(t);
    _a = _a
        .join(
          ' ',
        )
        .trim()
        .split(' ');
    _i = 0;
  }
}
