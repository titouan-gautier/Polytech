import pytest

try:
    from tp3.queue_ import (Queue,
                            q_new,
                            q_size,
                            q_is_empty,
                            q_is_full,
                            q_str,
                            q_enqueue,
                            q_dequeue,
                            q_rear,
                            q_front,
                            )
except ImportError:
    if 'Queue' not in globals():
        from dataclasses import dataclass

        @dataclass
        class Queue:
            def __post_init__(self):
                raise NotImplementedError("Queue class not found")
    if 'q_new' not in globals():
        def q_new(n=10):
            raise NotImplementedError("q_new function not found")
    if 'q_size' not in globals():
        def q_size(q):
            raise NotImplementedError("q_size function not found")
    if 'q_is_empty' not in globals():
        def q_is_empty(q):
            raise NotImplementedError("q_is_empty function not found")
    if 'q_is_full' not in globals():
        def q_is_full(q):
            raise NotImplementedError("q_is_full function not found")
    if 'q_str' not in globals():
        def q_str(q):
            raise NotImplementedError("q_str function not found")
    if 'q_enqueue' not in globals():
        def q_enqueue(q, item):
            raise NotImplementedError("q_enqueue function not found")
    if 'q_dequeue' not in globals():
        def q_dequeue(q):
            raise NotImplementedError("q_dequeue function not found")
    if 'q_rear' not in globals():
        def q_rear(q):
            raise NotImplementedError("q_rear function not found")
    if 'q_front' not in globals():
        def q_front(q):
            raise NotImplementedError("q_front function not found")


ROLLING_QUEUE = 7  #

@pytest.mark.key("e11q1")
class TestQueue:

    def test_q_new_default(self):
        q = q_new()
        assert isinstance(q, Queue)

    def test_q_new_custom_size(self, dsize):
        q = q_new(dsize)
        assert isinstance(q, Queue)

    def test_q_new_fails_size(self, dsize):
        pytest.raises(AssertionError, q_new, -1 - dsize)

    def test_q_size_empty_queue(self, dsize):
        q = q_new(dsize)
        assert q_size(q) == 0

    def test_q_is_empty(self, dsize):
        q = q_new(dsize)
        assert q_is_empty(q)

    def test_q_size_enqueue(self, input_list):
        l = input_list  # alias
        q = q_new(len(l))
        for i, e in enumerate(l):
            q_enqueue(q, e)
            assert q_size(q) == i + 1

    def test_q_is_empty_enqueue(self, input_list):
        l = input_list
        q = q_new(len(l))
        for e in l:
            q_enqueue(q, e)
            assert not q_is_empty(q)

    def test_q_size_dequeue(self, input_list):
        l = input_list
        q = q_new(len(l))
        for e in l:
            q_enqueue(q, e)
        for i in range(len(l)):
            q_dequeue(q)
            assert q_size(q) == len(l) - 1 - i

    def test_q_is_empty_dequeue(self, input_list):
        l = input_list
        queue = q_new(len(l))
        for e in l:
            q_enqueue(queue, e)
        for i in range(len(l) - 1):
            q_dequeue(queue)
            assert not q_is_empty(queue)
        q_dequeue(queue)
        assert q_is_empty(queue)

    def test_q_size_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for i, e in enumerate(l):
                q_enqueue(q, e)
                assert q_size(q) == i + 1
            for i in range(len(l)):
                q_dequeue(q)
                assert q_size(q) == len(l) - 1 - i

    def test_is_empty_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
                assert not q_is_empty(q)
            for i in range(len(l) - 1):
                q_dequeue(q)
                assert not q_is_empty(q)
            q_dequeue(q)
            assert q_is_empty(q)

    def test_q_is_full(self, dsize):
        q = q_new(dsize)
        assert q_is_full(q) if dsize == 0 else not q_is_full(q)

    def test_q_is_full_enqueue(self, input_list):
        l = input_list
        q = q_new(len(l))
        for e in l:
            assert not q_is_full(q)
            q_enqueue(q, e)
        assert q_is_full(q)

    def test_is_full_enqueue_dequeue(self, input_list):
        l = input_list
        q = q_new(len(l))
        for _ in range(ROLLING_QUEUE):
            for e in l:
                assert not q_is_full(q)
                q_enqueue(q, e)
            assert q_is_full(q)
            for _ in range(len(l)):
                q_dequeue(q)
                assert not q_is_full(q)

    def test_q_str_empty_queue(self, dsize):
        q = q_new(dsize)
        assert q_str(q) == "[]"

    def test_q_str(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for e in l:
            q_enqueue(q, e)
        assert q_str(q) == str(l)

    def test_q_str_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
            assert q_str(q) == str(l)
            for _ in range(len(l)):
                q_dequeue(q)
            assert q_str(q) == "[]"

    def test_q_enqueue_dequeue_fails_overflow(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
            for _ in range(len(l)):
                q_dequeue(q)
        for _ in range(len(l) + dsize):
            q_enqueue(q, 42)
        pytest.raises(OverflowError, q_enqueue, q, item=42)

    def test_q_dequeue_enqueue_fails_empty(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
            for _ in range(len(l)):
                q_dequeue(q)
        pytest.raises(IndexError, q_dequeue, q)

    def test_q_rear(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
                assert q_rear(q) == e
            for _ in range(len(l)):
                assert q_rear(q) == l[-1]
                q_dequeue(q)

    def test_q_front(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
                assert q_front(q) == l[0]
            for e in l:
                assert q_front(q) == e
                q_dequeue(q)

    def test_q_rear_fails_empty_queue(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
            for e in l:
                q_dequeue(q)
        pytest.raises(IndexError, q_rear, q)

    def test_q_front_fails_empty_queue(self, input_list, dsize):
        l = input_list
        q = q_new(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q_enqueue(q, e)
            for e in l:
                q_dequeue(q)
        pytest.raises(IndexError, q_front, q)
