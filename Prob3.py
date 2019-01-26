# Problem Stmt.:
#Given the root to a binary tree, implement serialize(root),
#which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    string = ''
    stack = [node]
    while len(stack):
        curr = stack.pop()
        if curr:
            string += curr.val + ','
            stack.append(curr.right)
            stack.append(curr.left)
        else:
            string += 'None,'
    return string

def deserialize(string):
    lst = string.split(',')
    lst.pop()
    lst.pop()
    lst = lst[::-1]
    root = curr = None
    stack = []
    left = True
    while len(lst)>0:
        val = lst.pop()
        if val != 'None':
            node = Node(val)
            if curr is not None:
                if left:
                    curr.left = node
                else:
                    curr.right = node
                    left = True
            elif root is None:
                root = node
            curr = node
            stack.append(node)
        else:
            curr = stack.pop()
            left = False
    return root

if __name__ == "__main__":
    node = Node('root',Node('left', Node('left.left')),Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
