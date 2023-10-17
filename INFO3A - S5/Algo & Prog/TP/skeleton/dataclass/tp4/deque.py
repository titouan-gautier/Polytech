from dataclasses import dataclass


@dataclass
class Deque:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("Deque class not implemented yet")


def d_new() -> Deque:
    raise NotImplementedError("Deque d_new function not implemented yet")


def d_is_empty(d: Deque) -> bool:
    raise NotImplementedError("Deque d_is_empty function not implemented yet")


def d_len(d: Deque) -> int:
    raise NotImplementedError("Deque d_len function not implemented yet")


def d_str(d: Deque) -> str:
    raise NotImplementedError("Deque d_str function not implemented yet")


def d_front(d: Deque) -> int:
    raise NotImplementedError("Deque d_front function not implemented yet")


def d_rear(d: Deque) -> int:
    raise NotImplementedError("Deque d_rear function not implemented yet")


def d_push_front(d: Deque, item: int) -> Deque:
    raise NotImplementedError("Deque d_push_front function not implemented yet")


def d_push_rear(d: Deque, item: int) -> Deque:
    raise NotImplementedError("Deque d_push_rear function not implemented yet")


def d_pop_front(d: Deque) -> Deque:
    raise NotImplementedError("Deque d_pop_front function not implemented yet")


def d_pop_rear(d: Deque) -> Deque:
    raise NotImplementedError("Deque d_pop_rear function not implemented yet")
