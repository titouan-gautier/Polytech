import pytest

try:
    from tp3.stack import Stack
except ImportError:
    if 'Stack' not in globals():
        class Stack:
            def __init__(self):
                raise NotImplementedError("Stack class not found")

methods = dir(Stack)

if 'str' not in methods:
    def str(self):
        return self.__str__()

    Stack.str = str

if 'size' not in methods:
    def size(self):
        return self.__len__()

    Stack.size = size


@pytest.mark.key("e9q2")
class TestStack:

    def test_s_new_default(self):
        s = Stack()
        assert isinstance(s, Stack)

    def test_s_new_custom_size(self, dsize):
        s = Stack(dsize)
        assert isinstance(s, Stack)

    def test_s_new_fails_custom_size(self, dsize):
        pytest.raises(AssertionError, Stack, -1 - dsize)

    def test_s_size_empty_stack(self, dsize):
        s = Stack(dsize)
        assert s.size() == 0

    def test_s_is_empty(self, dsize):
        s = Stack(dsize)
        assert s.is_empty()

    def test_s_size_push(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for i, e in enumerate(l):
            s.push(e)
            assert s.size() == i + 1

    def test_s_size_pop(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for e in l:
            s.push(e)
        assert s.size() == len(l)
        for i in range(len(l)):
            s.pop()
            assert s.size() == len(l) - 1 - i

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
        assert s.str() == "[]"

    def test_s_str(self, input_list, dsize):
        l = input_list  # alias
        s = Stack(len(l) + dsize)
        for i, e in enumerate(l):
            s.push(e)
        assert s.str() == str(l)

    def test_s_push_fails_overflow(self, input_list, dsize):
        l = input_list  # alias
        max_size = max(0, len(l) - 1 - dsize)
        s = Stack(max_size)
        for i in range(max_size):
            s.push(l[i])
        pytest.raises(OverflowError, s.push, l[max_size])

    def test_s_pop_fails_out_of_bounds_empty(self, dsize):
        s = Stack(dsize)
        pytest.raises(IndexError, s.pop)

    def test_s_top_fails_out_of_bounds_empty(self, dsize):
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
