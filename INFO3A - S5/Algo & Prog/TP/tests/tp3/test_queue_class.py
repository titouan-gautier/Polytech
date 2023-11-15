import pytest
from tests.conftest import import_stuff

import_stuff('queue')

# beurk!
from tests.conftest import *

ROLLING_QUEUE = 7  #


@pytest.mark.key("e11q1")
class TestQueue:

    def test_q_new_default(self):
        q = Queue()
        assert isinstance(q, Queue)

    def test_q_new_custom_size(self, dsize):
        q = Queue(dsize)
        assert isinstance(q, Queue)

    def test_q_new_fails_size(self, dsize):
        pytest.raises(AssertionError, Queue, -1 - dsize)

    def test_q_size_empty_queue(self, dsize):
        q = Queue(dsize)
        assert q.__len__() == 0

    def test_q_is_empty(self, dsize):
        q = Queue(dsize)
        assert q.is_empty()

    def test_q_size_enqueue(self, input_list):
        l = input_list  # alias
        q = Queue(len(l))
        for i, e in enumerate(l):
            q.enqueue(e)
            assert q.__len__() == i + 1

    def test_q_is_empty_enqueue(self, input_list):
        l = input_list
        q = Queue(len(l))
        for e in l:
            q.enqueue(e)
            assert not q.is_empty()

    def test_q_size_dequeue(self, input_list):
        l = input_list
        q = Queue(len(l))
        for e in l:
            q.enqueue(e)
        for i in range(len(l)):
            q.dequeue()
            assert q.__len__() == len(l) - 1 - i

    def test_q_is_empty_dequeue(self, input_list):
        l = input_list
        queue = Queue(len(l))
        for e in l:
            queue.enqueue(e)
        for i in range(len(l) - 1):
            queue.dequeue()
            assert not queue.is_empty()
        queue.dequeue()
        assert queue.is_empty()

    def test_q_size_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for i, e in enumerate(l):
                q.enqueue(e)
                assert q.__len__() == i + 1
            for i in range(len(l)):
                q.dequeue()
                assert q.__len__() == len(l) - 1 - i

    def test_is_empty_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
                assert not q.is_empty()
            for i in range(len(l) - 1):
                q.dequeue()
                assert not q.is_empty()
            q.dequeue()
            assert q.is_empty()

    def test_q_is_full(self, dsize):
        q = Queue(dsize)
        assert q.is_full() if dsize == 0 else not q.is_full()

    def test_q_is_full_enqueue(self, input_list):
        l = input_list
        q = Queue(len(l))
        for e in l:
            assert not q.is_full()
            q.enqueue(e)
        assert q.is_full()

    def test_is_full_enqueue_dequeue(self, input_list):
        l = input_list
        q = Queue(len(l))
        for _ in range(ROLLING_QUEUE):
            for e in l:
                assert not q.is_full()
                q.enqueue(e)
            assert q.is_full()
            for _ in range(len(l)):
                q.dequeue()
                assert not q.is_full()

    def test_q_str_empty_queue(self, dsize):
        q = Queue(dsize)
        assert q.__str__() == "[]"

    def test_q_str(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for e in l:
            q.enqueue(e)
        assert q.__str__() == str(l)

    def test_q_str_enqueue_dequeue(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
            assert q.__str__() == str(l)
            for _ in range(len(l)):
                q.dequeue()
            assert q.__str__() == "[]"

    def test_q_enqueue_dequeue_fails_overflow(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
            for _ in range(len(l)):
                q.dequeue()
        for _ in range(len(l) + dsize):
            q.enqueue(42)
        pytest.raises(OverflowError, q.enqueue, item=42)

    def test_q_dequeue_enqueue_fails_empty(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
            for _ in range(len(l)):
                q.dequeue()
        pytest.raises(IndexError, q.dequeue)

    def test_q_rear(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
                assert q.rear() == e
            for _ in range(len(l)):
                assert q.rear() == l[-1]
                q.dequeue()

    def test_q_front(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
                assert q.front() == l[0]
            for e in l:
                assert q.front() == e
                q.dequeue()

    def test_q_rear_fails_empty_queue(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
            for e in l:
                q.dequeue()
        pytest.raises(IndexError, q.rear)

    def test_q_front_fails_empty_queue(self, input_list, dsize):
        l = input_list
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
            for e in l:
                q.dequeue()
        pytest.raises(IndexError, q.front)
