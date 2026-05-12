# =============================================================================
#  FUNDAMENTAL DATA STRUCTURES — Summary & Examples
#  Each section covers: what it is, complexity, and 3 concrete use-case examples
# =============================================================================

# =============================================================================
# 1. ARRAY / LIST
#    - Contiguous memory, dynamic resize (x2 when full)
#    - Access: O(1) | Insert end: O(1) amortized | Insert middle: O(n) | Delete: O(n)
# =============================================================================

print("=" * 60)
print("1. ARRAY / LIST")
print("=" * 60)

# --- Example 1: Leaderboard (indexed access) ---
# Use case: You need instant access to a player's score by rank.
# O(1) access by index makes arrays ideal for ranked/ordered data.
leaderboard = [("Alice", 9800), ("Bob", 8500), ("Charlie", 7200)]
top_player = leaderboard[0]  # O(1)
print(f"\n[Leaderboard] Top player: {top_player[0]} with {top_player[1]} pts")

# --- Example 2: Collecting sensor readings (append) ---
# Use case: A temperature sensor appends readings over time.
# append() is O(1) amortized — perfect for streaming/accumulating data.
sensor_readings = []
for temp in [22.1, 23.4, 21.9, 24.0, 22.8]:
    sensor_readings.append(temp)  # O(1) amortized
average = sum(sensor_readings) / len(sensor_readings)
print(f"[Sensor] Average temperature: {average:.2f}°C")

# --- Example 3: Sliding window on a log (slice) ---
# Use case: Keep only the last N log entries in memory.
# Lists support slicing to maintain a rolling window efficiently.
logs = ["login", "view_page", "click_button", "logout", "login", "error"]
window_size = 3
last_logs = logs[-window_size:]  # O(k) where k = window size
print(f"[Logs] Last {window_size} events: {last_logs}")


# =============================================================================
# 2. HASH TABLE — dict / set
#    - Hash function maps key → index in underlying array
#    - Access: O(1) avg | Insert: O(1) avg | Delete: O(1) avg
# =============================================================================

print("\n" + "=" * 60)
print("2. HASH TABLE (dict / set)")
print("=" * 60)

# --- Example 1: Word frequency counter ---
# Use case: Count occurrences of words in a document (search engine indexing).
# dict gives O(1) insert and lookup regardless of vocabulary size.
text = "the cat sat on the mat the cat"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1  # O(1) per operation
print(f"\n[Word Frequency] {word_count}")

# --- Example 2: Deduplication with a set ---
# Use case: Remove duplicate user IDs from an event stream.
# set membership check is O(1) vs O(n) for a list — massive speedup at scale.
event_user_ids = [101, 202, 101, 303, 202, 404, 101]
unique_users = set(event_user_ids)  # O(n) total, O(1) per lookup
print(f"[Deduplication] Unique users: {unique_users}")

# --- Example 3: Caching / Memoization ---
# Use case: Avoid recomputing expensive Fibonacci values (e.g., API response cache).
# dict as a cache gives O(1) hit lookup instead of recomputing O(2^n).
def fib(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:              # O(1) lookup
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(f"[Memoization] fib(35) = {fib(35)} (instant after first call)")


# =============================================================================
# 3. LINKED LIST — collections.deque
#    - Nodes with pointers, non-contiguous memory
#    - Access: O(n) | Insert/Delete at ends: O(1)
# =============================================================================

print("\n" + "=" * 60)
print("3. LINKED LIST (collections.deque)")
print("=" * 60)

from collections import deque

# --- Example 1: Browser history (back/forward) ---
# Use case: Navigate back and forward in browser history.
# O(1) append and pop on both ends makes deque perfect for double-ended navigation.
history = deque()
for page in ["home", "about", "products", "contact"]:
    history.append(page)           # O(1)
current = history.pop()            # O(1) — go back
print(f"\n[Browser History] Went back from '{current}', now at '{history[-1]}'")

# --- Example 2: Task pipeline (producer-consumer) ---
# Use case: A pipeline where tasks are added at the back and processed from the front.
# popleft() is O(1) — list.pop(0) would be O(n) and kill performance at scale.
pipeline = deque(["task_1", "task_2", "task_3", "task_4"])
processed = []
while pipeline:
    task = pipeline.popleft()      # O(1) — NOT list.pop(0) which is O(n)
    processed.append(f"{task}_done")
print(f"[Pipeline] Processed: {processed}")

# --- Example 3: Sliding window maximum (fixed-size deque) ---
# Use case: Real-time monitoring — track the last N events efficiently.
# maxlen automatically discards oldest items in O(1).
recent_errors = deque(maxlen=3)    # fixed-size window
for error in ["timeout", "404", "500", "timeout", "503"]:
    recent_errors.append(error)    # auto-discards oldest — O(1)
print(f"[Error Window] Last 3 errors: {list(recent_errors)}")


# =============================================================================
# 4. STACK — list (LIFO)
#    - append() to push, pop() to pop, [-1] to peek — all O(1)
# =============================================================================

print("\n" + "=" * 60)
print("4. STACK (list — LIFO)")
print("=" * 60)

# --- Example 1: Balanced parentheses checker ---
# Use case: Validate syntax in a code editor or HTML parser.
# Each opening bracket is pushed; each closing bracket pops and checks.
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)       # O(1)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()            # O(1)
    return len(stack) == 0

print(f"\n[Parentheses] '(a + [b * c])' balanced: {is_balanced('(a + [b * c])')}")
print(f"[Parentheses] '(a + [b * c)'  balanced: {is_balanced('(a + [b * c)')}")

# --- Example 2: Undo functionality ---
# Use case: Text editor undo — each action is pushed; Ctrl+Z pops the last one.
actions = []
for action in ["type:H", "type:e", "type:l", "type:l", "type:o"]:
    actions.append(action)         # O(1) push
undone = actions.pop()             # O(1) pop
print(f"[Undo] Undid action '{undone}', remaining: {actions}")

# --- Example 3: DFS on a graph (iterative) ---
# Use case: Crawl all pages of a website starting from the homepage.
# Stack replaces recursion — avoids Python's recursion limit on deep graphs.
graph = {
    "home": ["about", "products"],
    "about": ["team"],
    "products": ["item1", "item2"],
    "team": [], "item1": [], "item2": []
}
def dfs_iterative(graph, start):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()         # O(1)
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(f"[DFS] Pages crawled: {dfs_iterative(graph, 'home')}")


# =============================================================================
# 5. QUEUE — collections.deque (FIFO)
#    - append() to enqueue (back), popleft() to dequeue (front) — both O(1)
# =============================================================================

print("\n" + "=" * 60)
print("5. QUEUE (collections.deque — FIFO)")
print("=" * 60)

# --- Example 1: Print queue ---
# Use case: Office printer handles jobs in the order they were submitted.
# FIFO guarantees fairness — first submitted, first printed.
print_queue = deque(["doc_A", "doc_B", "doc_C"])
print_queue.append("doc_D")        # New job arrives — O(1)
next_job = print_queue.popleft()   # Printer takes next job — O(1)
print(f"\n[Print Queue] Printing: '{next_job}', remaining: {list(print_queue)}")

# --- Example 2: BFS shortest path ---
# Use case: Find the shortest path between two people in a social network.
# BFS explores level by level — queue ensures nodes are visited in order of distance.
def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()     # O(1)
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

social = {"Alice": ["Bob", "Carol"], "Bob": ["Dave"], "Carol": ["Dave", "Eve"], "Dave": [], "Eve": []}
path = bfs_shortest_path(social, "Alice", "Eve")
print(f"[BFS] Shortest path Alice → Eve: {path}")

# --- Example 3: Level-order tree traversal ---
# Use case: Display an org chart level by level (CEO → VPs → Managers...).
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_nodes = []
        for _ in range(len(queue)):
            node = queue.popleft()   # O(1)
            level_nodes.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level_nodes)
    return result

print(f"[Level-Order] Tree levels: {level_order(root)}")


# =============================================================================
# 6. TREE — Binary Tree / BST
#    - Hierarchical structure, BST: left < node < right
#    - Balanced BST — Search/Insert/Delete: O(log n)
# =============================================================================

print("\n" + "=" * 60)
print("6. TREE (Binary Tree / BST)")
print("=" * 60)

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):         # O(log n) balanced
        def _insert(node, val):
            if not node:
                return BSTNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):         # O(log n) balanced
        def _search(node, val):
            if not node:
                return False
            if val == node.val:
                return True
            return _search(node.left, val) if val < node.val else _search(node.right, val)
        return _search(self.root, val)

    def inorder(self):             # O(n) — returns sorted list
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result

# --- Example 1: Sorted data storage ---
# Use case: Store user ages and retrieve them in sorted order instantly.
# BST inorder traversal always yields elements in sorted order — O(n).
bst = BST()
for age in [35, 22, 48, 15, 30, 42, 55]:
    bst.insert(age)
print(f"\n[BST] Ages in sorted order: {bst.inorder()}")

# --- Example 2: Fast search in a product catalog ---
# Use case: Check if a product ID exists in a large catalog.
# O(log n) search vs O(n) for a list — critical at scale.
catalog_bst = BST()
for pid in [1042, 3001, 500, 2200, 750, 4400]:
    catalog_bst.insert(pid)
print(f"[BST Search] Product 2200 exists: {catalog_bst.search(2200)}")
print(f"[BST Search] Product 9999 exists: {catalog_bst.search(9999)}")

# --- Example 3: Expression tree evaluation ---
# Use case: Compilers and calculators parse and evaluate expressions as trees.
# Each leaf is an operand, each internal node is an operator.
class ExprNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def evaluate(node):
    if node.left is None:
        return int(node.val)
    left_val  = evaluate(node.left)
    right_val = evaluate(node.right)
    ops = {'+': left_val + right_val, '-': left_val - right_val,
           '*': left_val * right_val, '/': left_val // right_val}
    return ops[node.val]

# Represents: (3 + 5) * (2 - 1)  →  expected: 8
root_expr        = ExprNode('*')
root_expr.left   = ExprNode('+')
root_expr.right  = ExprNode('-')
root_expr.left.left   = ExprNode('3')
root_expr.left.right  = ExprNode('5')
root_expr.right.left  = ExprNode('2')
root_expr.right.right = ExprNode('1')
print(f"[Expression Tree] (3+5)*(2-1) = {evaluate(root_expr)}")


# =============================================================================
# 7. HEAP — heapq (Min-Heap / Priority Queue)
#    - Parent always ≤ children (min-heap)
#    - Peek min: O(1) | Insert: O(log n) | Remove min: O(log n)
# =============================================================================

print("\n" + "=" * 60)
print("7. HEAP (heapq — Min-Heap)")
print("=" * 60)

import heapq

# --- Example 1: K smallest elements ---
# Use case: Find the 3 cheapest products from a large catalog.
# heapq.nsmallest is O(n log k) — far better than sorting all O(n log n).
prices = [49.99, 12.50, 89.00, 5.99, 34.75, 7.25, 120.00]
k_cheapest = heapq.nsmallest(3, prices)  # O(n log k)
print(f"\n[Heap] 3 cheapest prices: {k_cheapest}")

# --- Example 2: Task scheduler by priority ---
# Use case: OS or job scheduler always picks the highest-priority task next.
# Min-heap on (priority, task) gives O(1) access to the most urgent item.
task_queue = []
tasks = [(3, "send_email"), (1, "fix_critical_bug"), (2, "write_tests"), (1, "deploy_hotfix")]
for priority, task in tasks:
    heapq.heappush(task_queue, (priority, task))  # O(log n)

print("[Scheduler] Processing order:")
while task_queue:
    priority, task = heapq.heappop(task_queue)    # O(log n)
    print(f"  Priority {priority}: {task}")

# --- Example 3: Merge K sorted lists ---
# Use case: Merge sorted log files from multiple servers into one sorted stream.
# Use a heap to always pick the globally smallest next element — O(n log k).
sorted_logs = [
    [(1, "server1: boot"),   (4, "server1: ready")],
    [(2, "server2: boot"),   (3, "server2: error")],
    [(0, "server3: init"),   (5, "server3: shutdown")],
]
heap = []
for i, log_list in enumerate(sorted_logs):
    if log_list:
        heapq.heappush(heap, (log_list[0][0], i, 0))  # (timestamp, list_idx, elem_idx)

merged = []
while heap:
    ts, li, ei = heapq.heappop(heap)
    merged.append(sorted_logs[li][ei][1])
    if ei + 1 < len(sorted_logs[li]):
        next_ts = sorted_logs[li][ei + 1][0]
        heapq.heappush(heap, (next_ts, li, ei + 1))

print(f"[Merge Logs] {merged}")


# =============================================================================
# 8. GRAPH — Adjacency List (dict)
#    - Nodes (vertices) connected by edges
#    - Directed/Undirected, Weighted/Unweighted, Cyclic/Acyclic
# =============================================================================

print("\n" + "=" * 60)
print("8. GRAPH (Adjacency List — dict)")
print("=" * 60)

# --- Example 1: Social network — mutual friends ---
# Use case: Find all friends reachable from a user (friend-of-friend suggestions).
# BFS on a graph explores all connections level by level.
social_graph = {
    "Alice": ["Bob", "Carol"],
    "Bob":   ["Alice", "Dave", "Eve"],
    "Carol": ["Alice", "Frank"],
    "Dave":  ["Bob"],
    "Eve":   ["Bob"],
    "Frank": ["Carol"],
}
def bfs_connections(graph, start):
    visited, queue = {start}, deque([start])
    while queue:
        user = queue.popleft()
        for friend in graph[user]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    visited.remove(start)
    return visited

print(f"\n[Social Graph] All connections of Alice: {bfs_connections(social_graph, 'Alice')}")

# --- Example 2: Dependency resolution (topological sort) ---
# Use case: Package manager (pip/npm) installs packages in the correct order.
# Topological sort on a DAG gives a valid install order.
def topological_sort(graph):
    visited, stack = set(), []
    def dfs(node):
        visited.add(node)
        for dep in graph.get(node, []):
            if dep not in visited:
                dfs(dep)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

dependencies = {
    "app":      ["flask", "sqlalchemy"],
    "flask":    ["werkzeug", "jinja2"],
    "sqlalchemy": ["greenlet"],
    "werkzeug": [],
    "jinja2":   [],
    "greenlet": [],
}
print(f"[Topological Sort] Install order: {topological_sort(dependencies)}")

# --- Example 3: Shortest path with weights (Dijkstra) ---
# Use case: GPS navigation — find the shortest route between two cities.
# Dijkstra uses a min-heap + graph to find optimal paths in O((V+E) log V).
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]  # (cost, node)
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return distances

city_map = {
    "Paris":    [("Lyon", 465),   ("Bordeaux", 584)],
    "Lyon":     [("Marseille", 315), ("Paris", 465)],
    "Bordeaux": [("Paris", 584),  ("Marseille", 637)],
    "Marseille":[("Lyon", 315),   ("Bordeaux", 637)],
}
distances = dijkstra(city_map, "Paris")
print(f"[Dijkstra] Shortest distances from Paris: {distances}")

print("\n" + "=" * 60)
print("All examples completed successfully!")
print("=" * 60)
