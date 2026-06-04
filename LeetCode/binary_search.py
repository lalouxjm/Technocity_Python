list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
target = 17


"""
works only for sorted list
"""
def binary_search(lst: list, t: int) -> int:
    """
    lo = 0
    hi = len(lst) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
    """
    """
    for i, v in enumerate(lst):
        if v == t:
        return i
    return -1
    """


print(f"{target} is on index: {binary_search(list1, target)}")