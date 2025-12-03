from .BSTNode import BSTNode

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self.root = self.root.insert(key)

    def delete(self, key):
        if self.root:
            self.root = self.root.delete(key)

    def height(self):
        return self.root.height() if self.root else -1

    def print(self):
        if self.root:
            self.root.print_tree()
        else:
            print("Empty BST")
            
    #ОБХОДЫ ДЕРЕВА

    def preorder(self):
        result = []
        def dfs(node):
            if node:
                result.append(node.key)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return result

    def inorder(self):
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                result.append(node.key)
                dfs(node.right)
        dfs(self.root)
        return result

    def postorder(self):
        result = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                result.append(node.key)
        dfs(self.root)
        return result

    def bfs(self):
        result = []
        queue = []
        if self.root:
            queue.append(self.root)
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        result = []
        stack = []
        if self.root:
            stack.append(self.root)
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # ПОИСК / MIN / MAX

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def find_min(self):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    def find_max(self):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node
