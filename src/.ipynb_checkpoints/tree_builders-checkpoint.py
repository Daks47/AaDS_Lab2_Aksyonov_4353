from .BST import BST
from .AVL import AVL
from .RBT import RBT

def build_bst(values):
    tree = BST()
    for v in values:
        tree.insert(v)
    return tree

def build_avl(values):
    tree = AVL()
    for v in values:
        tree.insert(v)
    return tree

def build_rbt(values):
    tree = RBT()
    for v in values:
        tree.insert(v)
    return tree
