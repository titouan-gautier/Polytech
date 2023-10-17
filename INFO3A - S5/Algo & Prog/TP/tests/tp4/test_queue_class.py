import pytest
import importlib

from tests.setup import QUEUE_STRUCT_NAMES, TP_CLASS
from tests.conftest import FakeStruct

try:
    queue_module = importlib.import_module(TP_CLASS['queue_deque']['module'])     # may raise ImportError

    for name in QUEUE_STRUCT_NAMES:
        if not hasattr(queue_module, name):
            setattr(queue_module, name, FakeStruct)

        # it is then "safe" to expose the student's code
        globals()[name] = getattr(queue_module, name)

        # aliases for the student's code
        if hasattr(name, 'str'):
            setattr(name, '__str__', lambda self: self.str())
        if hasattr(name, 'size'):
            setattr(name, '__len__', lambda self: self.len())

except ImportError:
    pass

ROLLING_QUEUE = 7  #


@pytest.mark.key("e8q2")
class TestQueue:

    def test_q_new_default(self):
        q = Queue()
        assert isinstance(q, Queue)

    def test_q_new_custom_size(self, dsize):
        q = Queue(dsize)
        assert isinstance(q, Queue)

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
        q = Queue(len(l))
        for e in l:
            q.enqueue(e)
        for i in range(len(l) - 1):
            q.dequeue()
            assert not q.is_empty()
        q.dequeue()
        assert q.is_empty()

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

    def test_is_full_enqueue_dequeue(self, input_list_with_null, dsize):
        l = input_list_with_null or []
        q = Queue(len(l) + dsize)
        for _ in range(ROLLING_QUEUE):
            for e in l:
                q.enqueue(e)
                assert not q.is_full()
            for i in range(len(l) - 1):
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
