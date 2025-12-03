class BSTNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    def height(self):
        lh = self.left.height() if self.left else -1
        rh = self.right.height() if self.right else -1
        return 1 + max(lh, rh)

    def search(self, key):
        if key == self.key:
            return self
        if key < self.key and self.left:
            return self.left.search(key)
        if key > self.key and self.right:
            return self.right.search(key)
        return None

    def insert(self, key):
        if key < self.key:
            if not self.left:
                self.left = BSTNode(key, parent=self)
            else:
                self.left = self.left.insert(key)
        elif key > self.key:
            if not self.right:
                self.right = BSTNode(key, parent=self)
            else:
                self.right = self.right.insert(key)
        return self

    def _min_node(self):
        node = self
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self
        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self

        # key == self.key
        if not self.left and not self.right:
            return None
        if not self.left:
            self.right.parent = self.parent
            return self.right
        if not self.right:
            self.left.parent = self.parent
            return self.left

        successor = self.right._min_node()
        self.key = successor.key
        self.right = self.right.delete(successor.key)
        return self

    def get_root(self):
        n = self
        while n.parent:
            n = n.parent
        return n

    def print_tree(self, lvl=0, prefix="Root: "):
        indent = " " * (lvl * 4)
        print(f"{indent}{prefix}{self.key} (h={self.height()})")
        if self.left:
            self.left.print_tree(lvl + 1, "L--- ")
        if self.right:
            self.right.print_tree(lvl + 1, "R--- ")
