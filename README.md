# Stack_Tree_Graph

Вот пример файла `README.md` для твоего репозитория на GitHub:

```markdown
# Data Structures Module - `dz.py`

This repository contains an implementation of common data structures using Python, including Stack, Queue, Binary Tree, and Graph. The module `dz.py` provides examples of how these data structures are defined and used, complete with inline comments and print statements to demonstrate their functionality.

## Table of Contents
- [Overview](#overview)
- [Modules](#modules)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Binary Tree](#binary-tree)
  - [Graph](#graph)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Overview

This project implements the following data structures:
- **Stack**: A LIFO (Last In First Out) structure, where the last element added is the first to be removed.
- **Queue**: A FIFO (First In First Out) structure, where the first element added is the first to be removed.
- **Binary Tree**: A hierarchical structure where each node has up to two children.
- **Graph**: A structure consisting of nodes (vertices) and edges connecting them.

Each data structure is implemented in a modular fashion, and the program prints out relevant messages to show how they operate.

## Modules

### Stack
The `Stack` class simulates the stack data structure, supporting:
- `push(item)` – add an item to the top of the stack.
- `pop()` – remove and return the top item from the stack.
- `peek()` – view the top item without removing it.
- `is_empty()` – check if the stack is empty.
- `size()` – return the size of the stack.

Example:
```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Peek:", stack.peek())  # Output: 3
stack.pop()
print("Stack after pop:", stack.items)  # Output: [1, 2]
```

### Queue
The `Queue` class simulates the queue data structure, supporting:
- `enqueue(item)` – add an item to the back of the queue.
- `dequeue()` – remove and return the item from the front of the queue.
- `is_empty()` – check if the queue is empty.
- `size()` – return the size of the queue.

Example:
```python
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print("Queue:", queue.items)  # Output: ['C', 'B', 'A']
queue.dequeue()
print("Queue after dequeue:", queue.items)  # Output: ['C', 'B']
```

### Binary Tree
The binary tree is implemented using a `Node` class, which has:
- `val` – the value of the node.
- `left` – the left child node.
- `right` – the right child node.

The `insert()` function allows adding nodes in a sorted manner, and the `print_tree()` function prints the tree structure.

Example:
```python
root = Node(50)
root = insert(root, 30)
root = insert(root, 70)
print_tree(root)
```

### Graph
The `Graph` class supports adding edges between vertices and printing the graph structure.

Example:
```python
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.print_graph()
```

## Usage

To run the `dz.py` module, simply execute the Python script in your terminal:

```bash
python dz.py
```

The program will print each module's execution and results.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository-name
   ```
3. Run the Python script:
   ```bash
   python dz.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Как использовать:
- Обязательно поменяй `https://github.com/yourusername/your-repository-name.git` на настоящий адрес твоего репозитория.
- Подсекции объясняют структуру кода, а примеры демонстрируют его использование.
