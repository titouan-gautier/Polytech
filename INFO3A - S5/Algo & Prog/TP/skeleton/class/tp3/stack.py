from __future__ import annotations


class Stack:

    def __init__(self, n: int = 10):
        raise NotImplementedError("Stack class not implemented yet")

    def size(self) -> int:
        raise NotImplementedError("Stack size method not implemented yet")

    def is_empty(self) -> bool:
        raise NotImplementedError("Stack is_empty method not implemented yet")

    def __str__(self) -> str:
        raise NotImplementedError("Stack __str__ method not implemented yet")

    def push(self, item: int) -> Stack:
        raise NotImplementedError("Stack push method not implemented yet")

    def pop(self) -> Stack:
        raise NotImplementedError("Stack pop method not implemented yet")

    def top(self) -> int:
        raise NotImplementedError("Stack top method not implemented yet")
