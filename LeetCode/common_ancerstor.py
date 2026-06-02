class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.right.left        # node with value 7
q = root.left.right.right       # node with value 9


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root


answer = lowest_common_ancestor(root, p, q)
print(answer.val)