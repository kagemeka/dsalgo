from __future__ import annotations


def argsort_permutation(arr: list[int]) -> list[int]:
    order = [0] * len(arr)
    for i, value in enumerate(arr):
        order[value] = i
    return order


def bucket_sort(arr: list[int]) -> list[int]:
    ...


def bubble_sort(arr: list[int]) -> list[int]:
    ...


def cocktail_shaker_sort(arr: list[int]) -> list[int]:
    ...


def insertion_sort(arr: list[int]) -> list[int]:
    ...


def heap_sort(arr: list[int]) -> list[int]:
    ...


def quick_sort(arr: list[int]) -> list[int]:
    ...


def radix_sort(arr: list[int]) -> list[int]:
    ...


def merge_sort(arr: list[int]) -> list[int]:
    ...
