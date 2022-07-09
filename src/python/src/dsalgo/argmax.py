def argmax(a: typing.Sequence[T]) -> int:
    # comparable list
    i, mx = 0, a[0]
    for j, x in enumerate(a):
        if x > mx:
            i, mx = j, x
    return i
