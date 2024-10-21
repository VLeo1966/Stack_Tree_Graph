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
