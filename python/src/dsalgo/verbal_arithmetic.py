from __future__ import annotations

import bisect
import functools
import operator
import typing


def verbal_arithmetic(
    words: list[list[int]],
    result: list[int],
    lo: int = 0,
    hi: int = 10,  # digit := [lo, hi),
    leading_zero: bool = True,
) -> list[typing.Dict[int, int]]:
    r"""Solve verbal arthmetic."""
    words = words.copy()
    words.append(result)
    letters: list[int] = sorted(
        functools.reduce(
            operator.or_,
            map(lambda w: set(w), words),
            set(),
        ),
    )
    if len(letters) > hi - lo:
        return []
    words = [
        [bisect.bisect_left(letters, letter) for letter in word]
        for word in words
    ]
    n, m = len(words), max(map(len, words))
    values = [-1] * (hi - lo)
    digits = [-1] * len(letters)
    patterns: list[typing.Dict[int, int]] = []

    def search(row: int, column: int, sum_column: int) -> None:
        if column >= m:
            if sum_column == 0:
                patterns.append(dict(zip(letters, digits)))
            return
        if row == n:
            if sum_column % 10 == 0:
                search(0, column + 1, sum_column // 10)
            return
        word = words[row]
        if column >= len(word):
            search(row + 1, column, sum_column)
            return
        sign = (row < n - 1) * 2 - 1
        v = word[~column]

        def no_leading_zero(digit: int) -> bool:
            return (
                digit != 0
                or column < len(word) - 1
                or leading_zero
                and row == 0
            )

        if digits[v] != -1:
            if no_leading_zero(digits[v]):
                search(row + 1, column, sum_column + sign * digits[v])
            return
        for digit in range(lo, hi):
            if values[digit - lo] != -1:
                continue
            if not no_leading_zero(digit):
                continue
            digits[v], values[digit - lo] = digit, v
            search(row + 1, column, sum_column + sign * digit)
            digits[v] = values[digit - lo] = -1

    search(0, 0, 0)
    return patterns


def to_int(
    words: list[str],
    result: str,
) -> tuple[list[list[int]], list[int]]:
    return (
        [list(map(ord, word)) for word in words],
        list(map(ord, result)),
    )


def to_str(answer: dict[int, int]) -> dict[str, int]:
    return {chr(value): digit for value, digit in answer.items()}


def verbal_arithmetic_from_str(
    words: list[str],
    result: str,
    lo: int = 0,
    hi: int = 10,
    leading_zero: bool = True,
) -> list[dict[str, int]]:
    answer = verbal_arithmetic(*to_int(words, result), lo, hi, leading_zero)
    return list(map(to_str, answer))
