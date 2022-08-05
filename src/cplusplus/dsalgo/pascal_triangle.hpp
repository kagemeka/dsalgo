#ifndef PASCAL_TRIANGLE_HPP
#define PASCAL_TRIANGLE_HPP
#include <vector>
template<typename T> auto pascal_triangle(unsigned long int size)
  -> std::vector<std::vector<T>> {
  std::vector<std::vector<T>> p(size, std::vector<T>(size, 0));
  for(unsigned long int i = 0; i < size; ++i) p[i][0] = 1;
  for(unsigned long int i = 1; i < size; ++i) {
    for(unsigned long int j = 1; j < size; ++j) {
      p[i][j] = p[i - 1][j - 1] + p[i - 1][j];
    }
  }
  return p;
}
#endif // PASCAL_TRIANGLE_HPP
