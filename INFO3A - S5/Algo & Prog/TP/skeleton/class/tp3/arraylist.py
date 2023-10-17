from __future__ import annotations


class ArrayList:

    def __init__(self, m: int = 10, l: list[int] | None = None):
        raise NotImplementedError("ArrayList class not implemented yet")

    def __len__(self) -> int:
        raise NotImplementedError("ArrayList __len__ method not implemented yet")

    def is_empty(self) -> bool:
        raise NotImplementedError("ArrayList is_empty method not implemented yet")

    def __str__(self) -> str:
        raise NotImplementedError("ArrayList __str__ method not implemented yet")

    def __getitem__(self, i: int) -> int:
        raise NotImplementedError("ArrayList __getitem__ method not implemented yet")

    def __setitem__(self, i: int, item: int) -> ArrayList:
        raise NotImplementedError("ArrayList __setitem__ method not implemented yet")

    def lookup(self, item: int) -> int | None:
        raise NotImplementedError("ArrayList lookup method not implemented yet")

    def remove(self, i: int) -> ArrayList:
        raise NotImplementedError("ArrayList remove method not implemented yet")

    def insert(self, i: int, item: int) -> ArrayList:
        raise NotImplementedError("ArrayList insert method not implemented yet")

    def prepend(self, item: int) -> ArrayList:
        raise NotImplementedError("ArrayList prepend method not implemented yet")

    def append(self, item: int) -> ArrayList:
        raise NotImplementedError("ArrayList append method not implemented yet")

    def extend(self, tab: 'ArrayList') -> ArrayList:
        raise NotImplementedError("ArrayList extend method not implemented yet")
