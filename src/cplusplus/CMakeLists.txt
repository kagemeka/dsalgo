#
cmake_minimum_required(VERSION 3.14)

project(dsalgo)

set(CMAKE_CXX_COMPILER_VERSION, 20)
# GoogleTest requires at least C++11
set(CMAKE_CXX_STANDARD 11)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)


enable_testing()


# region add unit tests

add_executable(
  dsalgo_test
  tests/euclidean_modular_gcd_inv.cpp
)

# endregion

target_link_libraries(
  dsalgo_test
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(dsalgo_test)
