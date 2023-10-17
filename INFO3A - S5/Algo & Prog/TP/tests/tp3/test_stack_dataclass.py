import pytest

try:
    from tp3.stack import (Stack,
                           s_new,
                           s_size,
                           s_is_empty,
                           s_str,
                           s_push,
                           s_pop,
                           s_top,
                           )
except ImportError:
    if 'Stack' not in globals():
        from dataclasses import dataclass

        @dataclass
        class Stack:
            def __post_init__(self):
                raise NotImplementedError("Stack class not found")
    if 's_new' not in globals():
        def s_new(n=10):
            raise NotImplementedError("s_new function not found")
    if 's_size' not in globals():
        def s_size(s):
            raise NotImplementedError("s_size function not found")
    if 's_is_empty' not in globals():
        def s_is_empty(s):
            raise NotImplementedError("s_is_empty function not found")
    if 's_str' not in globals():
        def s_str(s):
            raise NotImplementedError("s_str function not found")
    if 's_push' not in globals():
        def s_push(s, item):
            raise NotImplementedError("s_push function not found")
    if 's_pop' not in globals():
        def s_pop(s):
            raise NotImplementedError("s_pop function not found")
    if 's_top' not in globals():
        def s_top(s):
            raise NotImplementedError("s_top function not found")


@pytest.mark.key("e9q2")
class TestStack:

    def test_s_new_default(self):
        s = s_new()
        assert isinstance(s, Stack)

    def test_s_new_custom_size(self, dsize):
        s = s_new(dsize)
        assert isinstance(s, Stack)

    def test_s_new_fails_custom_size(self, dsize):
        pytest.raises(AssertionError, s_new, -1 - dsize)

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

    def test_s_push_fails_overflow(self, input_list, dsize):
        l = input_list  # alias
        max_size = max(0, len(l) - 1 - dsize)
        s = s_new(max_size)
        for i in range(max_size):
            s_push(s, l[i])
        pytest.raises(OverflowError, s_push, s, l[max_size])

    def test_s_pop_fails_out_of_bounds_empty(self, dsize):
        s = s_new(dsize)
        pytest.raises(IndexError, s_pop, s)

    def test_s_top_fails_out_of_bounds_empty(self, dsize):
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
