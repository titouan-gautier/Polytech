import pytest
import importlib
import re

from tests.setup import BSTREE_STRUCT_NAMES, BSTREE_NAMES, TP_CLASS
from tests.conftest import FakeStruct, fake_function, input_tree_with_null, input_tree, empty_tree, input_unique_tree

try:
    btree_module = importlib.import_module(TP_CLASS['bstree']['module'])     # may raise ImportError

    for name in BTREE_NAMES:
        if not hasattr(btree_module, name):
            if name in BTREE_STRUCT_NAMES:
                setattr(btree_module, name, FakeStruct)
            else:
                setattr(btree_module, name, fake_function)
        # it is then "safe" to expose the student's code
        globals()[name] = getattr(btree_module, name)
except ImportError:
    pass



# @pytest.mark.key("e3q1")
# class TestIsBST:
#
#         def test_bt_is_bst_empty(self, empty_tree):
#             bt = bt_new(empty_tree)
#             assert bt_is_bst(bt)
#
#         def test_bt_is_bst(self, input_tree):
#             bt = bt_new(input_tree)
#             assert bt_is_bst(bt)
#
#         def test_bt_is_not_bst(self, input_tree):
#             bt = bt_new(input_tree)
#             bt_root(bt).left.right.data = 42
#             assert not bt_is_bst(bt)
