from .RBNode import RBNode

class RBT:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = RBNode(key, color=RBNode.BLACK)
        else:
            self.root = self.root.insert(key)

    def delete(self, key):
        if self.root:
            self.root = self.root.delete(key)
            if self.root:
                self.root.color = RBNode.BLACK

    def height(self):
        return self.root.height() if self.root else -1

    def print(self):
        if self.root:
            self.root.print_tree()
        else:
            print("Empty red-black tree")
    #ОБХОДЫ ДЛЯ RBT

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
        q = []
        if self.root:
            q.append(self.root)
        while q:
            node = q.pop(0)
            result.append(node.key)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return result

    def dfs(self):
        result = []
        st = []
        if self.root:
            st.append(self.root)
        while st:
            node = st.pop()
            result.append(node.key)
            if node.right: st.append(node.right)
            if node.left: st.append(node.left)
        return result

    #ПОИСК / МИНИМУМ / МАКСИМУМ

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
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
