import pytest
import random
from tests.conftest import import_stuff

import_stuff('arraylist')

# beurk!
from tests.conftest import *


@pytest.mark.key("e4q2")
class TestNew:
    def test_al_new_default(self, dsize):
        assert isinstance(ArrayList(dsize), ArrayList)

    def test_al_new(self, input_list_with_null, dsize):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        assert isinstance(ArrayList(size + dsize, l), ArrayList)

    def test_al_new_fails_size(self, input_list, dsize):
        l = input_list  # alias
        pytest.raises(AssertionError, ArrayList, 0, l=l)
        pytest.raises(AssertionError, ArrayList, len(l) - 1 - dsize, l=l)


@pytest.mark.key("e4q3")
class TestLenAndEmpty:
    def test_al_len_empty(self, empty_list, dsize):
        l = empty_list  # alias
        assert ArrayList(dsize, l).__len__() == 0

    def test_al_len(self, input_list, dsize):
        l = input_list  # alias
        assert ArrayList(len(l) + dsize, l).__len__() == len(l)

    def test_al_is_empty(self, dsize):
        assert ArrayList(dsize).is_empty()

    def test_al_is_not_empty(self, input_list, dsize):
        assert not ArrayList(len(input_list), input_list).is_empty()


@pytest.mark.key("e4q4")
class TestStr:
    def test_al_str_empty(self, empty_list, dsize):
        l = empty_list  # alias
        str_repr = ArrayList(dsize, l).__str__()
        assert str_repr == "[]"

    def test_al_str(self, input_list, dsize):
        l = input_list  # alias
        str_repr = ArrayList(len(l) + dsize, l).__str__()
        assert str_repr == str(l)


@pytest.mark.key("e5q1")
class TestGet:
    def test_al_get(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        assert all(al.__getitem__(i) == l[i] for i in range(len(l)))

    def test_al_get_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(dsize, l)
        assert all(pytest.raises(IndexError, al.__getitem__, i=i) for i in range(-1, dsize + 1))

    def test_al_get_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        assert pytest.raises(IndexError, al.__getitem__, i=-1)
        assert all(pytest.raises(IndexError, al.__getitem__, i=al.__len__() + i) for i in range(dsize))


@pytest.mark.key("e5q2")
class TestSet:
    def test_al_set(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, [0] * len(l))
        for i in range(len(l)):
            al.__setitem__(i, l[i])
        assert all(al.__getitem__(i) == l[i] for i in range(len(l)))
        assert al.__len__() == len(l)
        assert not al.is_empty()

    def test_al_set_chain(self, random_list_of_10):
        al = ArrayList(len(random_list_of_10), [0] * len(random_list_of_10))
        al.__setitem__(0, 42).__setitem__( 1, 42).__setitem__(2, 42).__setitem__(3, 42)
        assert all(al.__getitem__(i) == 42 for i in range(4))
        assert all(al.__getitem__(i) == 0 for i in range(4, len(random_list_of_10)))
        assert not al.is_empty()
        assert al.__len__() == len(random_list_of_10)

    def test_al_set_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(dsize, l)
        assert all(pytest.raises(IndexError, al.__setitem__, i=i, item=42) for i in range(-1, dsize + 1))
        assert al.__len__() == 0
        assert al.is_empty()

    def test_al_set_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, [0] * len(l))
        assert pytest.raises(IndexError, al.__setitem__, i=-1, item=42)
        assert all(pytest.raises(IndexError, al.__setitem__, i=al.__len__() + i, item=42) for i in range(dsize))
        assert al.__len__() == len(l)
        assert not al.is_empty()


@pytest.mark.key("e5q3")
class TestLookup:
    def test_al_lookup(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        assert all(al.lookup(e) == l.index(e) for e in l)  # index rather than i because of duplicates

    def test_al_lookup_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(dsize, l)
        assert al.lookup(42) is None

    def test_al_lookup_none(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        assert al.lookup(442) is None


@pytest.mark.key("e5q4")
class TestRemove:

    def test_al_remove(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        al.remove(al.__len__() - 1)
        if len(l) == 1:  # refill the array list to be able to test removing the first element
            al = ArrayList(len(l) + dsize, l)
        al.remove(0)
        l = l[1:-1]
        assert al.__len__() == len(l)
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))
        max_len = al.__len__()
        for i in range(max_len - 1, -1, -1):
            pos = random.randint(0, i)
            al.remove(pos)
            l = l[:pos] + l[pos + 1:]
            assert al.__len__() == len(l)
            assert not al.is_empty() if len(l) > 0 else al.is_empty()
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))

    def test_al_remove_chain(self, random_list_of_10, dsize):
        l = random_list_of_10
        al = ArrayList(len(l) + dsize, l)
        al.remove(al.__len__() - 1).remove(0).remove(1).remove(2)
        # (0) 1 (2) 3 (4) 5 6 7 8 (9)
        l = l[1:2] + l[3:4] + l[5:-1]
        assert all(al.__getitem__(i) == e for i, e in enumerate(l))
        assert not al.is_empty()
        assert al.__len__() == len(l)

    def test_al_remove_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(dsize, l)
        assert all(pytest.raises(IndexError, al.remove, i=i) for i in range(-1, dsize + 1))
        assert al.__len__() == 0
        assert al.is_empty()

    def test_al_remove_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + dsize, l)
        assert pytest.raises(IndexError, al.remove, i=-1)
        assert all(pytest.raises(IndexError, al.remove, i=al.__len__() + i) for i in range(dsize))
        assert al.__len__() == len(l)
        assert not al.is_empty()


@pytest.mark.key("e5q5")
class TestInsert:

    def test_al_insert(self, input_list, dsize):
        l = input_list  # alias
        max_len = len(l) + 2 + dsize
        al = ArrayList(max_len, l)
        al.insert(al.__len__(), 42).insert(0, 42)
        l = [42] + l + [42]
        assert al.__len__() == len(l)
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))
        for _ in range(dsize):
            pos = random.randint(0, al.__len__())
            al.insert(pos, 42 + pos)
            l = l[:pos] + [42 + pos] + l[pos:]
            assert not al.is_empty()
            assert al.__len__() == len(l)
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))

    def test_al_insert_chain(self, random_list_of_10):
        l = random_list_of_10
        al = ArrayList(len(l) + 4, l)
        al.insert(al.__len__(), 42).insert(0, 42).insert(1, 42).insert(11, 42)
        # 0:42 1:42 2 3 4 5 6 7 8 9 10 11:42 12 13:42
        l.insert(0, 42)
        l.insert(len(l), 42)
        l.insert(1, 42)
        l.insert(11, 42)
        assert all(al.__getitem__(i) == e for i, e in enumerate(l))
        assert not al.is_empty()
        assert al.__len__() == len(l)

    def test_al_insert_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(1 + dsize, l)
        for i in range(dsize + 1):
            al.insert(random.randint(0, i), 42)
        assert all(al.__getitem__(i) == 42 for i in range(dsize + 1))
        assert al.__len__() == dsize + 1
        assert not al.is_empty()

    def test_al_insert_fails_out_of_bounds(self, input_list_with_null, dsize):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = ArrayList(size + dsize, l)
        assert pytest.raises(IndexError, al.insert, -1, 42)
        assert all(pytest.raises(IndexError, al.insert, al.__len__() + i, 42) for i in range(1, dsize))
        l = l or []
        assert al.__len__() == len(l)
        assert al.is_empty() == (len(l) == 0)

    def test_al_insert_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = ArrayList(size, l)
        assert all(pytest.raises(OverflowError, al.insert, i, 42) for i in range(0, size + 1))
        l = l or []
        assert al.__len__() == len(l)
        assert al.is_empty() == (len(l) == 0)


@pytest.mark.key("e5q6")
class TestPrependAppend:

    def test_al_prepend(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + 1 + dsize, l)
        for _ in range(dsize + 1):
            al.prepend(42)
        l = [42] * (dsize + 1) + l
        assert not al.is_empty()
        assert al.__len__() == len(l)
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))

    def test_al_prepend_chain(self, random_list_of_10):
        l = random_list_of_10
        al = ArrayList(len(l) + 4, l)
        al.prepend(42).prepend(42).prepend(42).prepend(42)
        l = [42] * 4 + l
        assert all(al.__getitem__(i) == e for i, e in enumerate(l))
        assert not al.is_empty()
        assert al.__len__() == len(l)

    def test_al_prepend_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(1 + dsize, l)
        for _ in range(dsize + 1):
            al.prepend(42)
        assert not al.is_empty()
        assert al.__len__() == dsize + 1
        assert all(al.__getitem__(j) == 42 for j in range(dsize + 1))

    def test_al_prepend_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = ArrayList(size, l)
        assert (pytest.raises(OverflowError, al.prepend, 42))
        l = l or []
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))
        assert al.__len__() == len(l)
        assert al.is_empty() == (len(l) == 0)

    def test_al_append(self, input_list, dsize):
        l = input_list  # alias
        al = ArrayList(len(l) + 1 + dsize, l)
        for _ in range(dsize + 1):
            al.append(42)
        l += [42] * (dsize + 1)
        assert not al.is_empty()
        assert al.__len__() == len(l)
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))

    def test_al_append_chain(self, random_list_of_10):
        l = random_list_of_10
        al = ArrayList(len(l) + 4, l)
        al.append(42).append(42).append(42).append(42)
        l += [42] * 4
        assert all(al.__getitem__(i) == e for i, e in enumerate(l))
        assert not al.is_empty()
        assert al.__len__() == len(l)

    def test_al_append_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = ArrayList(1 + dsize, l)
        for _ in range(dsize + 1):
            al.append(42)
        assert not al.is_empty()
        assert al.__len__() == dsize + 1
        assert all(al.__getitem__(j) == 42 for j in range(dsize + 1))

    def test_al_append_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = ArrayList(size, l)
        assert (pytest.raises(OverflowError, al.append, 42))
        l = l or []
        assert all(al.__getitem__(j) == e for j, e in enumerate(l))
        assert al.__len__() == len(l)
        assert al.is_empty() == (len(l) == 0)


@pytest.mark.key("e5q7")
class TestExtend:

    def test_al_extend(self, random_list_of_10, input_list_with_null, dsize):
        l2 = input_list_with_null  # alias
        size2 = 0 if l2 is None else len(l2)
        al1 = ArrayList(len(random_list_of_10) + size2 + dsize, random_list_of_10)
        al2 = ArrayList(size2, l2)
        al1.extend(al2)
        l2 = l2 or []
        l1 = random_list_of_10 + l2
        assert all(al1.__getitem__(j) == e for j, e in enumerate(l1))
        assert not al1.is_empty()
        assert al1.__len__() == len(l1)
        assert all(al2.__getitem__(j) == e for j, e in enumerate(l2))
        assert not al2.is_empty() if len(l2) > 0 else al2.is_empty()
        assert al2.__len__() == len(l2)

    def test_al_extend_empty(self, empty_list, input_list_with_null, dsize):
        l1 = empty_list  # alias
        l2 = input_list_with_null  # alias
        size2 = 0 if l2 is None else len(l2)
        al1 = ArrayList(size2 + dsize, l1)  # empty list, with room for al2 elements
        al2 = ArrayList(size2, l2)  # random list (it may be empty as well)
        al1.extend(al2)
        l2 = l2 or []
        l = l2[:]  # /!\ cannot overwrite l1, otherwise next iter for l2 fails
        assert all(al1.__getitem__(j) == e for j, e in enumerate(l))
        assert not al1.is_empty() if len(l) > 0 else al1.is_empty()
        assert al1.__len__() == len(l)
        assert all(al2.__getitem__(j) == e for j, e in enumerate(l2))
        assert not al2.is_empty() if len(l2) > 0 else al2.is_empty()
        assert al2.__len__() == len(l2)

    def test_al_extend_fails_overflow(self, random_list_of_10, input_list, dsize):
        l2 = input_list  # alias
        al1 = ArrayList(len(random_list_of_10) + len(l2) - 1, random_list_of_10)
        al2 = ArrayList(len(l2), l2)
        assert (pytest.raises(OverflowError, al1.extend, tab=al2))
        l1 = random_list_of_10
        assert all(al1.__getitem__(j) == e for j, e in enumerate(l1))
        assert not al1.is_empty()
        assert al1.__len__() == len(l1)
        assert all(al2.__getitem__(j) == e for j, e in enumerate(l2))
        assert not al2.is_empty() if len(l2) > 0 else al2.is_empty()
        assert al2.__len__() == len(l2)
