# Класс Stack (Стек)
class Stack:
    # Инициализация пустого списка для хранения элементов стека
    def __init__(self):
        self.items = []

    # Метод для проверки, пуст ли стек
    def is_empty(self):
        return self.items == []

    # Метод для добавления элемента в стек
    def push(self, item):
        self.items.append(item)

    # Метод для просмотра последнего элемента стека без его удаления
    def peek(self):
        return self.items[-1]

# Создаем экземпляр стека
stack = Stack()

# Проверяем, пуст ли стек (ожидаем True)
print(stack.is_empty())

# Добавляем элементы в стек
stack.push(1)
stack.push(2)
stack.push(3)

# Проверяем снова, пуст ли стек (ожидаем False)
print(stack.is_empty())

# Просматриваем последний элемент стека (ожидаем 3)
print(stack.peek())

# Класс Queue (Очередь)
class Queue:
    # Инициализация пустого списка для хранения элементов очереди
    def __init__(self):
        self.items = []

    # Метод для проверки, пуста ли очередь
    def is_empty(self):
        return self.items == []

    # Метод для добавления элемента в начало списка (очередь)
    def enqueue(self, item):
        self.items.insert(0, item)

    # Метод для удаления и возвращения элемента из конца списка (очередь)
    def dequeue(self):
        return self.items.pop()

    # Метод для получения размера очереди
    def size(self):
        return len(self.items)

# Создаем экземпляр очереди
queue = Queue()

# Проверяем, пуста ли очередь (ожидаем True)
print(queue.is_empty())

# Добавляем элементы в очередь
queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# Проверяем снова, пуста ли очередь (ожидаем False)
print(queue.is_empty())

# Выводим размер очереди (ожидаем 4)
print(queue.size())

# Удаляем и возвращаем первый добавленный элемент (ожидаем "действие 1")
print(queue.dequeue())

# Выводим новый размер очереди после удаления элемента (ожидаем 3)
print(queue.size())

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


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()




