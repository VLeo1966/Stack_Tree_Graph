# Класс Node (Узел)
class Node():
    # Инициализатор для создания узла
    def __init__(self, key):
        self.left = None  # Левый дочерний узел
        self.right = None  # Правый дочерний узел
        self.val = key  # Значение узла

# Функция для добавления нового узла в дерево
def insert(root, key):
    # Если корень пуст, создаем новый узел
    if root is None:
        return Node(key)
    else:
        # Если значение корня меньше ключа, вставляем в правое поддерево
        if root.val < key:
            root.right = insert(root.right, key)
        # Если значение корня больше или равно ключу, вставляем в левое поддерево
        else:
            root.left = insert(root.left, key)
    return root  # Возвращаем корень дерева

# Создаем корневой узел дерева с ключом 70
root = Node(70)

# Вставляем узлы с различными значениями
root = insert(root, 30)  # Вставляем узел со значением 30
root = insert(root, 56)  # Вставляем узел со значением 56
root = insert(root, 89)  # Вставляем узел со значением 89
root = insert(root, 45)  # Вставляем узел со значением 45
root = insert(root, 60)  # Вставляем узел со значением 60
root = insert(root, 73)  # Вставляем узел со значением 73
root = insert(root, 98)  # Вставляем узел со значением 98
root = insert(root, 84)  # Вставляем узел со значением 84

# Функция для печати дерева с отступами
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        # Печатаем правое поддерево с увеличенным отступом
        print_tree(root.right, level + 1, "R--- ")
        # Печатаем корневой узел с текущим отступом
        print(" " * (level * 4) + prefix + str(root.val))
        # Печатаем левое поддерево с увеличенным отступом
        print_tree(root.left, level + 1, "L--- ")

# Вызываем функцию для печати дерева
print_tree(root)
