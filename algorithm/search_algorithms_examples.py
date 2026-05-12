# =============================================================================
# DAY 1 — SEARCH ALGORITHMS
# From worst to best complexity for each problem.
# Run this file directly to see all results: python day1_search_algorithms.py
# =============================================================================


# =============================================================================
# 1. LINEAR SEARCH
# -----------------------------------------------------------------------------
# Idea    : scan every element one by one until the target is found.
# Use when: data is unsorted, or you only search once (not worth sorting first).
# Time    : O(n)  — must check every element in the worst case
# Space   : O(1)  — no auxiliary structure needed
# =============================================================================

def linear_search_v1(arr, target):
    """
    Version 1 — explicit index loop.
    Time: O(n) | Space: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i        # return index of first match
    return -1               # -1 signals "not found" (common convention)


def linear_search_v2(arr, target):
    """
    Version 2 — enumerate() — more Pythonic, avoids manual indexing.
    Time: O(n) | Space: O(1)
    Preferred in production code for readability.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def linear_search_v3(arr, target):
    """
    Version 3 — Python built-in .index().
    Time: O(n) | Space: O(1)
    Cleanest syntax, but raises ValueError if not found instead of returning -1.
    Use try/except or check with `in` first.
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1


# =============================================================================
# 2. BINARY SEARCH
# -----------------------------------------------------------------------------
# Precondition: the array MUST be sorted.
# Idea    : compare the target with the middle element.
#           If smaller → search left half. If larger → search right half.
#           Each step halves the search space → O(log n).
# Use when: sorted data, repeated searches (amortise the sort cost).
# Time    : O(log n)
# Space   : O(log n) recursive (call stack) | O(1) iterative
#
# Key edge cases to always mention:
#   - empty array
#   - single element
#   - target smaller than arr[0] or larger than arr[-1]
#   - duplicate values (returns *an* index, not necessarily the first)
# =============================================================================

def binary_search_v1_naive(arr, target):
    """
    Version 1 — NAIVE: linear scan on a sorted array.
    Wastes the sorted property entirely.
    Time: O(n) | Space: O(1)
    Shown here only to illustrate what NOT to do.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
        if value > target:      # early exit possible because array is sorted
            return -1
    return -1


def binary_search_v2_recursive(arr, target, lo=0, hi=None):
    """
    Version 2 — recursive.
    Time: O(log n) | Space: O(log n) — each call adds a frame to the call stack.
    Clean and easy to reason about, but uses stack space.
    """
    if hi is None:
        hi = len(arr) - 1

    if lo > hi:                 # base case: search space is empty
        return -1

    mid = (lo + hi) // 2       # integer division — avoids float index

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_v2_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_v2_recursive(arr, target, lo, mid - 1)


def binary_search_v3_iterative(arr, target):
    """
    Version 3 — iterative. PREFERRED in interviews.
    Time: O(log n) | Space: O(1) — no call stack overhead.
    Same logic as recursive but uses a while loop instead.
    """
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1        # target is in the right half
        else:
            hi = mid - 1        # target is in the left half

    return -1


def binary_search_v4_builtin(arr, target):
    """
    Version 4 — bisect module (standard library).
    Time: O(log n) | Space: O(1)
    bisect_left returns the insertion point; we check if it's actually the target.
    Use this in production code — battle-tested and handles edge cases correctly.
    """
    import bisect
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return i
    return -1


# =============================================================================
# 3. BINARY SEARCH VARIANTS
# -----------------------------------------------------------------------------
# Real interview problems rarely ask for plain binary search.
# They ask for these variants — know the pattern cold.
# =============================================================================

def find_first_occurrence(arr, target):
    """
    Find the FIRST index of target in a sorted array with duplicates.
    Key change: when we find target, don't stop — keep searching left.
    Time: O(log n) | Space: O(1)

    Example: arr = [1, 2, 2, 2, 3], target = 2 → returns 1 (not 2 or 3)
    """
    lo, hi = 0, len(arr) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid        # record this position, but keep going left
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return result


def find_last_occurrence(arr, target):
    """
    Find the LAST index of target in a sorted array with duplicates.
    Mirror of find_first_occurrence — keep searching right when found.
    Time: O(log n) | Space: O(1)

    Example: arr = [1, 2, 2, 2, 3], target = 2 → returns 3
    """
    lo, hi = 0, len(arr) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid        # record, but keep going right
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return result


def search_insert_position(arr, target):
    """
    If target is not found, return the index where it WOULD be inserted
    to keep the array sorted. Classic LeetCode #35.
    Time: O(log n) | Space: O(1)

    Example: arr = [1, 3, 5, 6], target = 4 → returns 2
             arr = [1, 3, 5, 6], target = 7 → returns 4
    """
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo           # lo is the insertion point when the loop ends


def search_in_rotated_array(arr, target):
    """
    Search in a ROTATED sorted array — no prior knowledge of the pivot.
    Example: [4, 5, 6, 7, 0, 1, 2] is [0,1,2,4,5,6,7] rotated at index 4.

    Key insight: one half is always sorted. Check which half, then decide
    which half to search — still O(log n).
    Time: O(log n) | Space: O(1)

    Example: arr = [4, 5, 6, 7, 0, 1, 2], target = 0 → returns 4
    """
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1    # target is in the sorted left half
            else:
                lo = mid + 1    # target must be in the right half
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1    # target is in the sorted right half
            else:
                hi = mid - 1    # target must be in the left half

    return -1


# =============================================================================
# DEMO — run all functions with test cases
# =============================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("1. LINEAR SEARCH")
    print("=" * 60)

    data = [7, 3, 15, 9, 2, 11, 5]
    target = 9
    print(f"  Array : {data}")
    print(f"  Target: {target}")
    print(f"  v1 (range loop)  → index {linear_search_v1(data, target)}")
    print(f"  v2 (enumerate)   → index {linear_search_v2(data, target)}")
    print(f"  v3 (built-in)    → index {linear_search_v3(data, target)}")
    print(f"  Not found case   → index {linear_search_v1(data, 99)}")

    print()
    print("=" * 60)
    print("2. BINARY SEARCH  (array must be sorted)")
    print("=" * 60)

    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    print(f"  Array : {sorted_data}")
    print(f"  Target: {target}")
    print(f"  v1 (naive O(n))     → index {binary_search_v1_naive(sorted_data, target)}")
    print(f"  v2 (recursive)      → index {binary_search_v2_recursive(sorted_data, target)}")
    print(f"  v3 (iterative)      → index {binary_search_v3_iterative(sorted_data, target)}")
    print(f"  v4 (bisect module)  → index {binary_search_v4_builtin(sorted_data, target)}")
    print(f"  Not found case      → index {binary_search_v3_iterative(sorted_data, 4)}")

    print()
    print("=" * 60)
    print("3. BINARY SEARCH VARIANTS")
    print("=" * 60)

    dupes = [1, 2, 2, 2, 3, 4, 5]
    print(f"\n  First/Last occurrence — array: {dupes}, target: 2")
    print(f"  First occurrence → index {find_first_occurrence(dupes, 2)}")
    print(f"  Last  occurrence → index {find_last_occurrence(dupes, 2)}")

    arr2 = [1, 3, 5, 6]
    print(f"\n  Insert position — array: {arr2}")
    print(f"  target=4 → insert at index {search_insert_position(arr2, 4)}")
    print(f"  target=0 → insert at index {search_insert_position(arr2, 0)}")
    print(f"  target=7 → insert at index {search_insert_position(arr2, 7)}")

    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"\n  Rotated array — array: {rotated}")
    print(f"  target=0 → index {search_in_rotated_array(rotated, 0)}")
    print(f"  target=6 → index {search_in_rotated_array(rotated, 6)}")
    print(f"  target=3 → index {search_in_rotated_array(rotated, 3)} (not found)")

    print()
    print("=" * 60)
    print("COMPLEXITY SUMMARY")
    print("=" * 60)
    print(f"  {'Algorithm':<35} {'Time':>10}  {'Space':>8}")
    print(f"  {'-'*35} {'-'*10}  {'-'*8}")
    print(f"  {'Linear search':<35} {'O(n)':>10}  {'O(1)':>8}")
    print(f"  {'Binary search (recursive)':<35} {'O(log n)':>10}  {'O(log n)':>8}")
    print(f"  {'Binary search (iterative)':<35} {'O(log n)':>10}  {'O(1)':>8}")
    print(f"  {'First/last occurrence':<35} {'O(log n)':>10}  {'O(1)':>8}")
    print(f"  {'Insert position':<35} {'O(log n)':>10}  {'O(1)':>8}")
    print(f"  {'Search in rotated array':<35} {'O(log n)':>10}  {'O(1)':>8}")