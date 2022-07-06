#pragma once

template<typename T> auto inv_2(T mod) -> T { return (mod + 1) >> 1; }
