from __future__ import annotations
from tp5.btree import BinaryTree, Node


class BSTree(BinaryTree):

    def is_bst(self) -> bool:
        return self.is_bst_rec(self.root_node)

    def is_bst_rec(self, current: Node) -> int | bool:

        if current.is_leaf():
            print(current.value)
            return current.value
        else:
            return self.is_bst_rec(current.left()) > current.value or self.is_bst_rec(current.right()) < current.value

if __name__ == "__main__":
    bst = BSTree([4, 2, 6])
    print(bst.is_bst())
