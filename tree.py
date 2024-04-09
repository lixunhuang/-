class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def find_node(node, target):
    """
    Search for a node with the given value in the tree.
    """
    if node is None:
        return False
    elif node.value == target:
        return True
    else:
        return find_node(node.left, target) or find_node(node.right, target)

def preorder_traversal(node):
    """
    Perform preorder traversal of the tree.
    """
    if node:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inject_node(node, son, place):
    """
    Insert a node as a left or right child of another node.
    """
    if place == 'left':
        son.left = node.left
        node.left = son
    elif place == 'right':
        son.right = node.right
        node.right = son
    else:
        print('Error: the place should be "left" or "right".')


def inject_search_tree(node, son):
    if node is None:
        node = son
        return
    elif node.value > son.value:
        inject_search_tree(node.right, son)
        return
    else:
        inject_search_tree(node.left, son)
        return

# 示例树
#        1
#      /   \
#     2     3
#    / \
#   5   4
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
inject_search_tree(node3, node2)
inject_search_tree(node3, node1)
inject_search_tree(node3, node4)
inject_search_tree(node3, node5)
# node1.left = node2
# node1.right = node3
# node2.left = node5
# node2.right = node4

# 在节点2的左侧插入新节点6
# inject_node(node2, TreeNode(6), 'left')

# 执行前序遍历
preorder_traversal(node3)
