import pytest
import re
from typing import Iterator

from tests.conftest import import_stuff

import_stuff('btree')

# beurk!
from tests.conftest import *


##################
# Helper functions
##################

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
        if current is not None and (n_left(current) is not None or n_right(current) is not None):
            queue.append(n_left(current))
            queue.append(n_right(current))
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

    def test_bt_new_default(self):
        bt = bt_new()
        assert isinstance(bt, BinaryTree), "bt_new() does not return a BinaryTree"


@pytest.mark.key("e1q3")
class TestIsEmptyAndRoot:

    def test_bt_new_empty(self):
        bt = bt_new()
        bt_is_empty(bt), "bt_is_empty() should return True on an empty tree"

    def test_bt_new_root_fails(self):
        bt = bt_new()
        pytest.raises(IndexError, bt_root, bt), "bt_root() should raise an IndexError on an empty tree"


@pytest.mark.key("e1q4")
class TestNodeFunctions:

    def test_node_new_get(self):
        left = n_new(4)
        right = n_new(2)
        n = n_new(42, left, right)
        assert n_get(n) == 42
        assert n_get(left) == 4
        assert n_get(right) == 2

    def test_node_set(self):
        left = n_new(4)
        right = n_new(2)
        n = n_new(42, left, right)
        n_set(n, 24)
        n_set(left, 2)
        n_set(right, 4)
        assert n_get(n) == 24
        assert n_get(left) == 2
        assert n_get(right) == 4

    def test_node_left_right(self):
        left = n_new(4)
        right = n_new(2)
        n = n_new(42, left, right)
        assert n_left(n) is left
        assert n_right(n) is right
        assert n_get(n_left(n)) == 4
        assert n_get(n_right(n)) == 2
        assert n_left(left) is None
        assert n_right(left) is None
        assert n_left(right) is None
        assert n_right(right) is None

    def test_node_is_leaf(self):
        left = n_new(4)
        right = n_new(2)
        n = n_new(42, left, right)
        assert not n_is_leaf(n)
        assert n_is_leaf(left)
        assert n_is_leaf(right)


@pytest.mark.key("e1q5")
class TestNewWithTreeAsList:

    def test_bt_new_empty_tree(self, empty_tree):
        bt = bt_new(empty_tree)
        assert isinstance(bt, BinaryTree), "bt_new() does not return a BinaryTree"
        assert bt_is_empty(bt), "bt_is_empty() should return True on an empty tree"
        pytest.raises(IndexError, bt_root, bt), "bt_root() should raise an IndexError on an empty tree"

    def test_bt_new_with_param(self, input_tree):
        bt = bt_new(input_tree)
        height = expected_height(len(input_tree))
        in_tree = input_tree[:]
        if height > 0:
            in_tree += [None] * (2 ** (height + 1) - 1 - len(input_tree))
        assert isinstance(bt, BinaryTree), "bt_new() does not return a BinaryTree"
        assert not bt_is_empty(bt), "bt_is_empty() should return False on a non-empty tree"
        assert all(
            (n is None and i is None) or (n is not None and n_get(n) == i)
            for n, i in zip(list(bfs_traversal(bt_root(bt), height)),
                            in_tree)), \
            "tree structure is not correct"


@pytest.mark.key("e2q1")
class TestHeightAndSize:

    def test_bt_height_empty(self, empty_tree):
        bt = bt_new(empty_tree)
        assert bt_height(bt) == -1

    def test_bt_height(self, input_tree):
        bt = bt_new(input_tree)
        h = expected_height(len(input_tree))
        assert bt_height(bt) == h

    def test_bt_size(self, input_tree_with_null):
        in_tree = input_tree_with_null or []
        bt = bt_new(in_tree)
        expected_size = len(in_tree) - in_tree.count(None)
        assert bt_size(bt) == expected_size


@pytest.mark.key("e2q2")
class TestBtStr:

    def test_bt_str(self, input_tree):
        bt = bt_new(input_tree)
        height = expected_height(len(input_tree))
        exp_levels = [[e for e in input_tree[2 ** i - 1:2 ** (i+1) - 1]
                       if e is not None]
                      for i in range(height + 1)]
        str_levels = bt_str(bt).split('\n')
        assert len(str_levels) == height + 1
        int_levels = [[int(s) for s in re.findall(r"\d+", lvl)] for lvl in str_levels]
        assert all(lvl == expected for lvl, expected in zip(int_levels, exp_levels))


@pytest.mark.key("e5q1")
class TestBtIsEqual:

    def test_bt_is_equal(self, input_tree, input_tree_with_null):
        bt1 = bt_new(input_tree)
        bt2 = bt_new(input_tree_with_null)
        assert bt_is_equal(bt1, bt2) == (input_tree == input_tree_with_null)


@pytest.mark.key("e5q2")
class TestBtIsHeap:
    def test_bt_is_heap(self, input_tree_with_null):
        bt = bt_new(input_tree_with_null)
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

        assert bt_is_heap(bt) == expected_heap


@pytest.mark.key("e5q3")
class TestBtLCA:

    def test_bt_lca(self, input_unique_tree):
        intree = input_unique_tree  # alias
        bt = bt_new(intree)
        ancestors = ancestor_idxs(len(intree))
        for i in range(len(intree)):
            for j in range(i, len(intree)):
                a, b = intree[i], intree[j]
                if a is None or b is None:
                    continue
                idx = 0
                while idx < min(len(ancestors[i]), len(ancestors[j])) and ancestors[i][idx] == ancestors[j][idx]:
                    idx += 1
                assert bt_lca(bt, a, b) == intree[ancestors[i][idx - 1]]


