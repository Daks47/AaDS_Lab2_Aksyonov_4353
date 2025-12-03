from .BSTNode import BSTNode

class AVLNode(BSTNode):
    def __init__(self, key, parent=None):
        super().__init__(key, parent)
        self.height_attr = 0

    def _update_height(self):
        lh = self.left.height_attr if isinstance(self.left, AVLNode) else -1
        rh = self.right.height_attr if isinstance(self.right, AVLNode) else -1
        self.height_attr = 1 + max(lh, rh)

    def _balance(self):
        lh = self.left.height_attr if isinstance(self.left, AVLNode) else -1
        rh = self.right.height_attr if isinstance(self.right, AVLNode) else -1
        return lh - rh

    def _rotate_left(self):
        pivot = self.right
        self.right = pivot.left
        if pivot.left:
            pivot.left.parent = self
        pivot.left = self
        pivot.parent = self.parent
        self.parent = pivot
        self._update_height()
        pivot._update_height()
        return pivot

    def _rotate_right(self):
        pivot = self.left
        self.left = pivot.right
        if pivot.right:
            pivot.right.parent = self
        pivot.right = self
        pivot.parent = self.parent
        self.parent = pivot
        self._update_height()
        pivot._update_height()
        return pivot

    def _rebalance(self):
        self._update_height()
        b = self._balance()

        if b > 1:  # left heavy
            if isinstance(self.left, AVLNode) and self.left._balance() < 0:
                self.left = self.left._rotate_left()
            return self._rotate_right()

        if b < -1:  # right heavy
            if isinstance(self.right, AVLNode) and self.right._balance() > 0:
                self.right = self.right._rotate_right()
            return self._rotate_left()

        return self

    def insert(self, key):
        if key < self.key:
            if not self.left:
                self.left = AVLNode(key, self)
            else:
                self.left = self.left.insert(key)
        elif key > self.key:
            if not self.right:
                self.right = AVLNode(key, self)
            else:
                self.right = self.right.insert(key)
        return self._rebalance()

    def delete(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            successor = self.right
            while successor.left:
                successor = successor.left
            self.key = successor.key
            self.right = self.right.delete(successor.key)

        return self._rebalance()

    def height(self):
        return self.height_attr

