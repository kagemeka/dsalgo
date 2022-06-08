import unittest


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


class Tests(unittest.TestCase):
    def test(self) -> None:
        import os

        os.environ["PYTHON_DEBUG"] = "1"
        debug(
            1,
            2,
            a=[1, 2, 3, 5, 6, 7, 8, 9, 0, 1, 1],
        )


if __name__ == "__main__":
    import doctest

    unittest.main()
