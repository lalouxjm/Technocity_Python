# =============================================================================
#  DATA STRUCTURES — Practice Exercises
#
#  Instructions:
#    - Each function is defined but intentionally left empty.
#    - Read the docstring carefully: it tells you WHAT to do and gives a hint
#      on WHICH data structure to use and WHY.
#    - Run the file at any time, the test suite at the bottom will tell you
#      which exercises pass and which still need work.
#    - Do NOT change function names or signatures.
#
#  Difficulty: ★★☆  (entry-level interview, first approach)
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — ARRAY / LIST
# ─────────────────────────────────────────────────────────────────────────────

def rotate_array(nums: list, k: int) -> list:
    """
    Rotate a list to the right by k steps.

    Example:
        rotate_array([1, 2, 3, 4, 5], 2)  →  [4, 5, 1, 2, 3]
        rotate_array([1, 2, 3], 1)         →  [3, 1, 2]

    Hint: Think about slicing. With an array you can access any
    sub-section in one operation. Watch out for k > len(nums).

    Complexity target: O(n) time, O(n) space.
    """
    pass


def two_sum(nums: list, target: int) -> list:
    """
    Given a list of integers, return the INDICES of the two numbers
    that add up to target. You may assume exactly one solution exists.

    Example:
        two_sum([2, 7, 11, 15], 9)   →  [0, 1]   (2 + 7 = 9)
        two_sum([3, 2, 4], 6)        →  [1, 2]   (2 + 4 = 6)

    Hint: A first pass with a nested loop works but is O(n²).
          Can you do it in one pass using a structure that gives O(1) lookup?
          Store what you've SEEN so far as you iterate.

    Complexity target: O(n) time, O(n) space.
    """
    #pass

    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s > target:
            right -= 1
        else:
            left += 1


def running_max(nums: list) -> list:
    """
    Return a new list where each element is the maximum value
    seen so far (from the start up to and including that index).

    Example:
        running_max([3, 1, 4, 1, 5, 9, 2])  →  [3, 3, 4, 4, 5, 9, 9]
        running_max([5, 4, 3])               →  [5, 5, 5]

    Hint: A single pass over the array is enough. Keep track of
          the current max as you go and append to a result list.

    Complexity target: O(n) time, O(n) space.
    """
    pass
    """max_list = []
    for i, j in nums:
        max_list.append(max(i, j))
    return max_list"""

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — HASH TABLE (dict / set)
# ─────────────────────────────────────────────────────────────────────────────

def first_unique_char(s: str) -> int:
    """
    Given a string, return the index of the first character that
    does not repeat. Return -1 if no such character exists.

    Example:
        first_unique_char("leetcode")   →  0   ('l' appears once)
        first_unique_char("aabb")       →  -1
        first_unique_char("aabbc")      →  4   ('c' appears once)

    Hint: Count frequencies in one pass (dict), then find the first
          character whose count is 1 in a second pass.
          Two O(n) passes is still O(n) overall.

    Complexity target: O(n) time, O(n) space.
    """
    pass
    """temp = ""
    first_unique = ""
    for u in s:
        if u not in temp:
            temp += u
            first_unique += u
        else:"""


def has_duplicate(nums: list) -> bool:
    """
    Return True if any value appears more than once, False otherwise.

    Example:
        has_duplicate([1, 2, 3, 1])   →  True
        has_duplicate([1, 2, 3, 4])   →  False

    Hint: A set only stores unique values. Think about what it means
          when the set size differs from the list size — or stop early
          the moment you see a value you've already encountered.

    Complexity target: O(n) time, O(n) space.
    """
    pass

    set_list = set(nums)
    if len(set_list) != len(nums):
        return True
    else:
        return False

def group_anagrams(words: list) -> list:
    """
    Group words that are anagrams of each other.
    The order of groups and words inside groups does not matter.

    Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        →  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    Hint: Two words are anagrams if they have the same letters in the
          same quantities — i.e. their SORTED characters are identical.
          Use a dict where the key is the sorted word.

    Complexity target: O(n * k log k) where k = average word length.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — STACK
# ─────────────────────────────────────────────────────────────────────────────

def is_balanced(s: str) -> bool:
    """
    Return True if every opening bracket has a matching closing bracket
    in the correct order. Brackets: (), [], {}

    Example:
        is_balanced("([]{})")   →  True
        is_balanced("([)]")     →  False
        is_balanced("{[]}")     →  True
        is_balanced("(")        →  False

    Hint: When you see an opening bracket, PUSH it. When you see a
          closing bracket, POP and check if it matches.
          If the stack is empty when you need to pop → unbalanced.

    Complexity target: O(n) time, O(n) space.
    """
    pass


def evaluate_rpn(tokens: list) -> int:
    """
    Evaluate an expression given in Reverse Polish Notation (RPN).
    Operators: '+', '-', '*', '//' (integer division, truncate toward zero).
    You can assume the expression is always valid.

    Example:
        evaluate_rpn(["2", "1", "+", "3", "*"])   →  9   ((2+1)*3)
        evaluate_rpn(["4", "13", "5", "/", "+"])  →  6   (4+(13/5))

    Hint: Push numbers onto a stack. When you see an operator,
          pop TWO values, apply the operator, and push the result back.
          The final answer is the last value left on the stack.

    Complexity target: O(n) time, O(n) space.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — QUEUE
# ─────────────────────────────────────────────────────────────────────────────

def moving_average(stream: list, window: int) -> list:
    """
    Given a stream of integers and a window size, return the list of
    moving averages at each step (average of the last `window` numbers).
    Round each average to 2 decimal places.

    Example:
        moving_average([1, 10, 3, 5], 3)
        →  [1.0, 5.5, 4.67, 6.0]
        Explanation: [1]/1=1.0, [1,10]/2=5.5, [1,10,3]/3=4.67, [10,3,5]/3=6.0

    Hint: Use a deque with maxlen=window. It auto-discards the oldest
          value when full — you don't need to manage that yourself.

    Complexity target: O(n) time, O(window) space.
    """
    pass


def bfs_levels(graph: dict, start: str) -> list:
    """
    Given an adjacency list (dict), return a list of lists where each
    inner list contains the nodes at that BFS level (distance from start).

    Example:
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": []}
        bfs_levels(graph, "A")
        →  [["A"], ["B", "C"], ["D", "E"]]

    Hint: Use a queue. Process all nodes of the current level before
          moving on — use len(queue) at the start of each level to know
          exactly how many nodes belong to that level.

    Complexity target: O(V + E) time, O(V) space.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — LINKED LIST (using collections.deque)
# ─────────────────────────────────────────────────────────────────────────────

from collections import deque

def is_palindrome_deque(s: str) -> bool:
    """
    Return True if the string is a palindrome (reads the same forwards
    and backwards), ignoring spaces and case. Use a deque to solve it.

    Example:
        is_palindrome_deque("racecar")          →  True
        is_palindrome_deque("A man a plan a canal Panama")  →  True
        is_palindrome_deque("hello")            →  False

    Hint: Load the cleaned characters into a deque. Then repeatedly
          popleft() and pop() and compare the two ends until the deque
          has 0 or 1 characters left.

    Complexity target: O(n) time, O(n) space.
    """
    pass


def simulate_hot_potato(names: list, count: int) -> str:
    """
    Simulate the Hot Potato game: players sit in a circle, the potato is
    passed `count` times, and the player holding it is eliminated.
    Repeat until one player remains — return their name.

    Example:
        simulate_hot_potato(["Alice", "Bob", "Carol", "Dave"], 3)
        →  "Alice"   (elimination order: Dave, Carol, Bob)

    Hint: A queue perfectly models a circle. To "pass" the potato,
          dequeue from the front and re-enqueue at the back.
          After `count` passes, dequeue (and discard) the current holder.

    Complexity target: O(n * count) time, O(n) space.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6 — TREE
# ─────────────────────────────────────────────────────────────────────────────

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """
    Return the maximum depth (number of nodes along the longest path
    from root to a leaf node) of a binary tree.

    Example — for this tree:
            3
           / \\
          9  20
             / \\
            15   7
        max_depth → 3

    Hint: Think recursively. The depth of a node is 1 + the max depth
          of its two subtrees. The depth of None is 0.

    Complexity target: O(n) time, O(h) space (h = height).
    """
    pass


def inorder_traversal(root: TreeNode) -> list:
    """
    Return the inorder traversal (left → node → right) of a binary tree
    as a flat list of values.
    Implement it ITERATIVELY (no recursion) using a stack.

    Example — for this tree:
            1
             \\
              2
             /
            3
        inorder_traversal → [1, 3, 2]

    Hint: Use a stack. Go as far left as possible, pushing nodes.
          When you can't go left, pop, record the value, then go right.

    Complexity target: O(n) time, O(n) space.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 7 — HEAP
# ─────────────────────────────────────────────────────────────────────────────

import heapq

def k_largest(nums: list, k: int) -> list:
    """
    Return the k largest elements from a list, in descending order.

    Example:
        k_largest([3, 1, 5, 12, 2, 11], 3)   →  [12, 11, 5]
        k_largest([7, 4, 6, 2], 2)            →  [7, 6]

    Hint: heapq.nlargest() exists but try it manually:
          maintain a MIN-heap of size k. For each number, if it's larger
          than the heap's minimum (heap[0]), push it and pop the minimum.
          A min-heap of size k always holds the k largest seen so far.

    Complexity target: O(n log k) time, O(k) space.
    """
    pass


def find_median_stream(stream: list) -> list:
    """
    Given a stream of integers arriving one by one, return the list of
    medians after each new number is inserted.

    Example:
        find_median_stream([5, 15, 1, 3])  →  [5, 10.0, 5, 4.0]
        Explanation: [5]→5, [5,15]→10.0, [1,5,15]→5, [1,3,5,15]→4.0

    Hint: Use TWO heaps — a max-heap for the lower half and a min-heap
          for the upper half. Keep them balanced (size difference ≤ 1).
          Python only has min-heap, so negate values to simulate max-heap.
          Median = top of the larger heap, or average of both tops.

    Complexity target: O(n log n) time, O(n) space.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 8 — GRAPH
# ─────────────────────────────────────────────────────────────────────────────

def has_cycle(graph: dict) -> bool:
    """
    Given a DIRECTED graph as an adjacency list, return True if the
    graph contains a cycle, False otherwise.

    Example:
        has_cycle({"A": ["B"], "B": ["C"], "C": ["A"]})   →  True
        has_cycle({"A": ["B"], "B": ["C"], "C": []})       →  False

    Hint: Use DFS with a "currently in recursion stack" set (often called
          `visiting`). If you reach a node that is already in `visiting`,
          you've found a cycle.
          Use a `visited` set to avoid re-processing finished nodes.

    Complexity target: O(V + E) time, O(V) space.
    """
    pass


def number_of_islands(grid: list) -> int:
    """
    Given a 2D grid of '1's (land) and '0's (water), count the number
    of islands. An island is surrounded by water and formed by connecting
    adjacent land cells horizontally or vertically.

    Example:
        grid = [
            ["1", "1", "0", "0"],
            ["1", "1", "0", "0"],
            ["0", "0", "1", "0"],
            ["0", "0", "0", "1"],
        ]
        number_of_islands(grid)  →  3

    Hint: Iterate every cell. When you find a '1', increment the count
          and use BFS/DFS to "sink" all connected land cells (mark as '0')
          so you don't count them again.

    Complexity target: O(m * n) time, O(m * n) space.
    """
    pass


# =============================================================================
#  TEST SUITE — Do not modify below this line.
#  Run:  python data_structures_exercises.py
# =============================================================================

def _build_tree():
    """Helper: build the tree used in tree tests."""
    root        = TreeNode(3)
    root.left   = TreeNode(9)
    root.right  = TreeNode(20)
    root.right.left  = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def _build_inorder_tree():
    """Helper: build 1 -> None, 2 (left=3)"""
    root       = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root

def run_tests():
    results = []

    def check(name, got, expected):
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

    # ── Array / List ──────────────────────────────────────────────
    print("\n[Array / List]")
    check("rotate_array basic",      rotate_array([1,2,3,4,5], 2),  [4,5,1,2,3])
    check("rotate_array k=1",        rotate_array([1,2,3], 1),      [3,1,2])
    check("rotate_array k>len",      rotate_array([1,2,3], 5),      [2,3,1])
    check("two_sum basic",           two_sum([2,7,11,15], 9),       [0,1])
    check("two_sum not first",       two_sum([3,2,4], 6),           [1,2])
    check("running_max asc",         running_max([1,2,3,4]),        [1,2,3,4])
    check("running_max mixed",       running_max([3,1,4,1,5,9,2]), [3,3,4,4,5,9,9])

    # ── Hash Table ────────────────────────────────────────────────
    print("\n[Hash Table]")
    check("first_unique_char found",    first_unique_char("leetcode"),  0)
    check("first_unique_char not found",first_unique_char("aabb"),     -1)
    check("first_unique_char end",      first_unique_char("aabbc"),     4)
    check("has_duplicate True",         has_duplicate([1,2,3,1]),       True)
    check("has_duplicate False",        has_duplicate([1,2,3,4]),       False)
    ga = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    ga_sorted = sorted([sorted(g) for g in ga]) if ga else None
    check("group_anagrams",
          ga_sorted,
          [["ate","eat","tea"], ["bat"], ["nat","tan"]])

    # ── Stack ─────────────────────────────────────────────────────
    print("\n[Stack]")
    check("is_balanced true",    is_balanced("([]{})"),  True)
    check("is_balanced false",   is_balanced("([)]"),    False)
    check("is_balanced open",    is_balanced("("),       False)
    check("evaluate_rpn ex1",    evaluate_rpn(["2","1","+","3","*"]),    9)
    check("evaluate_rpn ex2",    evaluate_rpn(["4","13","5","/","+"]),   6)

    # ── Queue ─────────────────────────────────────────────────────
    print("\n[Queue]")
    check("moving_average",
          moving_average([1,10,3,5], 3),
          [1.0, 5.5, 4.67, 6.0])
    graph_bfs = {"A":["B","C"],"B":["D"],"C":["D","E"],"D":[],"E":[]}
    levels = bfs_levels(graph_bfs, "A")
    check("bfs_levels",
          [sorted(l) for l in levels] if levels else None,
          [["A"], ["B","C"], ["D","E"]])

    # ── Linked List / Deque ───────────────────────────────────────
    print("\n[Linked List / Deque]")
    check("is_palindrome true",   is_palindrome_deque("racecar"),                      True)
    check("is_palindrome spaces", is_palindrome_deque("A man a plan a canal Panama"),  True)
    check("is_palindrome false",  is_palindrome_deque("hello"),                        False)
    check("hot_potato",           simulate_hot_potato(["Alice","Bob","Carol","Dave"], 3), "Alice")

    # ── Tree ──────────────────────────────────────────────────────
    print("\n[Tree]")
    check("max_depth",         max_depth(_build_tree()),        3)
    check("max_depth None",    max_depth(None),                 0)
    check("inorder iterative", inorder_traversal(_build_inorder_tree()), [1,3,2])

    # ── Heap ──────────────────────────────────────────────────────
    print("\n[Heap]")
    check("k_largest basic",  k_largest([3,1,5,12,2,11], 3),  [12,11,5])
    check("k_largest small",  k_largest([7,4,6,2], 2),         [7,6])
    check("median stream",    find_median_stream([5,15,1,3]),  [5, 10.0, 5, 4.0])

    # ── Graph ─────────────────────────────────────────────────────
    print("\n[Graph]")
    check("has_cycle true",
          has_cycle({"A":["B"],"B":["C"],"C":["A"]}),   True)
    check("has_cycle false",
          has_cycle({"A":["B"],"B":["C"],"C":[]}),       False)
    grid = [["1","1","0","0"],
            ["1","1","0","0"],
            ["0","0","1","0"],
            ["0","0","0","1"]]
    check("number_of_islands", number_of_islands(grid), 3)

    # ── Summary ───────────────────────────────────────────────────
    passed = sum(results)
    total  = len(results)
    print("\n" + "=" * 60)
    print(f" {passed}/{total} tests passed", "🎉" if passed == total else "💪 Keep going!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_tests()
