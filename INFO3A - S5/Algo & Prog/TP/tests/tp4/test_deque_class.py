import pytest
from tests.conftest import import_stuff

import_stuff('deque')

# beurk!
from tests.conftest import *


@pytest.mark.key("e6q1")
class TestDeque:
    def test_d_new_default(self):
        d = Deque()
        assert isinstance(d, Deque)

    def test_d_is_empty(self):
        d = Deque()
        assert d.is_empty()

    def test_d_len_empty(self):
        d = Deque()
        assert d.__len__() == 0

    def test_d_str_empty(self):
        d = Deque()
        assert d.__str__() == "[]"

    def test_d_front_fails_empty(self):
        d = Deque()
        pytest.raises(IndexError, d.front)

    def test_d_rear_fails_empty(self):
        d = Deque()
        pytest.raises(IndexError, d.front)

    def test_d_push_front(self, input_list):
        d = Deque()
        l = input_list
        for i in l:
            d.push_front(i)
            assert d.front() == i
            assert d.rear() == l[0]
        assert d.__str__() == str(l[::-1])

    def test_d_push_front_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_front(i)
        assert d.__len__() == len(l)

    def test_d_push_front_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_front(i)
        if len(l) == 0:
            assert d.is_empty()
        else:
            assert not d.is_empty()

    def test_d_push_rear(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_rear(i)
            assert d.rear() == i
        assert d.__str__() == str(l)

    def test_d_push_rear_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_rear(i)
        assert d.__len__() == len(l)

    def test_d_push_rear_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_rear(i)
        if len(l) == 0:
            assert d.is_empty()
        else:
            assert not d.is_empty()

    def test_d_pop_front(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_front(i)
        assert d.__str__() == str(l[::-1])
        for i in l:
            d.pop_front()
        assert d.__str__() == "[]"

    def test_d_pop_front_len(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_front(i)
        assert d.__len__() == len(l)
        for _ in l:
            d.pop_front()
        assert d.__len__() == 0

    def test_d_pop_front_is_empty(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_front(i)
        if len(l) == 0:
            assert d.is_empty()
        else:
            assert not d.is_empty()
        for i in l:
            d.pop_front()
        assert d.is_empty()

    def test_d_pop_rear(self, input_list_with_null):
        input_list_with_null = input_list_with_null or []
        d = Deque()
        l = input_list_with_null
        for i in l:
            d.push_rear(i)
        assert d.__str__() == str(l)
        for _ in l:
            d.pop_rear()
        assert d.__str__() == "[]"
