import 'dart:io';

void main() {
  var a = [1, 2, 3];
  var s = 'aaa';
  var write = WriteStdout();
  write(s);
  write.iter(a);
  write.iterln(a);

}


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