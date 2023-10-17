from dataclasses import dataclass


@dataclass
class Stack:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("Stack class not implemented yet")


def s_new(n: int = 10) -> Stack:
    raise NotImplementedError("Stack s_new function not implemented yet")


def s_size(s: Stack) -> int:
    raise NotImplementedError("Stack s_size function not implemented yet")


def s_is_empty(s: Stack) -> bool:
    raise NotImplementedError("Stack s_is_empty function not implemented yet")


def s_str(s: Stack) -> str:
    raise NotImplementedError("Stack s_str function not implemented yet")


def s_push(s: Stack, item: int) -> Stack:
    raise NotImplementedError("Stack s_push function not implemented yet")


def s_pop(s: Stack) -> Stack:
    raise NotImplementedError("Stack s_pop function not implemented yet")


def s_top(s: Stack) -> int:
    raise NotImplementedError("Stack s_top function not implemented yet")
