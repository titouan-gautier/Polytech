from __future__ import annotations
from typing import Iterator


class Cell:
    prev: Cell
    val: int
    next: Cell

    def __init__(self, data: int | None, next: Cell | None = None, prev: Cell | None = None):
        self.val = data
        self.next = next
        self.prev = prev


class LinkedList:
    sentinelle: Cell
    size: int

    def __init__(self, l: list[int] | None = None):
        self.sentinelle = Cell(None)
        self.size = 0

        if l is not None:
            for i in l:
                self.append(i)

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def head(self) -> Cell:
        if self.is_empty():
            raise IndexError()

        return self.sentinelle.next

    def tail(self) -> Cell:
        if self.is_empty():
            raise IndexError()

        res = self.sentinelle

        for i in range(self.size):
            res = res.next

        return res

    def __getitem__(self, idx: Cell) -> int:

        res = self.sentinelle

        while res is not idx:
            if res is self.tail():
                raise IndexError()
            res = res.next

        return res.val

    def __setitem__(self, idx: Cell, item: int) -> LinkedList:

        res = self.sentinelle

        while res is not idx:
            if res is self.tail():
                raise IndexError()
            res = res.next

        res.val = item

        return self

    def insert(self, item: int, neighbor: Cell | None = None, after: bool = True) -> LinkedList:

        if self.size == 0:

            new_cell = Cell(item, self.sentinelle, self.sentinelle)

            self.sentinelle.next = new_cell
            self.sentinelle.prev = new_cell

        else:

            if neighbor is None:

                if after:

                    new_cell = Cell(item, self.head(), self.sentinelle)

                    self.head().prev = new_cell
                    self.sentinelle.next = new_cell

                else:

                    new_cell = Cell(item, self.sentinelle, self.tail())

                    self.tail().next = new_cell
                    self.sentinelle.prev = new_cell

            else:

                if after:

                    new_cell = Cell(item, neighbor.next, neighbor)

                    neighbor.next.prev = new_cell
                    neighbor.next = new_cell

                else:

                    new_cell = Cell(item, neighbor, neighbor.prev)

                    neighbor.prev.next = new_cell
                    neighbor.prev = new_cell

        self.size += 1

        return self

    def __iter__(self):

        return self.__next__()

    def __next__(self):

        if self.is_empty():
            return

        res = self.head()

        while res != self.tail():
            yield res
            res = res.next

        yield res

    def __reversed__(self):

        if self.is_empty():
            return

        res = self.tail()

        while res != self.head():
            yield res
            res = res.prev

        yield res

    def __str__(self) -> str:

        res = "["

        if self.is_empty():
            res += "]"
            return res

        for i in self:
            res += f"{i.val}, "

        res = res[:len(res) - 2]
        res += "]"

        return res

    def lookup(self, item: int) -> Cell | None:

        for i in self:
            if i.val == item:
                return i

        return None

    def cell_at(self, i: int) -> Cell:
        if self.is_empty():
            raise IndexError

        count = 0

        for c in self:
            if count == i :
                return c
            count += 1


        raise IndexError

    def append(self, item: int) -> LinkedList:
        return self.insert(item, None, False)

    def prepend(self, item: int) -> LinkedList:
        return self.insert(item, None, True)

    def remove(self, cell: Cell) -> LinkedList:

        for i in self :
            if i is cell :
                prev_cell = cell.prev
                next_cell = cell.next

                prev_cell.next = next_cell
                next_cell.prev = prev_cell

                self.size -= 1

        return self

    def extend(self, other: LinkedList) -> LinkedList:

        for i in other :
            self.append(i.val)

        return self

