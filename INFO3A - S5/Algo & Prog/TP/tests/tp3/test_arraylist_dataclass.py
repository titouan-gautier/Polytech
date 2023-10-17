import pytest
try:
    from tp3.arraylist import (ArrayList,
                               al_new,
                               al_len,
                               al_is_empty,
                               al_str,
                               al_get,
                               al_set,
                               al_lookup,
                               al_remove,
                               al_insert,
                               al_prepend,
                               al_append,
                               al_extend,
                               )
except ImportError:
    if 'ArrayList' not in globals():
        from dataclasses import dataclass

        @dataclass
        class ArrayList:
            def __post_init__(self):
                raise NotImplementedError("ArrayList class not found")
    if 'al_new' not in globals():
        def al_new(size, l=None):
            raise NotImplementedError("al_new function not found")
    if 'al_len' not in globals():
        def al_len(tab):
            raise NotImplementedError("al_len function not found")
    if 'al_is_empty' not in globals():
        def al_is_empty(tab):
            raise NotImplementedError("al_is_empty function not found")
    if 'al_str' not in globals():
        def al_str(tab):
            raise NotImplementedError("al_str function not found")
    if 'al_get' not in globals():
        def al_get(tab, i):
            raise NotImplementedError("al_get function not found")
    if 'al_set' not in globals():
        def al_set(tab, i, item):
            raise NotImplementedError("al_set function not found")
    if 'al_lookup' not in globals():
        def al_lookup(tab, item):
            raise NotImplementedError("al_lookup function not found")
    if 'al_remove' not in globals():
        def al_remove(tab, i):
            raise NotImplementedError("al_remove function not found")
    if 'al_insert' not in globals():
        def al_insert(tab, i, item):
            raise NotImplementedError("al_insert function not found")
    if 'al_prepend' not in globals():
        def al_prepend(tab, item):
            raise NotImplementedError("al_prepend function not found")
    if 'al_append' not in globals():
        def al_append(tab, item):
            raise NotImplementedError("al_append function not found")
    if 'al_extend' not in globals():
        def al_extend(tab1, tab2):
            raise NotImplementedError("al_extend function not found")

import random


@pytest.mark.key("e4q2")
class TestNew:
    def test_al_new_default(self, dsize):
        assert isinstance(al_new(dsize), ArrayList)

    def test_al_new(self, input_list_with_null, dsize):
        l = input_list_with_null        # alias
        size = 0 if l is None else len(l)
        assert isinstance(al_new(size + dsize, l), ArrayList)

    def test_al_new_fails_size(self, input_list, dsize):
        l = input_list        # alias
        pytest.raises(AssertionError, al_new, 0, l=l)
        pytest.raises(AssertionError, al_new, len(l) - 1 - dsize, l=l)


@pytest.mark.key("e4q3")
class TestLenAndEmpty:
    def test_al_len_empty(self, empty_list, dsize):
        l = empty_list        # alias
        assert al_len(al_new(dsize, l)) == 0

    def test_al_len(self, input_list, dsize):
        l = input_list        # alias
        assert al_len(al_new(len(l) + dsize, l)) == len(l)

    def test_al_is_empty(self, dsize):
        assert al_is_empty(al_new(dsize))

    def test_al_is_not_empty(self, input_list, dsize):
        assert not al_is_empty(al_new(len(input_list), input_list))


@pytest.mark.key("e4q4")
class TestStr:
    def test_al_str_empty(self, empty_list, dsize):
        l = empty_list        # alias
        str_repr = al_str(al_new(dsize, l))
        assert str_repr == "[]"

    def test_al_str(self, input_list, dsize):
        l = input_list        # alias
        str_repr = al_str(al_new(len(l) + dsize, l))
        assert str_repr == str(l)


@pytest.mark.key("e5q1")
class TestGet:
    def test_al_get(self, input_list, dsize):
        l = input_list        # alias
        al = al_new(len(l) + dsize, l)
        assert all(al_get(al, i) == l[i] for i in range(len(l)))

    def test_al_get_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(dsize, l)
        assert all(pytest.raises(IndexError, al_get, al, i=i) for i in range(-1, dsize + 1))

    def test_al_get_fails_out_of_bounds(self, input_list, dsize):
        l = input_list        # alias
        al = al_new(len(l) + dsize, l)
        assert pytest.raises(IndexError, al_get, al, i=-1)
        assert all(pytest.raises(IndexError, al_get, al, i=al_len(al) + i) for i in range(dsize))


@pytest.mark.key("e5q2")
class TestSet:
    def test_al_set(self, input_list, dsize):
        l = input_list        # alias
        al = al_new(len(l) + dsize, [0] * len(l))
        for i in range(len(l)):
            al_set(al, i, l[i])
        assert all(al_get(al, i) == l[i] for i in range(len(l)))
        assert al_len(al) == len(l)
        assert not al_is_empty(al)

    def test_al_set_chain(self, random_list_of_10):
        al = al_new(len(random_list_of_10), [0] * len(random_list_of_10))
        al_set(al_set(al_set(al_set(al, 0, 42), 1, 42), 2, 42), 3, 42)
        assert all(al_get(al, i) == 42 for i in range(4))
        assert all(al_get(al, i) == 0 for i in range(4, len(random_list_of_10)))
        assert not al_is_empty(al)
        assert al_len(al) == len(random_list_of_10)

    def test_al_set_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(dsize, l)
        assert all(pytest.raises(IndexError, al_set, al, i=i, item=42) for i in range(-1, dsize + 1))
        assert al_len(al) == 0
        assert al_is_empty(al)

    def test_al_set_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + dsize, [0] * len(l))
        assert pytest.raises(IndexError, al_set, al, i=-1, item=42)
        assert all(pytest.raises(IndexError, al_set, al, i=al_len(al) + i, item=42) for i in range(dsize))
        assert al_len(al) == len(l)
        assert not al_is_empty(al)


@pytest.mark.key("e5q3")
class TestLookup:
    def test_al_lookup(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + dsize, l)
        assert all(al_lookup(al, e) == l.index(e) for e in l)   # index rather than i because of duplicates

    def test_al_lookup_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(dsize, l)
        assert al_lookup(al, 42) is None

    def test_al_lookup_none(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + dsize, l)
        assert al_lookup(al, 442) is None


@pytest.mark.key("e5q4")
class TestRemove:

    def test_al_remove(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + dsize, l)
        al_remove(al, al_len(al) - 1)
        if len(l) == 1:     # refill the array list to be able to test removing the first element
            al = al_new(len(l) + dsize, l)
        al_remove(al, 0)
        l = l[1:-1]
        assert al_len(al) == len(l)
        assert all(al_get(al, j) == e for j, e in enumerate(l))
        max_len = al_len(al)
        for i in range(max_len - 1, -1, -1):
            pos = random.randint(0, i)
            al_remove(al, pos)
            l = l[:pos] + l[pos+1:]
            assert al_len(al) == len(l)
            assert not al_is_empty(al) if len(l) > 0 else al_is_empty(al)
        assert all(al_get(al, j) == e for j, e in enumerate(l))

    def test_al_remove_chain(self, random_list_of_10, dsize):
        l = random_list_of_10
        al = al_new(len(l) + dsize, l)
        al_remove(al_remove(al_remove(al_remove(al, al_len(al) - 1), 0), 1), 2)
        # (0) 1 (2) 3 (4) 5 6 7 8 (9)
        l = l[1:2] + l[3:4] + l[5:-1]
        assert all(al_get(al, i) == e for i, e in enumerate(l))
        assert not al_is_empty(al)
        assert al_len(al) == len(l)

    def test_al_remove_fails_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(dsize, l)
        assert all(pytest.raises(IndexError, al_remove, al, i=i) for i in range(-1, dsize + 1))
        assert al_len(al) == 0
        assert al_is_empty(al)

    def test_al_remove_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + dsize, l)
        assert pytest.raises(IndexError, al_remove, al, i=-1)
        assert all(pytest.raises(IndexError, al_remove, al, i=al_len(al) + i) for i in range(dsize))
        assert al_len(al) == len(l)
        assert not al_is_empty(al)


@pytest.mark.key("e5q5")
class TestInsert:

    def test_al_insert(self, input_list, dsize):
        l = input_list  # alias
        max_len = len(l) + 2 + dsize
        al = al_new(max_len, l)
        al_insert(al_insert(al, al_len(al), 42), 0, 42)
        l = [42] + l + [42]
        assert al_len(al) == len(l)
        assert all(al_get(al, j) == e for j, e in enumerate(l))
        for _ in range(dsize):
            pos = random.randint(0, al_len(al))
            al_insert(al, pos, 42 + pos)
            l = l[:pos] + [42 + pos] + l[pos:]
            assert not al_is_empty(al)
            assert al_len(al) == len(l)
        assert all(al_get(al, j) == e for j, e in enumerate(l))

    def test_al_insert_chain(self, random_list_of_10):
        l = random_list_of_10
        al = al_new(len(l) + 4, l)
        al_insert(al_insert(al_insert(al_insert(al, al_len(al), 42), 0, 42), 1, 42), 11, 42)
        # 0:42 1:42 2 3 4 5 6 7 8 9 10 11:42 12 13:42
        l.insert(0, 42)
        l.insert(len(l), 42)
        l.insert(1, 42)
        l.insert(11, 42)
        assert all(al_get(al, i) == e for i, e in enumerate(l))
        assert not al_is_empty(al)
        assert al_len(al) == len(l)

    def test_al_insert_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(1 + dsize, l)
        for i in range(dsize + 1):
            al_insert(al, random.randint(0, i), 42)
        assert all(al_get(al, i) == 42 for i in range(dsize + 1))
        assert al_len(al) == dsize + 1
        assert not al_is_empty(al)

    def test_al_insert_fails_out_of_bounds(self, input_list_with_null, dsize):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = al_new(size + dsize, l)
        assert pytest.raises(IndexError, al_insert, al, -1, 42)
        assert all(pytest.raises(IndexError, al_insert, al, al_len(al) + i, 42) for i in range(1, dsize))
        l = l or []
        assert al_len(al) == len(l)
        assert al_is_empty(al) == (len(l) == 0)

    def test_al_insert_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = al_new(size, l)
        assert all(pytest.raises(OverflowError, al_insert, al, i, 42) for i in range(0, size + 1))
        l = l or []
        assert al_len(al) == len(l)
        assert al_is_empty(al) == (len(l) == 0)


@pytest.mark.key("e5q6")
class TestPrependAppend:

    def test_al_prepend(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + 1 + dsize, l)
        for _ in range(dsize + 1):
            al_prepend(al, 42)
        l = [42] * (dsize + 1) + l
        assert not al_is_empty(al)
        assert al_len(al) == len(l)
        assert all(al_get(al, j) == e for j, e in enumerate(l))

    def test_al_prepend_chain(self, random_list_of_10):
        l = random_list_of_10
        al = al_new(len(l) + 4, l)
        al_prepend(al_prepend(al_prepend(al_prepend(al, 42), 42),42), 42)
        l = [42] * 4 + l
        assert all(al_get(al, i) == e for i, e in enumerate(l))
        assert not al_is_empty(al)
        assert al_len(al) == len(l)

    def test_al_prepend_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(1 + dsize, l)
        for _ in range(dsize + 1):
            al_prepend(al, 42)
        assert not al_is_empty(al)
        assert al_len(al) == dsize + 1
        assert all(al_get(al, j) == 42 for j in range(dsize + 1))

    def test_al_prepend_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = al_new(size, l)
        assert(pytest.raises(OverflowError, al_prepend, al, 42))
        l = l or []
        assert all(al_get(al, j) == e for j, e in enumerate(l))
        assert al_len(al) == len(l)
        assert al_is_empty(al) == (len(l) == 0)

    def test_al_append(self, input_list, dsize):
        l = input_list  # alias
        al = al_new(len(l) + 1 + dsize, l)
        for _ in range(dsize + 1):
            al_append(al, 42)
        l += [42] * (dsize + 1)
        assert not al_is_empty(al)
        assert al_len(al) == len(l)
        assert all(al_get(al, j) == e for j, e in enumerate(l))

    def test_al_append_chain(self, random_list_of_10):
        l = random_list_of_10
        al = al_new(len(l) + 4, l)
        al_append(al_append(al_append(al_append(al, 42), 42), 42), 42)
        l += [42] * 4
        assert all(al_get(al, i) == e for i, e in enumerate(l))
        assert not al_is_empty(al)
        assert al_len(al) == len(l)

    def test_al_append_empty(self, empty_list, dsize):
        l = empty_list  # alias
        al = al_new(1 + dsize, l)
        for _ in range(dsize + 1):
            al_append(al, 42)
        assert not al_is_empty(al)
        assert al_len(al) == dsize + 1
        assert all(al_get(al, j) == 42 for j in range(dsize + 1))

    def test_al_append_fails_overflow(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = al_new(size, l)
        assert(pytest.raises(OverflowError, al_append, al, 42))
        l = l or []
        assert all(al_get(al, j) == e for j, e in enumerate(l))
        assert al_len(al) == len(l)
        assert al_is_empty(al) == (len(l) == 0)


@pytest.mark.key("e5q7")
class TestExtend:

    def test_al_extend(self, random_list_of_10, input_list_with_null, dsize):
        l2 = input_list_with_null  # alias
        size2 = 0 if l2 is None else len(l2)
        al1 = al_new(len(random_list_of_10) + size2 + dsize, random_list_of_10)
        al2 = al_new(size2, l2)
        al_extend(al1, al2)
        l2 = l2 or []
        l1 = random_list_of_10 + l2
        assert all(al_get(al1, j) == e for j, e in enumerate(l1))
        assert not al_is_empty(al1)
        assert al_len(al1) == len(l1)
        assert all(al_get(al2, j) == e for j, e in enumerate(l2))
        assert not al_is_empty(al2) if len(l2) > 0 else al_is_empty(al2)
        assert al_len(al2) == len(l2)

    def test_al_extend_empty(self, empty_list, input_list_with_null, dsize):
        l1 = empty_list  # alias
        l2 = input_list_with_null        # alias
        size2 = 0 if l2 is None else len(l2)
        al1 = al_new(size2 + dsize, l1)     # empty list, with room for al2 elements
        al2 = al_new(size2, l2)             # random list (it may be empty as well)
        al_extend(al1, al2)
        l2 = l2 or []
        l = l2[:]           # /!\ cannot overwrite l1, otherwise next iter for l2 fails
        assert all(al_get(al1, j) == e for j, e in enumerate(l))
        assert not al_is_empty(al1) if len(l) > 0 else al_is_empty(al1)
        assert al_len(al1) == len(l)
        assert all(al_get(al2, j) == e for j, e in enumerate(l2))
        assert not al_is_empty(al2) if len(l2) > 0 else al_is_empty(al2)
        assert al_len(al2) == len(l2)

    def test_al_extend_fails_overflow(self, random_list_of_10, input_list, dsize):
        l2 = input_list  # alias
        al1 = al_new(len(random_list_of_10) + len(l2) - 1, random_list_of_10)
        al2 = al_new(len(l2), l2)
        assert (pytest.raises(OverflowError, al_extend, al1, tab2=al2))
        l1 = random_list_of_10
        assert all(al_get(al1, j) == e for j, e in enumerate(l1))
        assert not al_is_empty(al1)
        assert al_len(al1) == len(l1)
        assert all(al_get(al2, j) == e for j, e in enumerate(l2))
        assert not al_is_empty(al2) if len(l2) > 0 else al_is_empty(al2)
        assert al_len(al2) == len(l2)
