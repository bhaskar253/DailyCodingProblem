# Problem Stmt.:
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_unival(root):
    if root is None:
        return 0
    is_unival = True
    if root.left and root.right:
        is_unival = root.val == root.left.val and root.val == root.right.val
    if root.left:
        is_unival = root.val == root.left.val
    if root.right:
        is_unival = root.val == root.right.val
    if not is_unival:
        return count_unival(root.left) + count_unival(root.right)
    return count_unival(root.left) + count_unival(root.right) + 1

if __name__ == "__main__":
    root = Node(0,Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))
    print(count_unival(root))
