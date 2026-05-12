# =============================================================================
# ALGORITHMIC PATTERNS — PROBABLE INTERVIEW EXERCISES
# 10 patterns likely to appear depending on level and company
# =============================================================================
# HOW TO USE
# ----------
# Each exercise has:
#   - A docstring explaining the problem and examples
#   - A function stub to complete
#   - A run_tests() call at the bottom to check your answers
#
# Run the full file:   python pattern_exercises_probable.py
# Run one section:     comment out the run_tests() calls you don't want
# =============================================================================

import heapq
from collections import deque, defaultdict


# =============================================================================
# PATTERN 1 — HEAP / PRIORITY QUEUE
# =============================================================================

def heap_warmup(nums: list[int], k: int) -> list[int]:
    """
    WARM-UP — Return the k largest elements in any order.

    Use Python's heapq module. Since heapq is a min-heap by default,
    maintain a heap of size k: push each element, pop when size exceeds k.
    What remains is the k largest.

    Do NOT sort the array — that would be O(n log n).
    This approach is O(n log k).

    Examples:
        [3, 1, 5, 12, 2, 11], k=3  -> [5, 11, 12]  (any order)
        [1, 2],               k=1  -> [2]
        [5, 5, 5],            k=2  -> [5, 5]
    """
    # YOUR CODE HERE
    pass


def heap_interview(nums: list[int]) -> float:
    """
    INTERVIEW — Median of a data stream.

    Design a structure that processes numbers one by one and returns
    the running median after each insertion. For this exercise, process
    the full list and return only the final median.

    Approach: maintain two heaps —
      - a max-heap for the lower half  (invert sign for Python's min-heap)
      - a min-heap for the upper half

    Keep them balanced (size difference <= 1).
    Median = top of the larger heap, or average of both tops if equal size.

    Examples:
        [1, 2]        -> 1.5
        [1, 2, 3]     -> 2.0
        [5, 3, 8, 4]  -> 4.5
        [1]           -> 1.0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 2 — FAST & SLOW POINTERS
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals, node = [], self
        while node:
            vals.append(str(node.val))
            node = node.next
        return " -> ".join(vals)


def make_list(values: list[int], cycle_pos: int = -1) -> ListNode:
    """Helper: build a linked list, optionally with a cycle at cycle_pos."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


def fast_slow_warmup(head: ListNode) -> bool:
    """
    WARM-UP — Detect a cycle in a linked list.

    Use two pointers: slow moves 1 step, fast moves 2 steps.
    If they ever meet, there is a cycle.
    If fast reaches None, there is no cycle.

    Examples:
        1 -> 2 -> 3 -> 4 -> (back to 2)  -> True
        1 -> 2 -> 3 -> None               -> False
        1 -> (back to 1)                  -> True
    """
    # YOUR CODE HERE
    pass


def fast_slow_interview(head: ListNode) -> ListNode:
    """
    INTERVIEW — Find the start node of a cycle in a linked list.

    If no cycle exists, return None.

    Phase 1: detect the meeting point using fast & slow pointers.
    Phase 2: reset one pointer to head. Move both one step at a time.
             They will meet exactly at the cycle entry node.

    This is Floyd's cycle detection algorithm.

    Examples:
        1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)  -> node with val=3
        1 -> 2 -> 3 -> None                    -> None
        1 -> (back to 1)                        -> node with val=1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 3 — MERGE INTERVALS
# =============================================================================

def merge_intervals_warmup(intervals: list[list[int]]) -> list[list[int]]:
    """
    WARM-UP — Merge all overlapping intervals.

    Given a list of [start, end] intervals, merge any that overlap
    and return the result sorted by start.

    Two intervals [a, b] and [c, d] overlap if c <= b.

    Step 1: sort by start.
    Step 2: iterate — if current start <= last merged end, extend.
            Otherwise, start a new interval.

    Examples:
        [[1,3],[2,6],[8,10],[15,18]]  -> [[1,6],[8,10],[15,18]]
        [[1,4],[4,5]]                 -> [[1,5]]
        [[1,4],[2,3]]                 -> [[1,4]]
    """
    # YOUR CODE HERE
    pass


def merge_intervals_interview(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    INTERVIEW — Insert a new interval into a sorted, non-overlapping list.

    Given a list of non-overlapping intervals sorted by start, insert
    new_interval and merge if necessary. Return the updated list.

    Three phases:
      1. Add all intervals that end before new_interval starts.
      2. Merge all intervals that overlap with new_interval.
      3. Add the rest as-is.

    Examples:
        [[1,3],[6,9]], new=[2,5]          -> [[1,5],[6,9]]
        [[1,2],[3,5],[6,7],[8,10],[12,16]], new=[4,8]  -> [[1,2],[3,10]]
        [], new=[5,7]                     -> [[5,7]]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 4 — MONOTONIC STACK
# =============================================================================

def monotonic_warmup(nums: list[int]) -> list[int]:
    """
    WARM-UP — Next greater element.

    For each element in nums, find the next element to its right that is
    strictly greater. If none exists, use -1.

    Use a monotonic decreasing stack: store indices of elements waiting
    for their next greater. When a greater element arrives, pop and resolve.

    Examples:
        [2, 1, 2, 4, 3]   -> [4, 2, 4, -1, -1]
        [1, 2, 3, 4]      -> [2, 3, 4, -1]
        [4, 3, 2, 1]      -> [-1, -1, -1, -1]
    """
    # YOUR CODE HERE
    pass


def monotonic_interview(temperatures: list[int]) -> list[int]:
    """
    INTERVIEW — Daily temperatures (days until warmer).

    Given daily temperatures, return an array where answer[i] is the
    number of days after day i before a warmer temperature occurs.
    If no warmer day exists, answer[i] = 0.

    Use a monotonic stack of indices. When today is warmer than the
    stack top, pop and compute the gap.

    Note: this is a classic interview problem — implement it cleanly
    from scratch without referring to a previous solution.

    Examples:
        [73,74,75,71,69,72,76,73]  -> [1,1,4,2,1,1,0,0]
        [30,40,50,60]              -> [1,1,1,0]
        [30,60,90]                 -> [1,1,0]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 5 — TRIE (PREFIX TREE)
# =============================================================================

class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class Trie:
    """
    WARM-UP — Implement a trie with insert, search, and startsWith.

    insert(word):     insert word into the trie
    search(word):     return True if word is in the trie
    startsWith(prefix): return True if any word starts with prefix

    Example usage:
        t = Trie()
        t.insert("apple")
        t.search("apple")    -> True
        t.search("app")      -> False
        t.startsWith("app")  -> True
        t.insert("app")
        t.search("app")      -> True
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # YOUR CODE HERE
        pass

    def search(self, word: str) -> bool:
        # YOUR CODE HERE
        pass

    def startsWith(self, prefix: str) -> bool:
        # YOUR CODE HERE
        pass


def trie_interview(words: list[str], prefix: str) -> list[str]:
    """
    INTERVIEW — Autocomplete: return all words with a given prefix.

    Build a trie from words, navigate to the end of prefix, then
    collect all words reachable from that node using DFS.
    Return results in alphabetical order.

    Examples:
        words=["apple","app","application","banana"], prefix="app"
            -> ["app", "apple", "application"]
        words=["dog","door","cat"], prefix="do"
            -> ["dog", "door"]
        words=["hello"], prefix="world"
            -> []
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 6 — UNION-FIND (DISJOINT SET UNION)
# =============================================================================

class UnionFind:
    """
    WARM-UP — Implement Union-Find with path compression and union by rank.

    find(x):    return the root representative of x's group
    union(x,y): merge the groups containing x and y
                return False if they were already in the same group

    Path compression: make every node point directly to root during find.
    Union by rank:    attach smaller tree under larger tree root.

    Example:
        uf = UnionFind(5)
        uf.union(0, 1)  -> True
        uf.union(1, 2)  -> True
        uf.union(0, 2)  -> False  (already connected)
        uf.find(2) == uf.find(0)  -> True
    """

    def __init__(self, n: int):
        # YOUR CODE HERE
        pass

    def find(self, x: int) -> int:
        # YOUR CODE HERE
        pass

    def union(self, x: int, y: int) -> bool:
        # YOUR CODE HERE
        pass


def union_find_interview(n: int, edges: list[list[int]]) -> int:
    """
    INTERVIEW — Number of connected components in an undirected graph.

    Given n nodes (0 to n-1) and a list of edges, return the number
    of connected components.

    Use UnionFind: start with n components, decrement each time two
    nodes from different components are successfully merged.

    Examples:
        n=5, edges=[[0,1],[1,2],[3,4]]       -> 2
        n=5, edges=[[0,1],[1,2],[2,3],[3,4]] -> 1
        n=3, edges=[]                         -> 3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 7 — GREEDY
# =============================================================================

def greedy_warmup(nums: list[int]) -> bool:
    """
    WARM-UP — Jump game.

    Given an array where nums[i] is the maximum jump length from index i,
    return True if you can reach the last index starting from index 0.

    Greedy: track the farthest reachable index at each step.
    If you're ever at a position beyond the current farthest, return False.

    Examples:
        [2, 3, 1, 1, 4]  -> True
        [3, 2, 1, 0, 4]  -> False
        [0]              -> True
        [1, 0, 2]        -> False
    """
    # YOUR CODE HERE
    pass


def greedy_interview(intervals: list[list[int]]) -> int:
    """
    INTERVIEW — Minimum number of meeting rooms required.

    Given a list of meeting [start, end] intervals, return the minimum
    number of rooms needed to hold all meetings simultaneously.

    Greedy with a min-heap:
      - Sort meetings by start time.
      - Use a heap of end times (one entry per room in use).
      - For each meeting: if the earliest-ending room is free, reuse it (pop).
      - Always push the current meeting's end time.
      - Heap size at the end = rooms needed.

    Examples:
        [[0,30],[5,10],[15,20]]  -> 2
        [[7,10],[2,4]]           -> 1
        [[1,5],[2,6],[3,7]]      -> 3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 8 — TOP K ELEMENTS
# =============================================================================

def top_k_warmup(nums: list[int], k: int) -> int:
    """
    WARM-UP — Kth largest element in an array.

    Return the kth largest element (not kth distinct).
    Use a min-heap of size k: the top of the heap is the kth largest.

    Examples:
        [3,2,1,5,6,4], k=2  -> 5
        [3,2,3,1,2,4,5,5,6], k=4  -> 4
        [1], k=1  -> 1
    """
    # YOUR CODE HERE
    pass


def top_k_interview(words: list[str], k: int) -> list[str]:
    """
    INTERVIEW — Top k frequent words.

    Given a list of words, return the k most frequent words sorted by
    frequency (descending). Break ties alphabetically (ascending).

    Approach: count frequencies, then use a heap.
    For the heap comparison, use (-count, word) so the most frequent
    word sorts first, and ties break alphabetically.

    Examples:
        ["i","love","leetcode","i","love","coding"], k=2
            -> ["i","love"]
        ["the","day","is","sunny","the","the","the","sunny","is","is"], k=4
            -> ["the","is","sunny","day"]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 9 — TREE TRAVERSALS
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(values: list) -> TreeNode:
    """Helper: build a binary tree from level-order list (None = missing node)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_traversal_warmup(root: TreeNode) -> bool:
    """
    WARM-UP — Validate a binary search tree.

    A valid BST requires that every node in the left subtree is strictly
    less than the node, and every node in the right subtree is strictly
    greater — not just immediate children, but the entire subtree.

    Use recursive DFS passing down valid (min, max) bounds.
    At each node, check: min < node.val < max.

    Examples:
        Tree [2,1,3]              -> True
        Tree [5,1,4,None,None,3,6]-> False  (4 is in right subtree of 5 but 4 < 5)
        Tree [1]                  -> True
    """
    # YOUR CODE HERE
    pass


def tree_traversal_interview(root: TreeNode) -> TreeNode:
    """
    INTERVIEW — Lowest common ancestor (LCA) of a binary tree.

    Given a binary tree (not necessarily a BST) and two nodes p and q,
    return their lowest common ancestor — the deepest node that has
    both p and q as descendants (a node can be a descendant of itself).

    Recursive insight: if root is p or q, return root.
    Otherwise recurse left and right. If both return non-None, root is the LCA.
    If only one side returns non-None, that side contains the answer.

    For this exercise, p and q are passed as integer values.
    Return the LCA node.

    Examples:
        Tree [3,5,1,6,2,0,8], p=5, q=1  -> node(3)
        Tree [3,5,1,6,2,0,8], p=5, q=4  -> node(5)  (5 is ancestor of 4)
        Tree [1,2], p=1, q=2            -> node(1)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PATTERN 10 — BIT MANIPULATION
# =============================================================================

def bit_warmup(nums: list[int]) -> int:
    """
    WARM-UP — Single number.

    Every element in the array appears exactly twice, except for one.
    Find that single element.

    Key insight: XOR of a number with itself is 0. XOR with 0 is the number.
    XOR all elements together — pairs cancel out, leaving the single element.
    O(n) time, O(1) space.

    Examples:
        [2, 2, 1]       -> 1
        [4, 1, 2, 1, 2] -> 4
        [1]             -> 1
    """
    # YOUR CODE HERE
    pass


def bit_interview(n: int) -> int:
    """
    INTERVIEW — Count total set bits from 1 to n (inclusive).

    Return the total number of '1' bits across the binary representations
    of all integers from 1 to n.

    Naive approach: loop and count bits per number — O(n log n).
    Optimal approach: for each bit position b (0, 1, 2, ...),
    count how many numbers in [1, n] have that bit set using the formula:
        cycle = 2 ** (b + 1)
        full_cycles = (n + 1) // cycle
        remainder = max(0, (n + 1) % cycle - 2**b)
        contribution = full_cycles * 2**b + remainder

    Implement either approach (the naive version passes all tests too).

    Examples:
        n=1   -> 1   (just "1")
        n=4   -> 5   (1, 10, 11, 100 -> 1+1+2+1 = 5)
        n=7   -> 12  (1+1+2+1+2+2+3 = 12)
        n=10  -> 17
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
        elif isinstance(expected, list):
            passed = got == expected
        else:
            passed = got == expected
        results.append(("PASS" if passed else "FAIL", name, got, expected))

    # --- Heap ---
    check("heap_warmup: k=3",
          sorted(heap_warmup([3,1,5,12,2,11], 3)), [5,11,12])
    check("heap_warmup: k=1",
          heap_warmup([1,2], 1), [2])
    check("heap_interview: [1,2]",      heap_interview([1,2]),       1.5)
    check("heap_interview: [1,2,3]",    heap_interview([1,2,3]),     2.0)
    check("heap_interview: [5,3,8,4]",  heap_interview([5,3,8,4]),   4.5)

    # --- Fast & slow pointers ---
    check("fast_slow_warmup: cycle",    fast_slow_warmup(make_list([1,2,3,4], 1)),  True)
    check("fast_slow_warmup: no cycle", fast_slow_warmup(make_list([1,2,3])),       False)
    cycle_list = make_list([1,2,3,4,5], 2)
    lca_node   = fast_slow_interview(cycle_list)
    check("fast_slow_interview: entry=3",  lca_node.val if lca_node else None, 3)
    check("fast_slow_interview: no cycle", fast_slow_interview(make_list([1,2,3])), None)

    # --- Merge intervals ---
    check("merge_intervals_warmup: basic",
          merge_intervals_warmup([[1,3],[2,6],[8,10],[15,18]]),
          [[1,6],[8,10],[15,18]])
    check("merge_intervals_warmup: touching",
          merge_intervals_warmup([[1,4],[4,5]]), [[1,5]])
    check("merge_intervals_interview: overlap",
          merge_intervals_interview([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
    check("merge_intervals_interview: multi",
          merge_intervals_interview([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
          [[1,2],[3,10],[12,16]])

    # --- Monotonic stack ---
    check("monotonic_warmup: mixed",
          monotonic_warmup([2,1,2,4,3]), [4,2,4,-1,-1])
    check("monotonic_warmup: ascending",
          monotonic_warmup([1,2,3,4]),   [2,3,4,-1])
    check("monotonic_interview: classic",
          monotonic_interview([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    check("monotonic_interview: ascending",
          monotonic_interview([30,40,50,60]), [1,1,1,0])

    # --- Trie ---
    t = Trie()
    t.insert("apple")
    check("trie_warmup: search apple",     t.search("apple"),    True)
    check("trie_warmup: search app",       t.search("app"),      False)
    check("trie_warmup: startsWith app",   t.startsWith("app"),  True)
    t.insert("app")
    check("trie_warmup: search app after insert", t.search("app"), True)
    check("trie_interview: prefix app",
          trie_interview(["apple","app","application","banana"], "app"),
          ["app","apple","application"])
    check("trie_interview: no match",
          trie_interview(["hello"], "world"), [])

    # --- Union-Find ---
    uf = UnionFind(5)
    check("union_find_warmup: new union",  uf.union(0,1), True)
    check("union_find_warmup: new union",  uf.union(1,2), True)
    check("union_find_warmup: same group", uf.union(0,2), False)
    check("union_find_interview: 2 components",
          union_find_interview(5, [[0,1],[1,2],[3,4]]), 2)
    check("union_find_interview: 1 component",
          union_find_interview(5, [[0,1],[1,2],[2,3],[3,4]]), 1)
    check("union_find_interview: no edges",
          union_find_interview(3, []), 3)

    # --- Greedy ---
    check("greedy_warmup: can reach",    greedy_warmup([2,3,1,1,4]), True)
    check("greedy_warmup: cannot reach", greedy_warmup([3,2,1,0,4]), False)
    check("greedy_warmup: single",       greedy_warmup([0]),         True)
    check("greedy_interview: 2 rooms",   greedy_interview([[0,30],[5,10],[15,20]]), 2)
    check("greedy_interview: 1 room",    greedy_interview([[7,10],[2,4]]),          1)
    check("greedy_interview: 3 rooms",   greedy_interview([[1,5],[2,6],[3,7]]),     3)

    # --- Top K ---
    check("top_k_warmup: k=2", top_k_warmup([3,2,1,5,6,4], 2), 5)
    check("top_k_warmup: k=4", top_k_warmup([3,2,3,1,2,4,5,5,6], 4), 4)
    check("top_k_interview: k=2",
          top_k_interview(["i","love","leetcode","i","love","coding"], 2),
          ["i","love"])
    check("top_k_interview: k=4",
          top_k_interview(["the","day","is","sunny","the","the","the","sunny","is","is"], 4),
          ["the","is","sunny","day"])

    # --- Tree traversals ---
    check("tree_traversal_warmup: valid BST",
          tree_traversal_warmup(make_tree([2,1,3])), True)
    check("tree_traversal_warmup: invalid BST",
          tree_traversal_warmup(make_tree([5,1,4,None,None,3,6])), False)
    lca_tree = make_tree([3,5,1,6,2,0,8,None,None,7,4])
    lca_result = tree_traversal_interview(lca_tree, 5, 1)
    check("tree_traversal_interview: LCA(5,1)=3",
          lca_result.val if lca_result else None, 3)
    lca_result2 = tree_traversal_interview(lca_tree, 5, 4)
    check("tree_traversal_interview: LCA(5,4)=5",
          lca_result2.val if lca_result2 else None, 5)

    # --- Bit manipulation ---
    check("bit_warmup: [2,2,1]",       bit_warmup([2,2,1]),       1)
    check("bit_warmup: [4,1,2,1,2]",   bit_warmup([4,1,2,1,2]),   4)
    check("bit_interview: n=1",        bit_interview(1),           1)
    check("bit_interview: n=4",        bit_interview(4),           5)
    check("bit_interview: n=7",        bit_interview(7),           12)
    check("bit_interview: n=10",       bit_interview(10),          17)

    # --- Summary ---
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