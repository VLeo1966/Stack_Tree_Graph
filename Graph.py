# Класс Graph (Граф)
class Graph:
    # Инициализация графа как словаря
    def __init__(self):
        self.graph = {}

    # Метод для добавления ребра между двумя вершинами
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Метод для печати графа
    def print_graph(self):
        # Пример: {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

# Создаем экземпляр графа
g = Graph()

# Добавляем ребра в граф
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Печатаем граф
g.print_graph()
