from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Cell:
    # TODO: add your attributes here
    # TODO: delete __post_init__ method
    def __post_init__(self):
        raise NotImplementedError("Cell class not implemented yet")


@dataclass
class LinkedList:
    def __post_init__(self):
        raise NotImplementedError("LinkedList class not implemented yet")


def ll_new(initial_l: list[int] | None = None) -> LinkedList:
    raise NotImplementedError("LinkedList ll_new function not implemented yet")


def ll_is_empty(l: LinkedList) -> bool:
    raise NotImplementedError("LinkedList ll_is_empty function not implemented yet")


def ll_len(l: LinkedList) -> int:
    raise NotImplementedError("LinkedList ll_len function not implemented yet")


def ll_head(l: LinkedList) -> Cell:
    raise NotImplementedError("LinkedList ll_head function not implemented yet")


def ll_tail(l: LinkedList) -> Cell:
    raise NotImplementedError("LinkedList ll_tail function not implemented yet")


def ll_get(l: LinkedList, idx: XXX) -> int:
    raise NotImplementedError("LinkedList ll_get function not implemented yet")


def ll_set(l: LinkedList, idx: XXX, item: int) -> LinkedList:
    raise NotImplementedError("LinkedList ll_set function not implemented yet")


def ll_iter_cells(l: LinkedList) -> Iterator[Cell]:
    raise NotImplementedError("LinkedList ll_iter_cells function not implemented yet")


def ll_reversed_iter_cells(l: LinkedList) -> Iterator[Cell]:
    raise NotImplementedError("LinkedList ll_iter_cells function not implemented yet")


def ll_insert(l: LinkedList, item: int, neighbor: Cell, after: bool = True) -> LinkedList:
    raise NotImplementedError("LinkedList ll_insert function not implemented yet")


def ll_append(l: LinkedList, item: int) -> LinkedList:
    raise NotImplementedError("LinkedList ll_append function not implemented yet")


def ll_prepend(l: LinkedList, item: int) -> LinkedList:
    raise NotImplementedError("LinkedList ll_prepend function not implemented yet")


def ll_str(l: LinkedList) -> str:
    raise NotImplementedError("LinkedList ll_str function not implemented yet")


def ll_lookup(l: LinkedList, item: int) -> Cell:
    raise NotImplementedError("LinkedList ll_lookup function not implemented yet")


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    raise NotImplementedError("LinkedList ll_cell_at function not implemented yet")


def ll_remove(l: LinkedList, cell: Cell) -> LinkedList:
    raise NotImplementedError("LinkedList ll_remove function not implemented yet")


def ll_extend(l1: LinkedList, l2: LinkedList) -> LinkedList:
    raise NotImplementedError("LinkedList ll_extend function not implemented yet")
