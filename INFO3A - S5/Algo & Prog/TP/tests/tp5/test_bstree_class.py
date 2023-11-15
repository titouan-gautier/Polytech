import pytest
from tests.conftest import import_stuff
from tests.tp5.test_btree_class import bfs_traversal, expected_height

import_stuff('btree')
import_stuff('bstree')

# beurk!
from tests.conftest import *


@pytest.mark.key("e3q1")
class TestIsBST:
    def test_bt_is_bst_empty(self, empty_tree):
        bt = BinaryTree(empty_tree)
        assert bt.is_bst()

    def test_bt_is_bst(self, input_ordered_tree):
        bt = BinaryTree(input_ordered_tree)
        assert bt.is_bst()

    @pytest.mark.parametrize("in_tree", [[1, 2], [1, None, 0], [1, None, 1], [1, 2, 0],
                                       [1, 2, 2], [1, 1, 0], [1, 1, 1],
                                       [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                       [6, 2, 11, 1, 4, 7, 12, None, None, 1, None, None, None, 12, 14],
                                       [6, 2, 11, 1, 4, 7, 12, None, None, 2, None, None, None, 12, 14],
                                       [6, 2, 11, 1, 7, 7, 12, None, None, 3, None, None, None, 12, 14]])
    def test_bt_is_not_bst(self, in_tree):
        bt = BinaryTree(in_tree)
        assert not bt.is_bst()


@pytest.mark.key("e3q2")
class TestLookup:

    def test_lookup_empty(self, empty_tree):
        bst = BSTree(empty_tree)
        assert all(bst.lookup(i) is None for i in range(10))

    def test_lookup(self, input_ordered_tree):
        bst = BSTree(input_ordered_tree)
        in_values = set(i for i in input_ordered_tree if i is not None)
        out_values = set(range(10)) - in_values
        assert all(bst.lookup(i).__getitem__() == i for i in in_values)
        assert all(bst.lookup(i).__getitem__() is None for i in out_values)


@pytest.mark.key("e3q3")
class TestInsert:

    @pytest.mark.parametrize("insert_list, height, in_tree", [([42], 0, [42]),
                                       ([42, 42], 0, [42]),
                                       ([42] * 3, 0, [42]),
                                       ([1, 2, 3, 1], 2, [1, None, 2, None, None, None, 3]),
                                       ([1, 3, 2, 2], 2, [1, None, 3, None, None, 2]),
                                       ([3, 2, 1, 3], 2, [3, 2, None, 1]),
                                       ([3, 1, 2, 1], 2, [3, 1, None, None, 2]),
                                       ([2, 1, 3, 2], 1, [2, 1, 3]),
                                       ([2, 3, 1, 3], 1, [2, 1, 3])])
    def test_insert_empty(self, empty_tree, insert_list, height, in_tree):
        bst = BSTree(empty_tree)
        for i in insert_list:
            bst.insert(i)
        assert all(
            (n is None and i is None) or (n is not None and n.__getitem__() == i)
            for n, i in zip(list(bfs_traversal(bst.root(), height)),
                            in_tree)), \
            "tree structure is not correct"

    def test_insert_none(self, input_ordered_tree):
        bst = BSTree(input_ordered_tree)
        in_values = set(i for i in input_ordered_tree if i is not None)
        height: int = expected_height(len(input_ordered_tree))
        for i in in_values:
            bst.insert(i)
        assert all(
            (n is None and i is None) or (n is not None and n.__getitem__() == i)
            for n, i in zip(list(bfs_traversal(bst.root(), height)),
                            input_ordered_tree)), \
            "tree structure is not correct"


@pytest.mark.key("e3q4")
class TestRemove:
    pass
