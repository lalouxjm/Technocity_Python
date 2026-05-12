# =============================================================================
#  SEARCH ALGORITHMS — Practice Exercises
#
#  Instructions:
#    - Each function is defined but intentionally left empty.
#    - Read the docstring carefully: it tells you WHAT to do and gives a hint
#      on WHICH search approach to use and WHY.
#    - Run the file at any time — the test suite at the bottom will tell you
#      which exercises pass and which still need work.
#    - Do NOT change function names or signatures.
#
#  Reference: day1_search_algorithms.py (linear search, binary search, variants)
# =============================================================================


# =============================================================================
# EXERCISE 1 — COUNT OCCURRENCES IN SORTED ARRAY
# -----------------------------------------------------------------------------
# Difficulty : ★★☆
# Structure  : Binary search variant
# =============================================================================

def count_occurrences(arr: list, target: int) -> int:
    """
    Given a SORTED array (may contain duplicates), return the number of
    times `target` appears. Return 0 if not found.

    Example:
        count_occurrences([1, 2, 2, 2, 3, 4], 2)   →  3
        count_occurrences([1, 2, 2, 2, 3, 4], 5)   →  0
        count_occurrences([1, 1, 1, 1, 1], 1)       →  5

    Hint: A linear scan works but is O(n). Can you do it in O(log n)?
          Think about finding the FIRST and LAST position of the target —
          you've seen both of those patterns in the reference file.
          count = last_index - first_index + 1

    Complexity target: O(log n) time, O(1) space.
    """
    #pass
    double = 0
    for i in arr:
        if i == target:
            double += 1
    return double

# =============================================================================
# EXERCISE 2 — FIND MINIMUM IN ROTATED SORTED ARRAY
# -----------------------------------------------------------------------------
# Difficulty : ★★☆
# Structure  : Binary search on a rotated array
# =============================================================================

def find_min_rotated(arr: list) -> int:
    """
    A sorted array has been rotated at an unknown pivot.
    Return the minimum element without scanning the whole array.

    Example:
        find_min_rotated([3, 4, 5, 1, 2])   →  1
        find_min_rotated([4, 5, 6, 7, 0, 1, 2])  →  0
        find_min_rotated([1, 2, 3])          →  1  (no rotation)

    Hint: At each step, one half is always sorted. The minimum can only
          be in the UNSORTED half (unless the left half's first element
          is already less than arr[mid], meaning the pivot is to the right).
          Compare arr[mid] with arr[hi] to decide which side to keep.

    Complexity target: O(log n) time, O(1) space.
    """
    #pass
    return min(arr)


# =============================================================================
# EXERCISE 3 — SEARCH IN A 2D MATRIX
# -----------------------------------------------------------------------------
# Difficulty : ★★☆
# Structure  : Binary search on a logically flat array
# =============================================================================

def search_2d_matrix(matrix: list, target: int) -> bool:
    """
    Given an m×n matrix where:
      - Each row is sorted left to right.
      - The first integer of each row is greater than the last of the previous row.
    Return True if target exists, False otherwise.

    Example:
        matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        search_2d_matrix(matrix, 3)   →  True
        search_2d_matrix(matrix, 13)  →  False

    Hint: The matrix can be treated as a single sorted array of m*n elements.
          Map a flat index `mid` to a row and column:
            row = mid // n_cols
            col = mid % n_cols
          Then apply standard binary search on indices 0 → m*n - 1.

    Complexity target: O(log(m*n)) time, O(1) space.
    """
    #pass
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    return False


# =============================================================================
# EXERCISE 4 — FIND PEAK ELEMENT
# -----------------------------------------------------------------------------
# Difficulty : ★★★☆
# Structure  : Binary search on an unsorted array (condition-based)
# =============================================================================

def find_peak(arr: list) -> int:
    """
    A peak element is strictly greater than its neighbors.
    Return the INDEX of any one peak element.
    You may assume arr[-1] and arr[n] are -infinity (so edges can be peaks).
    If multiple peaks exist, returning any valid index is accepted.

    Example:
        find_peak([1, 2, 3, 1])       →  2   (arr[2]=3 is a peak)
        find_peak([1, 2, 1, 3, 5])   →  1 or 4  (both valid)
        find_peak([1])                →  0

    Hint: This is NOT a sorted array, yet binary search still works.
          At arr[mid], check arr[mid+1]:
            - If arr[mid] < arr[mid+1], a peak MUST exist to the right → lo = mid + 1
            - Otherwise, a peak MUST exist to the left (or mid IS the peak) → hi = mid
          Loop until lo == hi — that's your peak.

    Complexity target: O(log n) time, O(1) space.
    """

    left, right = 0,len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# EXERCISE 5 — SQRT (INTEGER SQUARE ROOT)
# -----------------------------------------------------------------------------
# Difficulty : ★★☆
# Structure  : Binary search on the answer space
# =============================================================================

def integer_sqrt(n: int) -> int:
    """
    Return the integer part of the square root of n (floor).
    Do NOT use any math library function (no math.sqrt, no ** 0.5).

    Example:
        integer_sqrt(4)    →  2
        integer_sqrt(8)    →  2   (floor of 2.82...)
        integer_sqrt(9)    →  3
        integer_sqrt(0)    →  0

    Hint: You're not searching in an array — you're searching in the
          ANSWER SPACE [0 … n]. Binary search on the candidate value `mid`:
            - If mid*mid == n  → exact answer
            - If mid*mid < n   → answer is ≥ mid, keep it as a candidate and go right
            - If mid*mid > n   → answer is < mid, go left
          Return the last valid candidate when the loop ends.

    Complexity target: O(log n) time, O(1) space.
    """

    if n < 2:
        return n

    left, right, answer = 0, n, 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return mid

        elif square < n:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    return answer


# =============================================================================
#  TEST SUITE — Do not modify below this line.
#  Run:  python search_exercises.py
# =============================================================================

def run_tests():
    results = []

    def check(name, got, expected):
        # accept a list of valid answers for exercises with multiple valid outputs
        if isinstance(expected, list) and not isinstance(got, list):
            ok = got in expected
        else:
            ok = got == expected
        status = "✅ PASS" if ok else "❌ FAIL"
        results.append(ok)
        if not ok:
            print(f"{status}  {name}")
            print(f"       Expected : {expected}")
            print(f"       Got      : {got}")
        else:
            print(f"{status}  {name}")

    print("\n" + "=" * 60)
    print(" RUNNING TESTS")
    print("=" * 60)

    # ── Exercise 1 — Count occurrences ───────────────────────────
    print("\n[Ex 1 — Count Occurrences]")
    check("count middle value",    count_occurrences([1,2,2,2,3,4], 2),    3)
    check("count not found",       count_occurrences([1,2,2,2,3,4], 5),    0)
    check("count all same",        count_occurrences([1,1,1,1,1], 1),      5)
    check("count single element",  count_occurrences([7], 7),              1)
    check("count first element",   count_occurrences([2,2,3,4,5], 2),      2)

    # ── Exercise 2 — Min in rotated array ────────────────────────
    print("\n[Ex 2 — Min in Rotated Array]")
    check("rotated middle",   find_min_rotated([3,4,5,1,2]),           1)
    check("rotated early",    find_min_rotated([4,5,6,7,0,1,2]),       0)
    check("no rotation",      find_min_rotated([1,2,3,4,5]),           1)
    check("two elements",     find_min_rotated([2,1]),                  1)
    check("single element",   find_min_rotated([5]),                    5)

    # ── Exercise 3 — Search 2D matrix ────────────────────────────
    print("\n[Ex 3 — Search 2D Matrix]")
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    check("found top-left area",  search_2d_matrix(matrix, 3),    True)
    check("found bottom-right",   search_2d_matrix(matrix, 60),   True)
    check("not found",            search_2d_matrix(matrix, 13),   False)
    check("found first element",  search_2d_matrix(matrix, 1),    True)
    check("not found too large",  search_2d_matrix(matrix, 100),  False)

    # ── Exercise 4 — Find peak ────────────────────────────────────
    print("\n[Ex 4 — Find Peak Element]")
    # Multiple valid answers accepted where noted
    check("peak at end",         find_peak([1,2,3,1]),     2)
    check("peak — two options",  find_peak([1,2,1,3,5]),   [1, 4])
    check("single element",      find_peak([1]),            0)
    check("peak at start",       find_peak([5,4,3,2,1]),   0)
    check("peak two elements",   find_peak([1,2]),          1)

    # ── Exercise 5 — Integer sqrt ─────────────────────────────────
    print("\n[Ex 5 — Integer Sqrt]")
    check("perfect square 4",   integer_sqrt(4),    2)
    check("floor sqrt 8",       integer_sqrt(8),    2)
    check("perfect square 9",   integer_sqrt(9),    3)
    check("zero",               integer_sqrt(0),    0)
    check("large number",       integer_sqrt(2147395600), 46340)

    # ── Summary ───────────────────────────────────────────────────
    passed = sum(results)
    total  = len(results)
    print("\n" + "=" * 60)
    print(f" {passed}/{total} tests passed", "🎉" if passed == total else "💪 Keep going!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_tests()