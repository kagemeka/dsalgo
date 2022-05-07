from __future__ import annotations


def argsort_permutation(arr: list[int]) -> list[int]:
    order = [0] * len(arr)
    for i, value in enumerate(arr):
        order[value] = i
    return order


def argsort(arr: list[int]) -> list[int]:
    return sorted(range(len(arr)), key=lambda i: arr[i])


def counting_sort_index(arr: list[int]) -> list[int]:
    if not arr:
        return []
    mn = min(arr)
    arr = [x - mn for x in arr]
    n, buckets_size = len(arr), max(arr) + 1
    count = [0] * buckets_size
    for x in arr:
        count[x] += 1
    for i in range(buckets_size - 1):
        count[i + 1] += count[i]
    order = [0] * n
    for i in range(n - 1, -1, -1):
        count[arr[i]] -= 1
        order[count[arr[i]]] = i
    return order


def counting_sort(arr: list[int]) -> list[int]:
    return [arr[i] for i in counting_sort_index(arr)]


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
