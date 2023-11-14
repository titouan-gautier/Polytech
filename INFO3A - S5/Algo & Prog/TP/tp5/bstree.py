from __future__ import annotations
from tp5.btree import BinaryTree, Node


class BSTree(BinaryTree):

    def bst_lookup(self, key: int) -> Node:
        return self.bst_lookup_rec(self.root_node, key)

    def bst_lookup_rec(self, current: Node, key: int) -> Node | None:

        if current.value == key:
            return current
        elif current.is_leaf():
            return None
        else:
            if key < current.value:
                return self.bst_lookup_rec(current.left(), key)
            if key > current.value:
                return self.bst_lookup_rec(current.right(), key)

    def bst_insert(self, key : int):
        return

    def bst_insert_rec(self, current: Node, previous : Node, key : int, done : bool) :

        if current.is_leaf():
            return None
        else:

            self.bst_insert_rec(current.left(), current, key, done)
            if current is not None and previous is not None :
                print(current.value, previous.value)
            if (current.value < key < previous.value) and done:
                print(True)
            self.bst_insert_rec(current.right() , current, key, done)

            return current


if __name__ == "__main__":
    bst = BSTree([6, 2, 11, 1, 4, 7, 12, None, None, 3, None, None, None, 12, 14])
    print(bst.bst_insert_rec(bst.root_node,None,5,False))
