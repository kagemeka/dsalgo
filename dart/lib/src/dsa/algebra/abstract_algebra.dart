library abstractAlgebra;


/* cut below */


abstract class AddSemiGroup<T>
{
  T operator +(T other);
}



abstract class AddMonoid<T>
implements AddSemiGroup<T> {
  T addIdentity();
}



abstract class AddGroup<T>
implements AddMonoid<T> {
  T operator -();
}



mixin Subtraction<
  T extends AddGroup<T>
> {
  T operator -(T other) {
    var x = this as T;
    return x + -other;
  }
}



abstract class MulSemiGroup<T>
{
  T operator *(T other);
}



abstract class MulMonoid<T>
implements MulSemiGroup<T> {
  T mulIdentity();
}



abstract class MulGroup<T>
implements MulMonoid<T> {
  T inv();
}



mixin Division<
  T extends MulGroup<T>
> {
  T operator /(T other) {
    var x = this as T;
    return x * other.inv();
  }
}



mixin Power<
  T extends MulMonoid<T>
> {
  T pow(int n) {
    var a = this as T;
    if (n == 0) {
      return a.mulIdentity();
    }
    var x = pow(n >> 1);
    x *= x;
    if (n & 1 == 1) x *= a;
    return x;
  }
}



abstract class Ring<T>
implements
AddGroup<T>,
MulMonoid<T> {
}


abstract class Field<T>
implements
AddGroup<T>,
MulGroup<T> {
}



extension
CumProd<
  T extends MulSemiGroup<T>
>
on List<T> {
  List<T> cumprod() {
    var a = List<T>.from(this);
    int n = a.length;
    for (
      int i = 0; i < n - 1; i++
    ) {
      a[i + 1] *= a[i];
    }
    return a;
  }
}



extension
CumSum<
  T extends AddSemiGroup<T>
>
on List<T> {
  List<T> cumpsum() {
    var a = List<T>.from(this);
    int n = a.length;
    for (
      int i = 0; i < n - 1; i++
    ) {
      a[i + 1] += a[i];
    }
    return a;
  }
}
