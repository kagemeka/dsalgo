import
'./abstract_algebra.dart';


/* cut below */



class Modular
with
Power<Modular>,
Division<Modular>,
Subtraction<Modular>
implements
Field<Modular> {
  int value = 0;
  final int mod;


  Modular(
    this.value,
    this.mod,
  ) {
    value %= mod;
  }


  Modular.define(this.mod);


  Modular call(
    int value,
  ) {
    return Modular(value, mod);
  }


  Modular operator +(
    final Modular other,
  ) {
    return Modular(
      value + other.value,
      mod,
    );
  }


  Modular addIdentity()
  {
    return Modular(0, mod);
  }


  Modular operator -() {
    return Modular(
      -value,
      mod,
    );
  }


  Modular operator *(
    Modular other,
  ) {
    return Modular(
      value * other.value,
      mod,
    );
  }


  Modular mulIdentity() {
    return Modular(1, mod);
  }


  Modular inv() {
    return this.pow(mod - 2);
  }


  String toString() {
    return '${value}';
  }


  List<Modular> factorial()
  {
    int n = value;
    List<Modular> a = [
      Modular(1, mod),
      for (
        int i = 1; i < n; i++
      ) Modular(i, mod)
    ];
    a = a.cumprod();
    return a;
  }


  List<Modular> invFactorial()
  {
    int n = value;
    var fac = this.factorial();
    List<Modular> a = [
      for (
        int i = n; i > 0; i--
      ) Modular(i, mod)
    ];
    a[0] = fac[n - 1].inv();
    a = a.cumprod();
    a = a.reversed.toList();
    return a;
  }
}
