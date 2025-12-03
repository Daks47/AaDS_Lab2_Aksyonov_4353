from .BSTNode import BSTNode


class RBNode(BSTNode):
    RED = 0
    BLACK = 1

    def __init__(self, key, parent=None, color=RED):
        super().__init__(key, parent)
        self.color = color  # новый узел по умолчанию красный

    #ПОВОРОТЫ

    def _rotate_left(self):
        pivot = self.right
        if pivot is None:
            return self

        self.right = pivot.left
        if pivot.left:
            pivot.left.parent = self

        pivot.parent = self.parent
        if self.parent:
            if self == self.parent.left:
                self.parent.left = pivot
            else:
                self.parent.right = pivot

        pivot.left = self
        self.parent = pivot

        return pivot

    def _rotate_right(self):
        pivot = self.left
        if pivot is None:
            return self

        self.left = pivot.right
        if pivot.right:
            pivot.right.parent = self

        pivot.parent = self.parent
        if self.parent:
            if self == self.parent.left:
                self.parent.left = pivot
            else:
                self.parent.right = pivot

        pivot.right = self
        self.parent = pivot

        return pivot

    #ВСТАВКА

    def insert(self, key):
        """Стандартная BST-вставка + фиксация свойств КЧ-дерева."""

        if key < self.key:
            if self.left is None:
                self.left = RBNode(key, parent=self, color=RBNode.RED)
                return self.left._fix_insert()
            else:
                new_root = self.left.insert(key)
                return new_root.get_root()

        elif key > self.key:
            if self.right is None:
                self.right = RBNode(key, parent=self, color=RBNode.RED)
                return self.right._fix_insert()
            else:
                new_root = self.right.insert(key)
                return new_root.get_root()

        return self.get_root()

    def _fix_insert(self):
        node = self

        while node.parent and node.parent.color == RBNode.RED:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                break

            if parent == grandparent.left:
                uncle = grandparent.right

                # Case 2: красный дядя
                if uncle and uncle.color == RBNode.RED:
                    parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    grandparent.color = RBNode.RED
                    node = grandparent
                else:
                    # Case 3: треугольник
                    if node == parent.right:
                        node = parent
                        node._rotate_left()
                        parent = node.parent
                        grandparent = parent.parent

                    # Case 4: линия
                    parent.color = RBNode.BLACK
                    grandparent.color = RBNode.RED
                    grandparent._rotate_right()

            else:
                # зеркальные случаи
                uncle = grandparent.left

                if uncle and uncle.color == RBNode.RED:
                    parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    grandparent.color = RBNode.RED
                    node = grandparent
                else:
                    if node == parent.left:
                        node = parent
                        node._rotate_right()
                        parent = node.parent
                        grandparent = parent.parent

                    parent.color = RBNode.BLACK
                    grandparent.color = RBNode.RED
                    grandparent._rotate_left()

        root = node.get_root()
        root.color = RBNode.BLACK
        return root

    #УДАЛЕНИЕ

    def _replace_node(self, child):
        """Заменяет текущий узел его ребёнком."""
        if self.parent:
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child
        if child:
            child.parent = self.parent

    def _minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        """Удаление ключа из КЧ-дерева."""
        if key < self.key:
            if self.left:
                return self.left.delete(key).get_root()
            return self.get_root()

        if key > self.key:
            if self.right:
                return self.right.delete(key).get_root()
            return self.get_root()

        # нашли узел
        if self.left and self.right:
            succ = self.right._minimum()
            self.key = succ.key
            return self.right.delete(succ.key).get_root()

        child = self.left if self.left else self.right
        deleted_color = self.color

        # узел имеет ребёнка
        if child:
            self._replace_node(child)
            root = child.get_root()
            if deleted_color == RBNode.BLACK:
                child._fix_delete()
            return root

        # удаляем лист
        parent = self.parent
        self._replace_node(None)

        if deleted_color == RBNode.BLACK and parent:
            self._fix_delete_leaf(parent)

        return parent.get_root() if parent else None

    # фиксация удаления (лист)

    def _fix_delete_leaf(self, parent):
        """Исправление двойной чёрноты, возникшей после удаления листа."""
        node = None

        while parent:
            sibling = parent.right if node is parent.left else parent.left

            # Case 1: красный брат
            if sibling and sibling.color == RBNode.RED:
                sibling.color = RBNode.BLACK
                parent.color = RBNode.RED
                if sibling == parent.right:
                    parent._rotate_left()
                else:
                    parent._rotate_right()
                sibling = parent.right if node is parent.left else parent.left

            # Case 2: оба ребёнка брата чёрные
            if sibling and \
               (not sibling.left or sibling.left.color == RBNode.BLACK) and \
               (not sibling.right or sibling.right.color == RBNode.BLACK):

                sibling.color = RBNode.RED
                if parent.color == RBNode.RED:
                    parent.color = RBNode.BLACK
                    return
                else:
                    node = parent
                    parent = parent.parent
                    continue

            # Case 3 / 4
            if sibling:
                if sibling == parent.right:
                    if not sibling.right or sibling.right.color == RBNode.BLACK:
                        sibling.left.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        sibling._rotate_right()
                        sibling = parent.right
                    sibling.color = parent.color
                    parent.color = RBNode.BLACK
                    sibling.right.color = RBNode.BLACK
                    parent._rotate_left()
                else:
                    if not sibling.left or sibling.left.color == RBNode.BLACK:
                        sibling.right.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        sibling._rotate_left()
                        sibling = parent.left
                    sibling.color = parent.color
                    parent.color = RBNode.BLACK
                    sibling.left.color = RBNode.BLACK
                    parent._rotate_right()
                return

        return

    # фиксация удаления (у узла был ребёнок)

    def _fix_delete(self):
        """Исправление свойств КЧ-дерева, если удалён узел с одним ребёнком."""
        if self.color == RBNode.RED:
            self.color = RBNode.BLACK
            return

        node = self

        while node.parent:
            parent = node.parent
            sibling = parent.right if node == parent.left else parent.left

            # Case 1: красный брат
            if sibling and sibling.color == RBNode.RED:
                sibling.color = RBNode.BLACK
                parent.color = RBNode.RED
                if sibling == parent.right:
                    parent._rotate_left()
                else:
                    parent._rotate_right()
                sibling = parent.right if node == parent.left else parent.left

            # Case 2: оба ребёнка брата чёрные
            if sibling and \
               (not sibling.left or sibling.left.color == RBNode.BLACK) and \
               (not sibling.right or sibling.right.color == RBNode.BLACK):

                sibling.color = RBNode.RED
                if parent.color == RBNode.RED:
                    parent.color = RBNode.BLACK
                    return
                node = parent
                continue

            # Case 3: у брата есть красный ребёнок
            if sibling:
                if sibling == parent.right:
                    if not sibling.right or sibling.right.color == RBNode.BLACK:
                        sibling.left.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        sibling._rotate_right()
                        sibling = parent.right

                    sibling.color = parent.color
                    parent.color = RBNode.BLACK
                    sibling.right.color = RBNode.BLACK
                    parent._rotate_left()
                else:
                    if not sibling.left or sibling.left.color == RBNode.BLACK:
                        sibling.right.color = RBNode.BLACK
                        sibling.color = RBNode.RED
                        sibling._rotate_left()
                        sibling = parent.left

                    sibling.color = parent.color
                    parent.color = RBNode.BLACK
                    sibling.left.color = RBNode.BLACK
                    parent._rotate_right()
                return

        return

    #ПЕЧАТЬ

    def _black_height(self, node):
        if node is None:
            return 1
        left = self._black_height(node.left)
        right = self._black_height(node.right)
        return left + (1 if node.color == RBNode.BLACK else 0)

    def black_height(self):
        return self._black_height(self)

    def print_tree(self, level=0, prefix="Root: "):
        indent = " " * (4 * level)
        color = "R" if self.color == RBNode.RED else "B"
        print(f"{indent}{prefix}{self.key} ({color})")
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ")
