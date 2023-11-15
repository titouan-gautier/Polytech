import pytest
from tests.conftest import import_stuff

import_stuff('deque')

# beurk!
from tests.conftest import *


@pytest.mark.key("e6q1")
class TestDeque:
    def test_d_new_default(self):
        d = d_new()
        assert isinstance(d, Deque)

    def test_d_is_empty(self):
        d = d_new()
        assert d_is_empty(d)

    def test_d_len_empty(self):
        d = d_new()
        assert d_len(d) == 0

    def test_d_str_empty(self):
        d = d_new()
        assert d_str(d) == "[]"

    def test_d_front_fails_empty(self):
        d = d_new()
        pytest.raises(IndexError, d_front, d)

    def test_d_rear_fails_empty(self):
        d = d_new()
        pytest.raises(IndexError, d_front, d)

    def test_d_push_front(self, input_list):
        d = d_new()
        l = input_list
        for i in l:
            d_push_front(d, i)
            assert d_front(d) == i
            assert d_rear(d) == l[0]
        assert d_str(d) == str(l[::-1])

    def test_d_push_front_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_front(d, i)
        assert d_len(d) == len(l)

    def test_d_push_front_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_front(d, i)
        if len(l) == 0:
            assert d_is_empty(d)
        else:
            assert not d_is_empty(d)

    def test_d_push_rear(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_rear(d, i)
            assert d_rear(d) == i
        assert d_str(d) == str(l)

    def test_d_push_rear_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_rear(d, i)
        assert d_len(d) == len(l)

    def test_d_push_rear_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_rear(d, i)
        if len(l) == 0:
            assert d_is_empty(d)
        else:
            assert not d_is_empty(d)

    def test_d_pop_front(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_front(d, i)
        assert d_str(d) == str(l[::-1])
        for i in l:
            d_pop_front(d)
        assert d_str(d) == "[]"

    def test_d_pop_front_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_front(d, i)
        assert d_len(d) == len(l)
        for _ in l:
            d_pop_front(d)
        assert d_len(d) == 0

    def test_d_pop_front_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_front(d, i)
        if len(l) == 0:
            assert d_is_empty(d)
        else:
            assert not d_is_empty(d)
        for i in l:
            d_pop_front(d)
        assert d_is_empty(d)

    def test_d_pop_rear(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = d_new()
        l = input_list_with_null
        for i in l:
            d_push_rear(d, i)
        assert d_str(d) == str(l)
        for _ in l:
            d_pop_rear(d)
        assert d_str(d) == "[]"

