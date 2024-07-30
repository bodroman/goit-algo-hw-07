class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max(node):
    current = node
    
    # Переходимо до крайнього правого листка
    while(current.right is not None):
        current = current.right
    
    return current.val

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

# Знаходимо найбільше значення
print(find_max(root))

