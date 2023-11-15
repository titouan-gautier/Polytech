from __future__ import annotations

from math import pow
from tp6.hachage import encodage


class Item:

    def __init__(self, k: str | None = None, v: int | None = None):
        self.cle: str = k
        self.valeur: int = v


class HashMap:

    def __init__(self):
        self.size: int = 0
        self.max_size: int = round(pow(2,20))
        self.table: list[Item] = [Item()] * self.max_size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self, k: str) -> int:
        i = 0
        index = self.H(k, i)

        while self.table[index] is None:
            i += 1
            index = self.H(k, i)

        return self.table[index].valeur

    def get_key(self, k: str) -> str:
        i = 0
        index = self.H(k, i)

        while self.table[index] is None:
            i += 1
            index = self.H(k, i)

        return self.table[index].cle

    def h(self, k: str):
        return encodage(k) % self.max_size

    def H(self, k: str, i: int) -> int:
        return round(self.h(k) + pow(i, 2) / 2 + i / 2)

    def put(self, k: str, v: int | None = None):
        i = 0
        index = self.H(k, i)

        while self.table[index] == Item() or self.table[index] is None:
            i += 1
            index = self.H(k, i)

        self.table[index] = (Item(k, v))

        self.size += 1

        return self

    def delete(self, k: str):
        i = 0
        index = self.H(k, i)

        if self.table[index].cle == k:
            self.table[index] = None

        while self.table[index] is not None:
            i += 1
            index = self.H(k, i)

            if self.table[index].cle == k:
                self.table[index] = None

        self.size -= 1
        return self

    def __str__(self):
        res = "{"
        for i in self.table:
            if i is not None:
                if i.cle is not None:
                    res += "'" + i.cle + "'" + ": " + str(i.valeur) + ", "

        res = res[:len(res) - 2]
        res += "}"

        return res


if __name__ == '__main__':
    hm = HashMap()
    hm.put("a", 1)
    print(hm)
