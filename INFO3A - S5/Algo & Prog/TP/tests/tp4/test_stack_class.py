import pytest
import importlib

from tests.setup import STACK_STRUCT_NAMES, TP_CLASS
from tests.conftest import FakeStruct

try:
    stack_module = importlib.import_module(TP_CLASS['stack_deque']['module'])     # may raise ImportError

    for name in STACK_STRUCT_NAMES:
        if not hasattr(stack_module, name):
            setattr(stack_module, name, FakeStruct)

        # it is then "safe" to expose the student's code
        globals()[name] = getattr(stack_module, name)

        # aliases for the student's code
        if hasattr(name, 'str'):
            setattr(name, '__str__', lambda self: self.str())
        if hasattr(name, 'size'):
            setattr(name, '__len__', lambda self: self.len())

except ImportError:
    pass


@pytest.mark.key("e8q1")
class TestStack:

    def test_s_new_default(self):
        s = Stack()
        assert isinstance(s, Stack)

    def test_s_new_custom_size(self, dsize):
        s = Stack(dsize)
        assert isinstance(s, Stack)

    def test_s_size_empty_stack(self, dsize):
        s = Stack(dsize)
        assert s.__len__() == 0

    def test_s_is_empty(self, dsize):
        s = Stack(dsize)
        assert s.is_empty()

    def test_s_size_push(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for i, e in enumerate(l):
            s.push(e)
            assert s.__len__() == i + 1

    def test_s_size_pop(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
        assert s.__len__() == len(l)
        for i in range(len(l)):
            s.pop()
            assert s.__len__() == len(l) - 1 - i

    def test_s_is_empty_push(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
            assert not s.is_empty()

    def test_s_is_empty_pop(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
        assert not s.is_empty()
        for _ in range(len(l) - 1):
            s.pop()
            assert not s.is_empty()
        s.pop()
        assert s.is_empty()

    def test_s_top_push(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
            assert s.top() == e

    def test_s_top_pop(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
            assert s.top() == e
        for e in reversed(l):
            assert s.top() == e
            s.pop()

    def test_s_str_empty(self, dsize):
        s = Stack(dsize)
        assert s.__str__() == "[]"

    def test_s_str(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for i, e in enumerate(l):
            s.push(e)
        assert s.__str__() == str(l)

    def test_s_pop_fails_empty(self, dsize):
        s = Stack(dsize)
        pytest.raises(IndexError, s.pop)

    def test_s_top_fails_empty(self, dsize):
        s = Stack(dsize)
        pytest.raises(IndexError, s.top)

    def test_s_pop_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
        for _ in range(len(l)):
            s.pop()
        pytest.raises(IndexError, s.pop)
