#include <functional>


// Operations are associative. 
template <typename S> 
struct Semigroup { 
private:
  using Op = std::function<S(S, S)>;
public:
  Op op; 
  bool commutative = false; 
};


template <typename S>
struct Monoid {
private:
  using Op = std::function<S(S, S)>;
  using Id = std::function<S()>;
public:
  Op op;
  Id e;
  bool commutative = false; 
};


template <typename S> struct Group : public Monoid<S> { 
private:
  using Op = std::function<S(S, S)>;
  using Id = std::function<S()>;
  using Inv = std::function<S(S)>;
public:
  Op op;
  Id e;
  Inv inverse;
  bool commutative; 
};


// Multiplication should distributes over addition.
// (S, +) is commutative monoid. 
// S x e_add = e_add.
template <typename S> 
struct Semiring { 
private:
  using Op = std::function<S(S, S)>;
  using Id = std::function<S()>;

public:
  Monoid<S> add;
  Monoid<S> mul;

  Semiring(
    Operator op_add,
    Identity e_add,   
    Operator op_mul,
    Identity e_mul, 
    bool commutative = false
  ) : add(op_add, e_add, true), mul(op_mul, e_mul, commutative) {}
};


template <typename S> 
struct Ring { 
protected:
  using Operator = function<S(S, S)>;
  using Identity = function<S()>;
  using Inverse = function<S(S)>;

public:
  Group<S> add;
  Monoid<S> mul;

  Ring(
    Operator op_add,
    Identity e_add, 
    Inverse inverse,  
    Operator op_mul,
    Identity e_mul, 
    bool commutative = false
  ) : add(op_add, e_add, inverse, true), mul(op_mul, e_mul, commutative) {}
};