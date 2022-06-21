import typing

import dsalgo.algstr
from dsalgo.type import S


def define_power_func(
    monoid: dsalgo.algstr.Monoid[S],
) -> typing.Callable[[S, int], S]:
    def pow(value: S, exponent: int) -> S:
        assert exponent >= 0
        if exponent == 0:
            return monoid.identity()
        x = pow(value, exponent >> 1)
        x = monoid.operation(x, x)
        if exponent & 1:
            x = monoid.operation(x, value)
        return x

    return pow
