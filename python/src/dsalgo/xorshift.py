import typing
import unittest

T = typing.TypeVar("T")


def new_rng(
    next: typing.Callable[[T], typing.Tuple[T, int]],
    seed: T,
) -> typing.Callable[[], int]:
    def rng() -> int:
        nonlocal seed
        seed, x = next(seed)
        return x

    return rng


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
