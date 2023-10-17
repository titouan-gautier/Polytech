import pytest
import importlib
import random

from tests.setup import LINKEDLIST_STRUCT_NAMES, LINKEDLIST_NAMES, TP_CLASS
from tests.conftest import FakeStruct, fake_function

try:
    llist_module = importlib.import_module(TP_CLASS['llist']['module'])     # may raise ImportError

    for name in LINKEDLIST_NAMES:
        if not hasattr(llist_module, name):
            if name in LINKEDLIST_STRUCT_NAMES:
                setattr(llist_module, name, FakeStruct)
            else:
                setattr(llist_module, name, fake_function)
        # it is then "safe" to expose the student's code
        globals()[name] = getattr(llist_module, name)
except ImportError:
    pass


@pytest.mark.key("e1q1")
class TestLList:
    def test_linked_list_struct(self):
        try:
            LinkedList()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True


@pytest.mark.key("e1q2")
class TestNewIsEmpty:
    def test_linked_list_empty(self):
        assert isinstance(ll_new(), LinkedList)

    def test_ll_is_empty(self):
        assert ll_is_empty(ll_new()) is True


@pytest.mark.key("e1q3")
class TestLenHeadTail:
    def test_ll_len_empty(self):
        ll = ll_new()
        assert ll_len(ll) == 0

    def test_ll_head_fails_empty(self):
        ll = ll_new()
        pytest.raises(IndexError, ll_head, ll)

    def test_ll_tail_fails_empty(self):
        ll = ll_new()
        pytest.raises(IndexError, ll_tail, ll)


@pytest.mark.key("e2q1")
@pytest.mark.parametrize("wrong_idx", [None, 0, 1])
class TestGetSet:
    def test_get_fails_idx(self, wrong_idx):
        ll = ll_new()
        pytest.raises(IndexError, ll_get, ll, idx=wrong_idx)

    def test_set_fails_idx(self, wrong_idx):
        ll = ll_new()
        pytest.raises(IndexError, ll_set, ll, idx=wrong_idx, item=42)


@pytest.mark.key("e2q2")
class TestInsert:
    def test_insert_head_get(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            ll_insert(ll, e)
            cells.append(ll_head(ll))
            assert ll_get(ll, ll_head(ll)) == e
            assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(ll_get(ll, c) == e for e, c in zip(input_list, cells))

    def test_insert_tail_get(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            ll_insert(ll, e,  neighbor=None, after=False)
            cells.append(ll_tail(ll))
            assert ll_get(ll, ll_tail(ll)) == e
            assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(ll_get(ll, c) == e for e, c in zip(input_list, cells))


@pytest.mark.key("e2q3")
class TestAppendPrepend:
    def test_prepend(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            ll_prepend(ll, e)
            cells.append(ll_head(ll))
            assert ll_get(ll, ll_head(ll)) == e
            assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(ll_get(ll, c) == e for e, c in zip(input_list, cells))

    def test_append(self, input_list):
        ll = ll_new()
        cells: list[Cell] = []
        for e in input_list:
            ll_append(ll, e)
            cells.append(ll_tail(ll))
            assert ll_get(ll, ll_tail(ll)) == e
            assert ll_len(ll) == len(cells)
            assert not ll_is_empty(ll)
        assert all(ll_get(ll, c) == e for e, c in zip(input_list, cells))


@pytest.mark.key("e2q4")
class TestNewParam:
    def test_new_empty(self, empty_list):
        ll = ll_new(empty_list)
        assert isinstance(ll, LinkedList)
        assert ll_len(ll) == 0
        assert ll_is_empty(ll)

    def test_new(self, input_list):
        ll = ll_new(input_list)
        assert isinstance(ll, LinkedList)
        assert ll_len(ll) == len(input_list)
        assert not ll_is_empty(ll)
        assert ll_get(ll, ll_head(ll)) == input_list[0]
        assert ll_get(ll, ll_tail(ll)) == input_list[-1]


@pytest.mark.key("e2q5")
class TestIter:
    def test_iter_empty(self):
        ll = ll_new()
        assert list(ll_iter_cells(ll)) == []

    def test_iter(self, input_list):
        ll = ll_new(input_list)
        assert all(ll_get(ll, c) == e for c, e in zip(ll_iter_cells(ll), input_list))

    def test_insert_iter(self, input_list):
        ll = ll_insert(ll_new(), input_list[0])
        permutation_l: list[int] = [input_list[0]]
        for i in range(1, len(input_list)):
            idx: int = random.choice(range(i))
            neighbor: Cell = list(ll_iter_cells(ll))[idx]
            after: bool = random.choice([True, False])
            ll_insert(ll, input_list[i], neighbor, after)
            permutation_l.insert(idx + 1 if after else idx, input_list[i])
            assert ll_len(ll) == i + 1
        assert all(ll_get(ll, c) == e for c, e in zip(ll_iter_cells(ll), permutation_l))

    def test_set_iter(self, input_list):
        ll = ll_new(input_list)
        random.shuffle(input_list)
        for c, e in zip(ll_iter_cells(ll), input_list):
            ll_set(ll, c, e)
        assert all(ll_get(ll, c) == e for c, e in zip(ll_iter_cells(ll), input_list))


@pytest.mark.key("e2q6")
class TestReversedIter:

    def test_reversed_iter(self, input_list):
        ll = ll_new(input_list)
        assert all(ll_get(ll, c) == e for c, e in zip(ll_reversed_iter_cells(ll), reversed(input_list)))


@pytest.mark.key("e3q1")
class TestStr:
    def test_str(self, input_list_with_null):
        ll = ll_new(input_list_with_null)
        input_list_with_null = input_list_with_null or []
        assert ll_str(ll) == str(input_list_with_null)


@pytest.mark.key("e3q2")
class TestLookupAndCellAt:
    def test_lookup(self, input_list):
        ll = ll_new(input_list)
        for e in input_list:
            found: Cell = ll_lookup(ll, e)
            assert ll_get(ll, found) == e
            for c in ll_iter_cells(ll):
                if c is found:
                    break
                assert ll_get(ll, c) != e

    @pytest.mark.parametrize("wrong_value", [None, -1, 1_111_111])
    def test_lookup_fails(self, input_list_with_null, wrong_value):
        ll = ll_new(input_list_with_null)
        assert ll_lookup(ll, wrong_value) is None

    def test_cell_at(self, input_list):
        ll = ll_new(input_list)
        assert all(ll_get(ll, ll_cell_at(ll, i)) == e for i, e in enumerate(input_list))

    @pytest.mark.parametrize("wrong_idx", [None, -1, 1_111_111])
    def test_cell_at_out_of_bounds(self, input_list, wrong_idx):
        ll = ll_new(input_list)
        if wrong_idx is None:
            pytest.raises(IndexError, ll_cell_at, ll, len(input_list))
        else:
            pytest.raises(IndexError, ll_cell_at, ll, wrong_idx)


@pytest.mark.key("e3q3")
class TestRemove:
    def test_remove(self, input_list_with_null):
        ll = ll_new(input_list_with_null)
        in_l = input_list_with_null or []
        for max_p in reversed(range(len(in_l))):
            p: int = random.randint(0, max_p)
            ll_remove(ll, ll_cell_at(ll, p))
            in_l = in_l[:p] + in_l[p + 1:]
            assert all(ll_get(ll, c) == e for c, e in zip(ll_iter_cells(ll), in_l))
        assert ll_len(ll) == 0
        assert ll_is_empty(ll)


@pytest.mark.key("e3q4")
class TestExtend:
    def test_extend(self, input_list_with_null, input_list):
        l1 = ll_new(input_list_with_null)
        in_l1 = input_list_with_null or []
        l2 = ll_new(input_list)
        ll_extend(l1, l2)
        assert ll_len(l1) == len(in_l1) + len(input_list)
        assert ll_len(l2) == len(input_list)
        assert all(ll_get(l1, c) == e for c, e in zip(ll_iter_cells(l1), in_l1 + input_list))
        assert all(ll_get(l2, c) == e for c, e in zip(ll_iter_cells(l2), input_list))
