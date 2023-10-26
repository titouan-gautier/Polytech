import pytest
import importlib
import re

from tests.setup import BTREE_STRUCT_NAMES, TP_CLASS
from tests.conftest import FakeStruct, input_tree_with_null, input_tree, empty_tree


try:
    btree_module = importlib.import_module(TP_CLASS['btree']['module'])     # may raise ImportError

    for name in BTREE_STRUCT_NAMES:
        if not hasattr(btree_module, name):
            setattr(btree_module, name, FakeStruct)

        # it is then "safe" to expose the student's code
        cls = getattr(btree_module, name)
        globals()[name] = cls

        # aliases for the student's code
        if hasattr(cls, 'str'):
            setattr(cls, '__str__', lambda self: self.str())
        if hasattr(cls, 'size'):
            setattr(cls, '__len__', lambda self: self.size())
        if hasattr(cls, 'is_equal'):
            setattr(cls, '__eq__', lambda self: self.is_equal())

except ImportError:
    pass


##################
# Helper functions
##################
from typing import Iterator


def level_order_traversal(node: Node | None) -> Iterator[list[int]]:
    queue: list[Node | None] = [node]
    while len(queue) != 0:
        level: list[int] = []
        queue.append(None)  # stop mark for the next level
        while current := queue.pop(0) is not None:
            level.append(n_get(current))
            if n_left(current) is not None:
                queue.append(n_left(current))
            if n_right(current) is not None:
                queue.append(n_right(current))
        yield level


def bfs_traversal(node: Node | None, height: int):
    depth: int = 0
    queue: list[Node | None] = [node]
    while len(queue) != 0:
        current = queue.pop(0)
        yield current
        if current is not None and (current.left() is not None or current.right() is not None):
            queue.append(current.left())
            queue.append(current.right())
        elif depth <= height:
            queue.append(None)
            queue.append(None)
        if len(queue) > 2 ** depth:
            depth += 1


def expected_height(length: int) -> int:
    if length == 0:
        return -1
    i: int = 1
    while 2 ** i - 1 < length:
        i += 1
    return i - 1


def ancestor_idxs(length: int) :
    ancs: list[list[int]] = [[] for _ in range(length)]
    for k in reversed(range(length)):
        i = k
        while i >= 0:
            if ancs[i]:
                ancs[k] = ancs[i] + ancs[k]
                break
            ancs[k].insert(0, i)
            i = (i - 2) // 2 if i % 2 == 0 else (i - 1) // 2
    return ancs


##################
# Tests
##################
@pytest.mark.key("e1q1")
class TestBTree:
    def test_node_struct(self):
        try:
            Node()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True, "Node is not a dataclass"

    def test_btree_struct(self):
        try:
            BinaryTree()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True, "BinaryTree is not a dataclass"


@pytest.mark.key("e1q2")
class TestNew:

    def test_BinaryTree_default(self):
        bt = BinaryTree()
        assert isinstance(bt, BinaryTree), "BinaryTree() does not return a BinaryTree"


@pytest.mark.key("e1q3")
class TestIsEmptyAndRoot:

    def test_BinaryTree_empty(self):
        bt = BinaryTree()
        bt.is_empty(), "bt.is_empty() should return True on an empty tree"

    def test_BinaryTree_root_fails(self):
        bt = BinaryTree()
        pytest.raises(IndexError, bt.root), "bt.root() should raise an IndexError on an empty tree"


@pytest.mark.key("e1q4")
class TestNodeFunctions:

    def test_node_new_get(self):
        left = Node(4)
        right = Node(2)
        n = Node(42, left, right)
        assert n.get() == 42
        assert left.get() == 4
        assert right.get() == 2

    def test_node_set(self):
        left = Node(4)
        right = Node(2)
        n = Node(42, left, right)
        n.set(24)
        left.set(2)
        right.set(4)
        assert n.get() == 24
        assert left.get() == 2
        assert right.get() == 4

    def test_node_left_right(self):
        left = Node(4)
        right = Node(2)
        n = Node(42, left, right)
        assert n.left() is left
        assert n.right() is right
        assert n.left().get() == 4
        assert n.right().get() == 2
        assert left.left() is None
        assert left.right() is None
        assert right.left() is None
        assert right.right() is None

    def test_node_is_leaf(self):
        left = Node(4)
        right = Node(2)
        n = Node(42, left, right)
        assert not n.is_leaf()
        assert left.is_leaf()
        assert right.is_leaf()


@pytest.mark.key("e1q5")
class TestNewWithTreeAsList:

    def test_BinaryTree_empty_tree(self, empty_tree):
        bt = BinaryTree(empty_tree)
        assert isinstance(bt, BinaryTree), "BinaryTree() does not return a BinaryTree"
        assert bt.is_empty(), "bt.is_empty() should return True on an empty tree"
        pytest.raises(IndexError, bt.root), "bt.root() should raise an IndexError on an empty tree"

    def test_BinaryTree_with_param(self, input_tree):
        bt = BinaryTree(input_tree)
        height = expected_height(len(input_tree))
        if height > 0:
            input_tree += [None] * (2 ** (height + 1) - 1 - len(input_tree))
        assert isinstance(bt, BinaryTree), "BinaryTree() does not return a BinaryTree"
        assert not bt.is_empty(), "bt.is_empty() should return False on a non-empty tree"
        assert all(
            (n is None and i is None) or (n is not None and n.get() == i)
            for n, i in zip(list(bfs_traversal(bt.root(), height)),
                            input_tree)), \
            "tree structure is not correct"


@pytest.mark.key("e2q1")
class TestHeightAndSize:

    def test_bt_height_empty(self, empty_tree):
        bt = BinaryTree(empty_tree)
        assert bt.height() == -1

    def test_bt_height(self, input_tree):
        bt = BinaryTree(input_tree)
        h = expected_height(len(input_tree))
        assert bt.height() == h

    def test_bt_size(self, input_tree_with_null):
        in_tree = input_tree_with_null or []
        bt = BinaryTree(in_tree)
        expected_size = len(in_tree) - in_tree.count(None)
        assert bt.__len__() == expected_size


@pytest.mark.key("e2q2")
class TestBtStr:

    def test_bt_str(self, input_tree):
        bt = BinaryTree(input_tree)
        height = expected_height(len(input_tree))
        exp_levels = [[e for e in input_tree[2 ** i - 1:2 ** (i+1) - 1]
                       if e is not None]
                      for i in range(height + 1)]
        str_levels = bt.__str__().split('\n')
        assert len(str_levels) == height + 1
        int_levels = [[int(s) for s in re.findall(r"\d+", lvl)] for lvl in str_levels]
        assert all(lvl == expected for lvl, expected in zip(int_levels, exp_levels))


@pytest.mark.key("e5q1")
class TestBtIsEqual:

    def test_bt_is_equal(self, input_tree, input_tree_with_null):
        bt1 = BinaryTree(input_tree)
        bt2 = BinaryTree(input_tree_with_null)
        assert bt1.__eq__(bt2) == (input_tree == input_tree_with_null)


@pytest.mark.key("e5q2")
class TestBtIsHeap:
    def test_bt_is_heap(self, input_tree_with_null):
        bt = BinaryTree(input_tree_with_null)
        in_tree = input_tree_with_null or []
        expected_heap = True
        for i in range(len(in_tree)):
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            if left_child_index < len(in_tree) \
                    and in_tree[left_child_index] is not None \
                    and in_tree[i] < in_tree[left_child_index]:
                expected_heap = False
                break

            if right_child_index < len(in_tree) \
                    and in_tree[right_child_index] is not None \
                    and in_tree[i] < in_tree[right_child_index]:
                expected_heap = False
                break

        assert bt.is_heap() == expected_heap


@pytest.mark.key("e5q3")
class TestBtLCA:

    def test_bt_lca(self):
        def test_bt_lca(self, input_unique_tree):
            intree = input_unique_tree  # alias
            bt = BinaryTree(intree)
            ancestors = ancestor_idxs(len(intree))
            for i in range(len(intree)):
                for j in range(i, len(intree)):
                    a, b = intree[i], intree[j]
                    if a is None or b is None:
                        continue
                    idx = 0
                    while idx < min(len(ancestors[i]), len(ancestors[j])) and ancestors[i][idx] == ancestors[j][idx]:
                        idx += 1
                    assert bt.lca(a, b) == intree[ancestors[i][idx - 1]]




