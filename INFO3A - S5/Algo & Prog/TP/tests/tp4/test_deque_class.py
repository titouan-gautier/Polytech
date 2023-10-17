import pytest
import importlib

from tests.setup import DEQUE_STRUCT_NAMES, TP_CLASS
from tests.conftest import FakeStruct

try:
    deque_module = importlib.import_module(TP_CLASS['deque']['module'])     # may raise ImportError

    for name in DEQUE_STRUCT_NAMES:
        if not hasattr(deque_module, name):
            setattr(deque_module, name, FakeStruct)

        # it is then "safe" to expose the student's code
        globals()[name] = getattr(deque_module, name)

        # aliases for the student's code
        if hasattr(name, 'str'):
            setattr(name, '__str__', lambda self: self.str())
        if hasattr(name, 'len'):
            setattr(name, '__len__', lambda self: self.len())

except ImportError:
    pass


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
