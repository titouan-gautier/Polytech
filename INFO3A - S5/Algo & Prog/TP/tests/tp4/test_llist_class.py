import pytest
import random
import importlib

from tests.setup import LINKEDLIST_STRUCT_NAMES, TP_CLASS
from tests.conftest import FakeStruct

try:
    llist_module = importlib.import_module(TP_CLASS['llist']['module'])     # may raise ImportError

    for name in LINKEDLIST_STRUCT_NAMES:
        if not hasattr(llist_module, name):
            setattr(llist_module, name, FakeStruct)

        # it is then "safe" to expose the student's code
        cls = getattr(llist_module, name)
        globals()[name] = cls

        # aliases for the student's code
        if hasattr(cls, 'str'):
            setattr(cls, '__str__', lambda self: self.str())
        if hasattr(cls, 'len'):
            setattr(cls, '__len__', lambda self: self.len())
        if hasattr(cls, 'get'):
            setattr(cls, '__getitem__', lambda self, i: self.get())
        if hasattr(cls, 'set'):
            setattr(cls, '__setitem__', lambda self, i, item: self.set(i, item))
        if hasattr(cls, 'iter_cells'):
            setattr(cls, '__iter__', lambda self: self.iter_cells())
        if hasattr(cls, 'reversed_iter_cells'):
            setattr(cls, '__reversed__', lambda self: self.reversed_iter_cells())

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
        assert isinstance(LinkedList(), LinkedList)

    def test_ll_is_empty(self):
        ll = LinkedList()
        assert ll.is_empty() is True


@pytest.mark.key("e1q3")
class TestLenHeadTail:
    def test_ll_len_empty(self):
        ll = LinkedList()
        assert ll.__len__() == 0

    def test_ll_head_fails_empty(self):
        ll = LinkedList()
        pytest.raises(IndexError, ll.head)

    def test_ll_tail_fails_empty(self):
        ll = LinkedList()
        pytest.raises(IndexError, ll.tail)


@pytest.mark.key("e2q1")
@pytest.mark.parametrize("wrong_idx", [None, 0, 1])
class TestGetSet:
    def test_get_fails_idx(self, wrong_idx):
        ll = LinkedList()
        pytest.raises(IndexError, ll.__getitem__, idx=wrong_idx)

    def test_set_fails_idx(self, wrong_idx):
        ll = LinkedList()
        pytest.raises(IndexError, ll.__setitem__, idx=wrong_idx, item=42)


@pytest.mark.key("e2q2")
class TestInsert:
    def test_insert_head___getitem__(self, input_list):
        ll = LinkedList()
        cells: list[Cell] = []
        for e in input_list:
            ll.insert(e)
            cells.append(ll.head())
            assert ll.__getitem__(ll.head()) == e
            assert ll.__len__() == len(cells)
            assert not ll.is_empty()
        assert all(ll.__getitem__(c) == e for e, c in zip(input_list, cells))

    def test_insert_tail___getitem__(self, input_list):
        ll = LinkedList()
        cells: list[Cell] = []
        for e in input_list:
            ll.insert(e,  neighbor=None, after=False)
            cells.append(ll.tail())
            assert ll.__getitem__(ll.tail()) == e
            assert ll.__len__() == len(cells)
            assert not ll.is_empty()
        assert all(ll.__getitem__(c) == e for e, c in zip(input_list, cells))


@pytest.mark.key("e2q3")
class TestAppendPrepend:
    def test_prepend(self, input_list):
        ll = LinkedList()
        cells: list[Cell] = []
        for e in input_list:
            ll.prepend(e)
            cells.append(ll.head())
            assert ll.__getitem__(ll.head()) == e
            assert ll.__len__() == len(cells)
            assert not ll.is_empty()
        assert all(ll.__getitem__(c) == e for e, c in zip(input_list, cells))

    def test_append(self, input_list):
        ll = LinkedList()
        cells: list[Cell] = []
        for e in input_list:
            ll.append(e)
            cells.append(ll.tail())
            assert ll.__getitem__(ll.tail()) == e
            assert ll.__len__() == len(cells)
            assert not ll.is_empty()
        assert all(ll.__getitem__(c) == e for e, c in zip(input_list, cells))


@pytest.mark.key("e2q4")
class TestNewParam:
    def test_new_empty(self, empty_list):
        ll = LinkedList(empty_list)
        assert isinstance(ll, LinkedList)
        assert ll.__len__() == 0
        assert ll.is_empty()

    def test_new(self, input_list):
        ll = LinkedList(input_list)
        assert isinstance(ll, LinkedList)
        assert ll.__len__() == len(input_list)
        assert not ll.is_empty()
        assert ll.__getitem__(ll.head()) == input_list[0]
        assert ll.__getitem__(ll.tail()) == input_list[-1]


@pytest.mark.key("e2q5")
class TestIter:
    def test_iter_empty(self):
        ll = LinkedList()
        assert list(ll.__iter__()) == []

    def test_iter(self, input_list):
        ll = LinkedList(input_list)
        assert all(ll.__getitem__(c) == e for c, e in zip(ll.__iter__(), input_list))

    def test_insert_iter(self, input_list):
        ll = LinkedList()
        ll.insert(input_list[0])
        permutation_l: list[int] = [input_list[0]]
        for i in range(1, len(input_list)):
            idx: int = random.choice(range(i))
            neighbor: Cell = list(ll.__iter__())[idx]
            after: bool = random.choice([True, False])
            ll.insert(input_list[i], neighbor, after)
            permutation_l.insert(idx + 1 if after else idx, input_list[i])
            assert ll.__len__() == i + 1
        assert all(ll.__getitem__(c) == e for c, e in zip(ll.__iter__(), permutation_l))

    def test_set_iter(self, input_list):
        ll = LinkedList(input_list)
        random.shuffle(input_list)
        for c, e in zip(ll.__iter__(), input_list):
            ll.__setitem__(c, e)
        assert all(ll.__getitem__(c) == e for c, e in zip(ll.__iter__(), input_list))


@pytest.mark.key("e2q6")
class TestReversedIter:

    def test_reversed_iter(self, input_list):
        ll = LinkedList(input_list)
        assert all(ll.__getitem__(c) == e for c, e in zip(ll.__reversed__(), reversed(input_list)))


@pytest.mark.key("e3q1")
class TestStr:
    def test_str(self, input_list_with_null):
        ll = LinkedList(input_list_with_null)
        input_list_with_null = input_list_with_null or []
        assert ll.__str__() == str(input_list_with_null)


@pytest.mark.key("e3q2")
class TestLookupAndCellAt:
    def test_lookup(self, input_list):
        ll = LinkedList(input_list)
        for e in input_list:
            found: Cell = ll.lookup(e)
            assert ll.__getitem__(found) == e
            for c in ll.__iter__():
                if c is found:
                    break
                assert ll.__getitem__(c) != e

    @pytest.mark.parametrize("wrong_value", [None, -1, 1_111_111])
    def test_lookup_fails(self, input_list_with_null, wrong_value):
        ll = LinkedList(input_list_with_null)
        assert ll.lookup(wrong_value) is None

    def test_cell_at(self, input_list):
        ll = LinkedList(input_list)
        assert all(ll.__getitem__(ll.cell_at(i)) == e for i, e in enumerate(input_list))

    @pytest.mark.parametrize("wrong_idx", [None, -1, 1_111_111])
    def test_cell_at_out_of_bounds(self, input_list, wrong_idx):
        ll = LinkedList(input_list)
        if wrong_idx is None:
            pytest.raises(IndexError, ll.cell_at, len(input_list))
        else:
            pytest.raises(IndexError, ll.cell_at, wrong_idx)


@pytest.mark.key("e3q3")
class TestRemove:
    def test_remove(self, input_list_with_null):
        ll = LinkedList(input_list_with_null)
        in_l = input_list_with_null or []
        for max_p in reversed(range(len(in_l))):
            p: int = random.randint(0, max_p)
            ll.remove(ll.cell_at(p))
            in_l = in_l[:p] + in_l[p + 1:]
            assert all(ll.__getitem__(c) == e for c, e in zip(ll.__iter__(), in_l))
        assert ll.__len__() == 0
        assert ll.is_empty()


@pytest.mark.key("e3q4")
class TestExtend:
    def test_extend(self, input_list_with_null, input_list):
        l1 = LinkedList(input_list_with_null)
        in_l1 = input_list_with_null or []
        l2 = LinkedList(input_list)
        l1.extend(l2)
        assert l1.__len__() == len(in_l1) + len(input_list)
        assert l2.__len__() == len(input_list)
        assert all(l1.__getitem__(c) == e for c, e in zip(l1.__iter__(), in_l1 + input_list))
        assert all(l2.__getitem__(c) == e for c, e in zip(l2.__iter__(), input_list))
