import random
import math
import matplotlib.pyplot as plt

from src.BST import BST
from src.AVL import AVL
from src.RBT import RBT


#BST — случайные ключи

def measure_height_bst(n):
    bst = BST()
    values = random.sample(range(10_000_000), n)

    for v in values:
        bst.insert(v)

    return bst.height()


def bst_random_heights():
    ns = list(range(100, 10_001, 200))
    heights = []

    for n in ns:
        heights.append(measure_height_bst(n))

    theory = [2.2 * math.log2(n) for n in ns]

    plt.figure(figsize=(12, 7))
    plt.plot(ns, heights, label="Экспериментальная высота", color="blue")
    plt.plot(ns, theory, label="2.2 log₂(n)", linestyle="--", color="green")
    plt.title("Зависимость высоты BST от количества ключей")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота дерева")
    plt.grid()
    plt.legend()
    plt.show()



#AVL — измерение высоты

def measure_height_avl(n, sorted_keys=False):
    avl = AVL()

    values = list(range(n)) if sorted_keys else random.sample(range(10_000_000), n)

    for v in values:
        avl.insert(v)

    return avl.height()



#RBT — измерение высоты

def measure_height_rbt(n, sorted_keys=False):
    rbt = RBT()

    values = list(range(n)) if sorted_keys else random.sample(range(10_000_000), n)

    for v in values:
        rbt.insert(v)

    return rbt.height()



#AVL + RBT высоты при случайных ключах

def avl_rbt_random_heights():
    ns = list(range(100, 10_001, 300))

    avl_h = []
    rbt_h = []

    for n in ns:
        avl_h.append(measure_height_avl(n))
        rbt_h.append(measure_height_rbt(n))

    avl_low = [math.log2(n) for n in ns]
    avl_high = [1.45 * math.log2(n) for n in ns]

    rbt_low = [math.log2(n) for n in ns]
    rbt_high = [2 * math.log2(n) for n in ns]

    # --- AVL ---
    plt.figure(figsize=(12, 6))
    plt.plot(ns, avl_h, label="Эксп. высота AVL", color="blue")
    plt.plot(ns, avl_low, label="Теор. нижняя оценка", linestyle="--", color="green")
    plt.plot(ns, avl_high, label="Теор. верхняя оценка", linestyle="--", color="red")
    plt.title("Зависимость высоты AVL от количества ключей")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота")
    plt.legend()
    plt.grid()
    plt.show()

    # --- RBT ---
    plt.figure(figsize=(12, 6))
    plt.plot(ns, rbt_h, label="Эксп. высота RBT", color="blue")
    plt.plot(ns, rbt_low, label="Теор. нижняя оценка", linestyle="--", color="green")
    plt.plot(ns, rbt_high, label="Теор. верхняя оценка", linestyle="--", color="red")
    plt.title("Зависимость высоты красно-чёрного дерева от количества ключей")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота")
    plt.legend()
    plt.grid()
    plt.show()



#AVL + RBT высоты при монотонно возрастающих ключах

def avl_rbt_sorted_heights():
    ns = list(range(100, 10_001, 300))

    avl_h = []
    rbt_h = []

    for n in ns:
        avl_h.append(measure_height_avl(n, sorted_keys=True))
        rbt_h.append(measure_height_rbt(n, sorted_keys=True))

    avl_low = [math.log2(n) for n in ns]
    avl_high = [1.45 * math.log2(n) for n in ns]

    rbt_low = [math.log2(n) for n in ns]
    rbt_high = [2 * math.log2(n) for n in ns]

    # --- AVL sorted ---
    plt.figure(figsize=(12, 6))
    plt.plot(ns, avl_h, label="Эксп. высота AVL (монот.)", color="blue")
    plt.plot(ns, avl_low, label="Теор. нижняя оценка", linestyle="--", color="green")
    plt.plot(ns, avl_high, label="Теор. верхняя оценка", linestyle="--", color="red")
    plt.title("AVL при монотонном вводе")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота")
    plt.legend()
    plt.grid()
    plt.show()

    # --- RBT sorted ---
    plt.figure(figsize=(12, 6))
    plt.plot(ns, rbt_h, label="Эксп. RBT (монот.)", color="blue")
    plt.plot(ns, rbt_low, label="Теор. нижняя оценка", linestyle="--", color="green")
    plt.plot(ns, rbt_high, label="Теор. верхняя оценка", linestyle="--", color="red")
    plt.title("RBT при монотонном вводе")
    plt.xlabel("Количество ключей")
    plt.ylabel("Высота")
    plt.legend()
    plt.grid()
    plt.show()
