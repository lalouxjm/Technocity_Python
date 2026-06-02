list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
target = 17


"""
works only for sorted list
"""
def binary_search(lst: list, t: int) -> int:
    """
    # Start of the search zone
    lo = 0

    # End of the search zone
    hi = len(lst) - 1

    # Continue while the search zone is valid
    while lo <= hi:
        # Find the middle index
        mid = (lo + hi) // 2

        # If the middle value is the target, return its index
        if lst[mid] == target:
            return mid

        # If the middle value is too small,
        # ignore the left half and search the right half
        elif lst[mid] < target:
            lo = mid + 1

        # If the middle value is too big,
        # ignore the right half and search the left half
        else:
            hi = mid - 1

    # If we exit the loop, the target was not found
    return -1
    """
    """
    for i, v in enumerate(lst):
        if v == t:
        return i
    return -1
    """


print(f"{target} is on index: {binary_search(list1, target)}")