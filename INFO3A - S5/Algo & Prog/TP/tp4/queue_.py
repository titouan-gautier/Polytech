from __future__ import annotations


class Queue:

    def __init__(self, n: int = 10):
        raise NotImplementedError("Queue class not implemented yet")

    def size(self) -> int:
        raise NotImplementedError("Queue size method not implemented yet")

    def is_empty(self) -> bool:
        raise NotImplementedError("Queue is_empty method not implemented yet")

    def is_full(self) -> bool:
        raise NotImplementedError("Queue is_full method not implemented yet")

    def __str__(self) -> str:
        raise NotImplementedError("Queue __str__ method not implemented yet")

    def enqueue(self, item: int) -> Queue:
        raise NotImplementedError("Queue enqueue method not implemented yet")

    def dequeue(self) -> Queue:
        raise NotImplementedError("Queue dequeue method not implemented yet")

    def rear(self) -> int:
        raise NotImplementedError("Queue rear method not implemented yet")

    def front(self) -> int:
        raise NotImplementedError("Queue front method not implemented yet")
