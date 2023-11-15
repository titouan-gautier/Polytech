import pytest
from tests.conftest import import_stuff

import_stuff('stack_deque')

# beurk!
from tests.conftest import *


@pytest.mark.key("e8q1")
class TestStack:

    def test_s_new_default(self):
        s = s_new()
        assert isinstance(s, Stack)

    def test_s_new_custom_size(self, dsize):
        s = s_new(dsize)
        assert isinstance(s, Stack)

    def test_s_size_empty_stack(self, dsize):
        s = s_new(dsize)
        assert s_size(s) == 0

    def test_s_is_empty(self, dsize):
        s = s_new(dsize)
        assert s_is_empty(s)

    def test_s_size_push(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for i, e in enumerate(l):
            s_push(s, e)
            assert s_size(s) == i + 1

    def test_s_size_pop(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
        assert s_size(s) == len(l)
        for i in range(len(l)):
            s_pop(s)
            assert s_size(s) == len(l) - 1 - i

    def test_s_is_empty_push(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
            assert not s_is_empty(s)

    def test_s_is_empty_pop(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
        assert not s_is_empty(s)
        for _ in range(len(l) - 1):
            s_pop(s)
            assert not s_is_empty(s)
        s_pop(s)
        assert s_is_empty(s)

    def test_s_top_push(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
            assert s_top(s) == e

    def test_s_top_pop(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
            assert s_top(s) == e
        for e in reversed(l):
            assert s_top(s) == e
            s_pop(s)

    def test_s_str_empty(self, dsize):
        s = s_new(dsize)
        assert s_str(s) == "[]"

    def test_s_str(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for i, e in enumerate(l):
            s_push(s, e)
        assert s_str(s) == str(l)

    def test_s_pop_fails_empty(self, dsize):
        s = s_new(dsize)
        pytest.raises(IndexError, s_pop, s)

    def test_s_top_fails_empty(self, dsize):
        s = s_new(dsize)
        pytest.raises(IndexError, s_top, s)

    def test_s_pop_fails_out_of_bounds(self, input_list, dsize):
        l = input_list  # alias
        s = s_new(len(l) + dsize)
        for e in l:
            s_push(s, e)
        for _ in range(len(l)):
            s_pop(s)
        pytest.raises(IndexError, s_pop, s)
