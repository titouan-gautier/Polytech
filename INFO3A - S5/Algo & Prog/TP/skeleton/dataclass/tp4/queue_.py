from dataclasses import dataclass


@dataclass
class Queue:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("Queue class not implemented yet")


def q_new(n: int = 10) -> Queue:
    raise NotImplementedError("Queue q_new function not implemented yet")


def q_size(q: Queue) -> int:
    raise NotImplementedError("Queue q_size function not implemented yet")


def q_is_empty(q: Queue) -> bool:
    raise NotImplementedError("Queue q_is_empty function not implemented yet")


def q_is_full(q: Queue) -> bool:
    raise NotImplementedError("Queue q_is_full function not implemented yet")


def q_str(q: Queue) -> str:
    raise NotImplementedError("Queue q_str function not implemented yet")


def q_enqueue(q: Queue, item: int) -> Queue:
    raise NotImplementedError("Queue q_enqueue function not implemented yet")


def q_dequeue(q: Queue) -> Queue:
    raise NotImplementedError("Queue q_dequeue function not implemented yet")


def q_rear(q: Queue) -> int:
    raise NotImplementedError("Queue q_rear function not implemented yet")


def q_front(q: Queue) -> int:
    raise NotImplementedError("Queue q_front function not implemented yet")