import 
'../algebra/modular.dart';



/* cut below */



class ModChoose<T> {
  List<Modular>
  fac = [],
  iFac = [];


  ModChoose(
    Modular n,
  ) {
    fac = n.factorial();
    iFac = n.invFactorial();
  }


  Modular call(int n, int r) {
    if (r > n || r < 0) {
      return
        fac[0].addIdentity();
    }
    var res;
    res = fac[n];
    res *= iFac[r];
    res *= iFac[n - r];
    return res;    
  }
}