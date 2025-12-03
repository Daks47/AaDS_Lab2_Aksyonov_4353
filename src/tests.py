from src.BST import BST
from src.AVL import AVL
from src.RBT import RBT


#ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

def bst_height(node):
    return node.height() if node else -1


def avl_height(node):
    return node.height_attr if node else -1


def avl_balance(node):
    if node is None:
        return 0
    lh = node.left.height_attr if node.left else -1
    rh = node.right.height_attr if node.right else -1
    return lh - rh


def rbt_color(node):
    return "R" if node.color == 0 else "B"


def rbt_bh(node):
    return node.black_height() if node else 0


#BST PRINT

def print_bst_tree(node, prefix="", is_left=True):
    if node is None:
        return
    connector = "L--- " if is_left else "R--- "
    print(prefix + connector + f"{node.key} h:{bst_height(node)}")
    print_bst_tree(node.left, prefix + "     ", True)
    print_bst_tree(node.right, prefix + "     ", False)


#AVL PRINT

def print_avl_tree(node, prefix="", is_left=True):
    if node is None:
        return
    h = avl_height(node)
    b = avl_balance(node)
    connector = "L--- " if is_left else "R--- "
    print(prefix + connector + f"{node.key} (h:{h}, b:{b})")
    print_avl_tree(node.left, prefix + "     ", True)
    print_avl_tree(node.right, prefix + "     ", False)


#RED–BLACK PRINT

def print_rbt_tree(node, prefix="", is_left=True):
    if node is None:
        return
    color = rbt_color(node)
    bh = rbt_bh(node)
    connector = "L--- " if is_left else "R--- "
    print(prefix + connector + f"{node.key}({color}, bh={bh})")
    print_rbt_tree(node.left, prefix + "     ", True)
    print_rbt_tree(node.right, prefix + "     ", False)


#BST TEST

def test_bst():
    print("\n===================== BST ДЕРЕВО =====================")

    tree = BST()
    values = [45, 20, 70, 10, 30, 60, 90]   # <<< новые значения

    for v in values:
        tree.insert(v)

    print("\nДерево:")
    print(f"Root: {tree.root.key} h:{bst_height(tree.root)}")
    print_bst_tree(tree.root.left, "", True)
    print_bst_tree(tree.root.right, "", False)

    print("\nПрямой обход:", tree.preorder())
    print("Центрированный обход:", tree.inorder())
    print("Обратный обход:", tree.postorder())
    print("Обход в ширину:", tree.bfs())
    print("Обход в глубину:", tree.dfs())

    print("\nМинимум:", tree.find_min().key, ", Максимум:", tree.find_max().key)

    print("\nПоиск 30:", "Найден" if tree.search(30) else "Не найден")

    print("\nПосле удаления 20:")
    tree.delete(20)
    print(f"Root: {tree.root.key} h:{bst_height(tree.root)}")
    print_bst_tree(tree.root.left, "", True)
    print_bst_tree(tree.root.right, "", False)



#AVL TEST

def test_avl():
    print("\n===================== AVL ДЕРЕВО =====================")

    tree = AVL()
    values = [25, 15, 40, 10, 18, 30, 50, 5, 12, 20, 35, 45, 55]  # <<< новые значения

    for v in values:
        tree.insert(v)

    print("\nAVL дерево после вставки:")
    print("Высота дерева:", avl_height(tree.root))
    print(f"Root: {tree.root.key} (h:{avl_height(tree.root)}, b:{avl_balance(tree.root)})")

    print_avl_tree(tree.root.left, "", True)
    print_avl_tree(tree.root.right, "", False)

    print("\nОбход в ширину:", tree.bfs())
    print("Прямой обход:", tree.preorder())
    print("Центрированный обход:", tree.inorder())

    print("\nAVL дерево после удаления 15 и 40:")
    tree.delete(15)
    tree.delete(40)

    print("Высота дерева:", avl_height(tree.root))
    print(f"Root: {tree.root.key} (h:{avl_height(tree.root)}, b:{avl_balance(tree.root)})")

    print_avl_tree(tree.root.left, "", True)
    print_avl_tree(tree.root.right, "", False)

    print("\nМинимальное значение:", tree.find_min().key)
    print("Максимальное значение:", tree.find_max().key)



#RED–BLACK TEST

def test_rbt():
    print("\n================ КРАСНО-ЧЁРНОЕ ДЕРЕВО ================")

    tree = RBT()
    values = [20, 8, 30, 5, 12, 25, 40, 10, 15, 22, 28]  # <<< новые значения

    for v in values:
        tree.insert(v)

    print("\nКрасно-черное дерево после вставки:")
    print(f"Root: {tree.root.key}({rbt_color(tree.root)}, bh={rbt_bh(tree.root)})")
    print_rbt_tree(tree.root.left, "", True)
    print_rbt_tree(tree.root.right, "", False)

    print("\nОбщая черная высота дерева:", rbt_bh(tree.root))

    print("\nПрямой обход:", tree.preorder())
    print("Центрированный обход:", tree.inorder())
    print("Обратный обход:", tree.postorder())
    print("Обход в ширину:", tree.bfs())

    value_to_find = 15
    found = tree.search(value_to_find)
    print(f"\nУзел {value_to_find} найден, цвет:",
          "Красный" if found.color == 0 else "Черный")

    print("\n--- После удаления значения 12 ---")
    tree.delete(12)

    print(f"Root: {tree.root.key}({rbt_color(tree.root)}, bh={rbt_bh(tree.root)})")
    print_rbt_tree(tree.root.left, "", True)
    print_rbt_tree(tree.root.right, "", False)

    print("Черная высота после удаления:", rbt_bh(tree.root))
