from __future__ import annotations
from tp4.llist import LinkedList


class Deque(LinkedList):

    def is_empty(self) -> bool:
        return self.size == 0

    def front(self) -> int:
        return self.head().val

    def rear(self) -> int:
        return self.tail().val

    def push_front(self, item: int) -> Deque:
        return self.prepend(item)

    def push_rear(self, item: int) -> Deque:
        return self.append(item)

    def pop_front(self) -> Deque:
        return self.remove(self.head())

    def pop_rear(self) -> Deque:
        return self.remove(self.tail())