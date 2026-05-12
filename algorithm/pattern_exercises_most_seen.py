# =============================================================================
# ALGORITHMIC PATTERNS — EXERCISES
# 10 core patterns, 2 exercises each (warm-up + interview-style)
# =============================================================================
# HOW TO USE
# ----------
# Each exercise has:
#   - A docstring explaining the problem and examples
#   - A function stub to complete
#   - A run_tests() call at the bottom to check your answers
#
# Run the full file:   python pattern_exercises.py
# Run one section:     comment out the run_tests() calls you don't want
# =============================================================================


# =============================================================================
# PATTERN 1 — TWO POINTERS
# =============================================================================

def two_pointers_warmup(s: str) -> bool:
    """
    WARM-UP — Check if a string is a palindrome.

    A palindrome reads the same forwards and backwards.
    Use two pointers starting at each end and moving inward.
    Do NOT use slicing (s == s[::-1]) — the point is to practice the pattern.

    Examples:
        "racecar"  -> True
        "hello"    -> False
        "a"        -> True
        ""         -> True
    """
    # YOUR CODE HERE
    pass


def two_pointers_interview(nums: list[int], target: int) -> list[int]:
    """
    INTERVIEW — Two sum in a sorted array.

    Given a sorted array of integers and a target, return the indices [i, j]
    (1-indexed) of the two numbers that add up to the target.
    Exactly one solution is guaranteed. You may not use the same element twice.

    Constraint: O(n) time, O(1) space — no hash map allowed.

    Examples:
        [2, 7, 11, 15], target=9   -> [1, 2]
        [1, 4, 6, 8],   target=10   -> [2, 3]
        [-3, 0, 4, 8],  target=5   -> [1, 4]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 2 — SLIDING WINDOW
# =============================================================================

def sliding_window_warmup(nums: list[int], k: int) -> int:
    """
    WARM-UP — Maximum sum of k consecutive elements.

    Given an array of integers and a window size k, return the maximum
    sum of any contiguous subarray of length k.

    Compute the first window, then slide: subtract the element leaving,
    add the element entering. No nested loops.

    Examples:
        [2, 1, 5, 1, 3, 2], k=3  -> 9   (subarray [5, 1, 3])
        [1, 4, 2, 9],        k=2  -> 11  (subarray [2, 9])
        [5],                 k=1  -> 5
    """
    # YOUR CODE HERE
    pass


def sliding_window_interview(s: str) -> int:
    """
    INTERVIEW — Longest substring without repeating characters.

    Given a string, return the length of the longest substring that contains
    no duplicate characters. Use a variable-size sliding window: expand right,
    shrink left when a duplicate enters the window.

    Examples:
        "abcabcbb"  -> 3   ("abc")
        "bbbbb"     -> 1   ("b")
        "pwwkew"    -> 3   ("wke")
        ""          -> 0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 3 — BINARY SEARCH
# =============================================================================

def binary_search_warmup(nums: list[int], target: int) -> int:
    """
    WARM-UP — Classic binary search.

    Given a sorted array and a target, return the index of the target.
    Return -1 if not found. Implement from scratch — no bisect module.

    Examples:
        [1, 3, 5, 7, 9], target=5  -> 2
        [1, 3, 5, 7, 9], target=6  -> -1
        [1],             target=1  -> 0
    """
    # YOUR CODE HERE
    pass


def binary_search_interview(nums: list[int], target: int) -> int:
    """
    INTERVIEW — Search in a rotated sorted array.

    A sorted array was rotated at some unknown pivot (e.g. [4,5,6,7,0,1,2]).
    Given this rotated array and a target, return its index or -1.
    Must run in O(log n).

    Key insight: one half of the array is always sorted after a rotation.
    Determine which half is sorted, then decide which half to search.

    Examples:
        [4, 5, 6, 7, 0, 1, 2], target=0  -> 4
        [4, 5, 6, 7, 0, 1, 2], target=3  -> -1
        [1],                   target=0  -> -1
        [3, 1],                target=1  -> 1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 4 — RECURSION & BACKTRACKING
# =============================================================================

def backtracking_warmup(n: int) -> list[list[int]]:
    """
    WARM-UP — Generate all subsets of [1, 2, ..., n].

    Return every possible subset (the power set), including the empty set.
    Order of subsets does not matter.

    Template to follow:
        def backtrack(start, current):
            add a copy of current to results
            for i in range(start, n+1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

    Examples:
        n=2  -> [[], [1], [1, 2], [2]]          (any order)
        n=3  -> [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    """
    def backtrack(start, current):
        print(type(current).__name__)
        results.append(current)
        print(results)
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    results = []
    backtrack(1, [])

    return results


def backtracking_interview(nums: list[int]) -> list[list[int]]:
    """
    INTERVIEW — All permutations of a list of unique integers.

    Return all possible orderings of the input list.
    Classic interview question — expected O(n * n!) time.

    Examples:
        [1, 2, 3]  -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        [0, 1]     -> [[0,1], [1,0]]
        [1]        -> [[1]]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 5 — HASH MAP / HASH SET
# =============================================================================

def hashmap_warmup(nums: list[int], target: int) -> list[int]:
    """
    WARM-UP — Two sum (unsorted).

    Given an unsorted array and a target, return the indices [i, j] of the
    two numbers that add up to target. Each input has exactly one solution.

    Use a hash map: for each number, check if (target - number) is already
    stored. If yes, you found the pair.

    Examples:
        [2, 7, 11, 15], target=9   -> [0, 1]
        [3, 2, 4],      target=6   -> [1, 2]
        [3, 3],         target=6   -> [0, 1]
    """
    # YOUR CODE HERE
    pass


def hashmap_interview(strs: list[str]) -> list[list[str]]:
    """
    INTERVIEW — Group anagrams.

    Given a list of strings, group the anagrams together.
    An anagram uses the same letters in a different order ("eat", "tea", "ate").

    Approach: use a sorted version of each word as the hash map key.
    All words that are anagrams share the same sorted key.

    Examples:
        ["eat","tea","tan","ate","nat","bat"]
            -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]  (any order)
        [""]      -> [[""]]
        ["a"]     -> [["a"]]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 6 — DEPTH-FIRST SEARCH (DFS)
# =============================================================================

def dfs_warmup(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    WARM-UP — DFS traversal order on an adjacency list.

    Given a graph as an adjacency list and a start node, return the list of
    nodes visited in DFS order (visit each node before its neighbors).
    Use a visited set to avoid revisiting.

    Example graph: {0: [1, 2], 1: [3], 2: [3], 3: []}

        0 -> 1 -> 3
        0 -> 2 -> 3  (already visited)

    Examples:
        graph={0:[1,2], 1:[3], 2:[3], 3:[]}, start=0  -> [0, 1, 3, 2]
    """
    # YOUR CODE HERE
    pass


def dfs_interview(grid: list[list[str]]) -> int:
    """
    INTERVIEW — Number of islands.

    Given a 2D grid of '1' (land) and '0' (water), count the number of islands.
    An island is a group of '1's connected horizontally or vertically.

    Approach: iterate the grid. When you find a '1', increment the counter
    and run DFS to mark all connected land cells as visited ('0' or '#').

    Examples:
        [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]  -> 1

        [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]  -> 3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 7 — BREADTH-FIRST SEARCH (BFS)
# =============================================================================

def bfs_warmup(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    WARM-UP — BFS traversal order on an adjacency list.

    Given the same graph as the DFS warm-up, return nodes in BFS order
    (visit all neighbors at distance 1, then distance 2, etc.).
    Use a queue (collections.deque) and a visited set.

    Examples:
        graph={0:[1,2], 1:[3], 2:[3], 3:[]}, start=0  -> [0, 1, 2, 3]
    """
    # YOUR CODE HERE
    pass


def bfs_interview(grid: list[list[int]]) -> int:
    """
    INTERVIEW — Shortest path in a binary maze.

    Given an n x n grid of 0s and 1s, return the length of the shortest
    clear path from the top-left (0,0) to the bottom-right (n-1, n-1).
    A clear cell has value 0. You can move in 8 directions.
    Return -1 if no path exists.

    BFS guarantees the shortest path in an unweighted grid.
    Path length = number of cells visited (including start and end).

    Examples:
        [[0,1],[1,0]]   -> 2
        [[0,0,0],[1,1,0],[1,1,0]]  -> 4
        [[1,0,0],[1,1,0],[1,1,0]]  -> -1  (start blocked)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 8 — DYNAMIC PROGRAMMING
# =============================================================================

def dp_warmup(n: int) -> int:
    """
    WARM-UP — Climbing stairs.

    You can climb 1 or 2 steps at a time. How many distinct ways are there
    to reach the top of a staircase with n steps?

    This is Fibonacci in disguise:
        ways(1) = 1
        ways(2) = 2
        ways(n) = ways(n-1) + ways(n-2)

    Use a bottom-up table or two variables — no recursion.

    Examples:
        n=1  -> 1
        n=2  -> 2
        n=3  -> 3
        n=5  -> 8
    """
    # YOUR CODE HERE
    pass


def dp_interview(amount: int, coins: list[int]) -> int:
    """
    INTERVIEW — Coin change (minimum coins).

    Given a list of coin denominations and a target amount, return the minimum
    number of coins needed to make up that amount.
    Return -1 if it's impossible.

    Build a dp table where dp[i] = min coins to make amount i.
    Initialize dp[0] = 0 and dp[1..amount] = infinity.
    For each amount i, try every coin: dp[i] = min(dp[i], dp[i - coin] + 1).

    Examples:
        amount=11, coins=[1,2,5]   -> 3   (5+5+1)
        amount=3,  coins=[2]       -> -1
        amount=0,  coins=[1]       -> 0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 9 — STACK
# =============================================================================

def stack_warmup(s: str) -> bool:
    """
    WARM-UP — Valid parentheses.

    Given a string of brackets, return True if it is valid.
    Valid means: every opening bracket has a matching closing bracket
    in the correct order.

    Brackets: '()', '[]', '{}'

    Examples:
        "()"       -> True
        "()[]{}"   -> True
        "(]"       -> False
        "([)]"     -> False
        "{[]}"     -> True
    """
    # YOUR CODE HERE
    pass


def stack_interview(temperatures: list[int]) -> list[int]:
    """
    INTERVIEW — Daily temperatures (next warmer day).

    Given a list of daily temperatures, return a list where answer[i] is
    the number of days you have to wait after day i to get a warmer temperature.
    If no warmer day exists, answer[i] = 0.

    Use a stack of indices of days with unresolved temperatures.
    When a warmer day arrives, pop and resolve all colder days on the stack.

    Examples:
        [73,74,75,71,69,72,76,73]  -> [1,1,4,2,1,1,0,0]
        [30,40,50,60]              -> [1,1,1,0]
        [30,60,90]                 -> [1,1,0]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 10 — PREFIX SUMS
# =============================================================================

def prefix_warmup(nums: list[int], l: int, r: int) -> int:
    """
    WARM-UP — Range sum query.

    Given an array, precompute prefix sums so you can answer range queries
    in O(1). Return the sum of elements from index l to r (inclusive).

    prefix[0] = 0
    prefix[i] = prefix[i-1] + nums[i-1]
    sum(l, r) = prefix[r+1] - prefix[l]

    Examples:
        nums=[1,2,3,4,5], l=1, r=3  -> 9  (2+3+4)
        nums=[1,2,3,4,5], l=0, r=4  -> 15
        nums=[3,7,2],     l=0, r=0  -> 3
    """
    # YOUR CODE HERE
    pass


def prefix_interview(nums: list[int], k: int) -> int:
    """
    INTERVIEW — Subarray sum equals k.

    Given an array of integers and a value k, return the total number of
    contiguous subarrays whose sum equals k.

    Brute force is O(n²). Optimal approach uses prefix sums + a hash map:
    - Track running prefix sum
    - At each index, check if (prefix_sum - k) has been seen before
    - If yes, there are that many subarrays ending here with sum k

    Examples:
        [1, 1, 1], k=2   -> 2
        [1, 2, 3], k=3   -> 2   (subarrays [1,2] and [3])
        [1,-1,1],  k=1   -> 3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    results = []

    def check(name, got, expected):
        if isinstance(expected, list) and expected and isinstance(expected[0], list):
            passed = sorted(map(tuple, got)) == sorted(map(tuple, expected))
        else:
            passed = got == expected
        status = "PASS" if passed else "FAIL"
        results.append((status, name, got, expected))

    # --- Two pointers ---
    # check("two_pointers_warmup: racecar",   two_pointers_warmup("racecar"), True)
    # check("two_pointers_warmup: hello",     two_pointers_warmup("hello"),   False)
    # check("two_pointers_warmup: empty",     two_pointers_warmup(""),        True)
    # check("two_pointers_interview: [2,7,11,15] t=9",  two_pointers_interview([2,7,11,15], 9),  [1,2])
    # check("two_pointers_interview: [1, 4, 6, 8] t=10",    two_pointers_interview([1, 4, 6, 8],   10),  [2, 3])
    # check("two_pointers_interview: [-3, 0, 4, 8] t=5",    two_pointers_interview([1, 4, 6, 8],   5),  [1, 4])

    # --- Sliding window ---
    # check("sliding_window_warmup: k=3",  sliding_window_warmup([2,1,5,1,3,2], 3), 9)
    # check("sliding_window_warmup: k=2",  sliding_window_warmup([1,4,2,9],     2), 11)
    # check("sliding_window_interview: abcabcbb", sliding_window_interview("abcabcbb"), 3)
    # check("sliding_window_interview: bbbbb",    sliding_window_interview("bbbbb"),    1)
    # check("sliding_window_interview: pwwkew",   sliding_window_interview("pwwkew"),   3)

    # --- Binary search ---
    # check("binary_search_warmup: found",    binary_search_warmup([1,3,5,7,9], 5), 2)
    # check("binary_search_warmup: missing",  binary_search_warmup([1,3,5,7,9], 6), -1)
    # check("binary_search_interview: rotated hit",   binary_search_interview([4,5,6,7,0,1,2], 0), 4)
    # check("binary_search_interview: rotated miss",  binary_search_interview([4,5,6,7,0,1,2], 3), -1)
    # check("binary_search_interview: [3,1] t=1",     binary_search_interview([3,1], 1),            1)

    # --- Backtracking ---
    check("backtracking_warmup: n=2",  backtracking_warmup(2), [[], [1], [1,2], [2]])
    # check("backtracking_interview: [1,2,3]",
    #       backtracking_interview([1,2,3]),
    #       [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

    # --- Hash map ---
    # check("hashmap_warmup: [2,7,11,15]",  hashmap_warmup([2,7,11,15], 9), [0,1])
    # check("hashmap_warmup: [3,2,4]",      hashmap_warmup([3,2,4],     6), [1,2])
    # check("hashmap_interview: anagrams",
    #       hashmap_interview(["eat","tea","tan","ate","nat","bat"]),
    #       [["eat","tea","ate"],["tan","nat"],["bat"]])

    # --- DFS ---
    # g = {0:[1,2], 1:[3], 2:[3], 3:[]}
    # check("dfs_warmup",       dfs_warmup(g, 0), [0,1,3,2])
    # check("dfs_interview: 1 island",
    #       dfs_interview([["1","1","1","1","0"],["1","1","0","1","0"],
    #                      ["1","1","0","0","0"],["0","0","0","0","0"]]), 1)
    # check("dfs_interview: 3 islands",
    #       dfs_interview([["1","1","0","0","0"],["1","1","0","0","0"],
    #                      ["0","0","1","0","0"],["0","0","0","1","1"]]), 3)

    # --- BFS ---
    # check("bfs_warmup",       bfs_warmup(g, 0), [0,1,2,3])
    # check("bfs_interview: path=2",  bfs_interview([[0,1],[1,0]]),              2)
    # check("bfs_interview: path=4",  bfs_interview([[0,0,0],[1,1,0],[1,1,0]]), 4)
    # check("bfs_interview: no path", bfs_interview([[1,0,0],[1,1,0],[1,1,0]]), -1)

    # --- DP ---
    # check("dp_warmup: n=1",  dp_warmup(1), 1)
    # check("dp_warmup: n=5",  dp_warmup(5), 8)
    # check("dp_interview: 11 coins=[1,2,5]", dp_interview(11, [1,2,5]), 3)
    # check("dp_interview: 3  coins=[2]",     dp_interview(3,  [2]),     -1)
    # check("dp_interview: 0  coins=[1]",     dp_interview(0,  [1]),     0)

    # --- Stack ---
    # check("stack_warmup: ()",      stack_warmup("()"),     True)
    # check("stack_warmup: (]",      stack_warmup("(]"),     False)
    # check("stack_warmup: {[]}",    stack_warmup("{[]}"),   True)
    # check("stack_interview: temps", stack_interview([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    # check("stack_interview: asc",   stack_interview([30,40,50,60]),             [1,1,1,0])

    # --- Prefix sums ---
    # check("prefix_warmup: l=1 r=3", prefix_warmup([1,2,3,4,5], 1, 3), 9)
    # check("prefix_warmup: l=0 r=4", prefix_warmup([1,2,3,4,5], 0, 4), 15)
    # check("prefix_interview: k=2",  prefix_interview([1,1,1], 2), 2)
    # check("prefix_interview: k=3",  prefix_interview([1,2,3], 3), 2)

    # --- Print summary ---
    passed = sum(1 for r in results if r[0] == "PASS")
    total  = len(results)
    print(f"\n{'='*60}")
    print(f"  Results: {passed}/{total} passed")
    print(f"{'='*60}")
    for status, name, got, expected in results:
        if status == "FAIL":
            print(f"  FAIL  {name}")
            print(f"        got:      {got}")
            print(f"        expected: {expected}")
    if passed == total:
        print("  All tests passed!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    run_tests()