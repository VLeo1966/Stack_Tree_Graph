# dz.py

# Модуль Stack (Стек)
print("Модуль: Stack (Стек)")

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

    # Метод для удаления и возврата последнего элемента стека
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # Метод для просмотра последнего элемента стека без его удаления
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Метод для получения размера стека
    def size(self):
        return len(self.items)

# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack после push:", stack.items)
print("Peek Stack:", stack.peek())
stack.pop()
print("Stack после pop:", stack.items)

# Модуль Queue (Очередь)
print("\nМодуль: Queue (Очередь)")

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

    # Метод для удаления и возврата элемента из конца списка (очередь)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    # Метод для получения размера очереди
    def size(self):
        return len(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print("Queue после enqueue:", queue.items)
queue.dequeue()
print("Queue после dequeue:", queue.items)

# Модуль Binary Tree (Бинарное дерево)
print("\nМодуль: Binary Tree (Бинарное дерево)")

# Класс Node (Узел бинарного дерева)
class Node:
    # Инициализация узла с значением
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функция для добавления узла в дерево
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Функция для печати дерева с отступами
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print_tree(root.right, level + 1, "R--- ")
        print(" " * (level * 4) + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--- ")

# Пример использования бинарного дерева
root = Node(50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print("Бинарное дерево:")
print_tree(root)

# Модуль Graph (Граф)
print("\nМодуль: Graph (Граф)")

# Класс Graph (Граф)
class Graph:
    # Инициализация графа как пустого словаря
    def __init__(self):
        self.graph = {}

    # Метод для добавления ребра между двумя вершинами
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Метод для печати графа
    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

# Пример использования графа
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

print("Граф:")
g.print_graph()
