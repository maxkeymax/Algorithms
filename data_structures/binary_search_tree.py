class Node:
    """Узел бинарного дерева."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Бинарное дерево поиска."""
    def __init__(self):
        self.root = None

    def add(self, value):
        """Добавить элемент в дерево."""
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        """Рекурсивный метод добавления элемента."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def search(self, value):
        """Поиск элемента в дереве."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Рекурсивный метод поиска элемента."""
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def print_in_order(self):
        """Вывод всех элементов в порядке возрастания."""
        self._print_in_order_recursive(self.root)

    def _print_in_order_recursive(self, node):
        """Рекурсивный метод вывода элементов."""
        if node:
            self._print_in_order_recursive(node.left)
            print(node.value, end=" ")
            self._print_in_order_recursive(node.right)


# Пример использования
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(10)
    bst.add(1)
    bst.add(6)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    print("Элементы в порядке возрастания:")
    bst.print_in_order()

    print("\nПоиск элемента 10:")
    result = bst.search(10)
    if result:
        print("Элемент найден:", result.value)
    else:
        print("Элемент не найден")