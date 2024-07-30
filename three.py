class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_sum(node):
    if node is None:
        return 0
    # Рекурсивно обходимо ліве і праве піддерева та додаємо значення вузлів
    return node.val + find_sum(node.left) + find_sum(node.right)

# Приклад використання:
# Будуємо дерево:
#        5
#       / \
#      3   8
#     / \   \
#    2   4   6

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(6)

# Знаходимо суму всіх значень
print(find_sum(root))
