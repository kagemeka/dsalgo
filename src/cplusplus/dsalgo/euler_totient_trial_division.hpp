#pragma once
auto phi(long n) -> long {
  long c = n;
  for(long i = 2; i * i <= n; i++) {
    if(n % i) continue;
    c -= c / i;
    while(n % i == 0) n /= i;
  }
  if(n > 1) c -= c / n;
  return c;
}