from __future__ import annotations
from collections import deque


class Node:
    value: int
    left_node: Node
    right_node: Node

    def __init__(self, value: int | None = None, left: Node | None = None, right: Node | None = None):
        self.left_node = left
        self.right_node = right
        self.value = value

    def get(self) -> int:
        return self.value

    def set(self, value: int) -> Node:
        self.value = value
        return self

    def left(self) -> Node:
        return self.left_node

    def right(self) -> Node:
        return self.right_node

    def is_leaf(self) -> bool:
        return self.right_node is None and self.left_node is None


class BinaryTree:
    root_node: Node | None
    height_node: int

    def __init__(self, nodes: list[int | None] | None = None):
        if nodes is None or nodes == []:
            self.root_node = None
            self.height_node = -1
        else:
            self.root_node = self.build_bt(nodes)
            self.height_node = self.height_recursive(self.root_node)

    def build_bt(self, nodes: list[int | None] | None = None, i: int = 0):

        if i >= len(nodes) or nodes[i] is None:
            return Node()
        else:
            node = Node(nodes[i])

            gauche = self.build_bt(nodes, 2 * i + 1)
            droite = self.build_bt(nodes, 2 * i + 2)

            node.left_node = gauche
            node.right_node = droite

            return node

    def is_empty(self) -> bool:
        return self.root_node is None

    def root(self) -> Node:
        if self.is_empty():
            raise IndexError()

        return self.root_node

    def height(self) -> int:

        if self.is_empty():
            return -1
        else:
            return self.height_recursive(self.root_node) - 1

    def height_recursive(self, current: Node):

        if current.is_leaf():
            return 0
        else:
            gauche = self.height_recursive(current.left())
            droite = self.height_recursive(current.right())

            return max(gauche, droite) + 1

    def __len__(self):

        if self.is_empty():
            return 0
        else:
            return self.bt_len(self.root_node)

    def bt_len(self, current: Node):

        if current.is_leaf():
            return 0
        else:
            gauche = self.bt_len(current.left())
            droite = self.bt_len(current.right())

            return gauche + droite + 1

    def __str__(self) -> str:
        res = self.bt_str()

        str = ""

        for i in range(len(res)):
            a = ""
            for j in range(len(res[i])):
                a += f"{res[i][j]} "
            if i == len(res) - 1:
                str += a
            else:
                str += a + "\n"

        return str

    def bt_str(self):

        if self.is_empty():
            return []

        result = []
        queue = deque()
        queue.append(self.root_node)

        while queue:
            level_result = []  # Crée un tableau pour le niveau actuel
            level_size = len(queue)  # Nombre de nœuds dans le niveau actuel

            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(node.get())

                if node.left():
                    queue.append(node.left())
                if node.right():
                    queue.append(node.right())

            result.append(level_result)

        return result[:len(result) - 1]

    def __eq__(self, other):
        if self.root_node is not None and other.root_node is not None:
            return self.bt_eq(self.root_node, other.root_node, True)
        else:
            return False

    def bt_eq(self, current1: Node, current2: Node, res: bool):

        if current1.is_leaf() and current2.is_leaf():
            return res
        else:

            if res:
                if current1 is not None and current2 is not None:
                    res = self.eq_node(current1, current2)
            else:
                return False

            if res:
                if current1 is not None and current2 is not None:
                    res = self.bt_eq(current1.left(), current2.left(), res)
                    res = self.bt_eq(current1.right(), current2.right(), res)

            return res

    def eq_node(self, current1: Node, current2: Node) -> bool:
        return current1.value == current2.value and current1.left().value == current2.left().value and current1.right().value == current1.right().value

    def is_heap(self) -> bool:
        if self.root_node is not None:
            return self.is_heap_rec(self.root_node, True)
        else:
            return True

    def is_heap_rec(self, current: Node, res: bool):

        if current.is_leaf():
            return True
        else:

            if res:
                res = self.is_heap_rec2(current, current.value, True)

            if res:
                res = self.is_heap_rec(current.left(), res)
            if res:
                res = self.is_heap_rec(current.right(), res)

            return res

    def is_heap_rec2(self, current: Node, val: int, res: bool):

        if current.is_leaf():

            if current.value is not None:
                if current.value > val:
                    return False
                else:
                    return True
            else:
                return True

        else:

            if current.value > val:
                res = False

            if res:
                res = self.is_heap_rec2(current.left(), val, res)
            if res:
                res = self.is_heap_rec2(current.right(), val, res)

            return res

    def bt_lca(self):
        return
    #Trouver l'ancetre le plus profond, c'est a dire le noeud le plus profond a partir du quel ont peut acceder à a et b deux noeud quelcoqnue.
    #Tester recursivenement pour root puis droite et gauche puis .... et renvoyer une bool et stocker le node le plus prfond trouver
    #Si bool est fausse retourner le node stocké.

    def bt_lca_rec2(self,current : Node):
        return


if __name__ == "__main__":
    bt = BinaryTree([2,1,4,0,None,3,5])
    print(bt)

