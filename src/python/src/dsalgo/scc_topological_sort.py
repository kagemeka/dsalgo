import typing


def toposort(labels: typing.List[int]) -> typing.List[int]:
    k = max(labels)
    return [k - l for l in labels]
