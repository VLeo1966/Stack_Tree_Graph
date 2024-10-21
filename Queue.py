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
