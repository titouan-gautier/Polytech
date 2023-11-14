from __future__ import annotations

from math import pow
from hachage import encodage


class Item:
    cle: str | None
    valeur: int | None

    def __init__(self, k: str | None = None, v: int | None = None):
        self.cle = k
        self.valeur = v


class HashMap:
    max_size: int
    size: int
    table = list[Item]

    def __init__(self, size):
        self.size = 0
        self.max_size = size
        self.table = [Item()] * size

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get(self, k: str) -> int:
        i = 0
        index = self.H(k, i)

        while self.table[index] is None:
            i += 1
            index = self.H(k, i)

        return self.table[index].valeur

    def h(self, k: str):
        return encodage(k) % self.max_size

    def H(self, k: str, i: int) -> int:
        return round(self.h(k) + pow(i, 2) / 2 + i / 2)

    def put(self, k: str, v: int):
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
            if i is not None :
                if i.cle is not None :
                    res += i.cle + ": " + str(i.valeur) + ", "

        res = res[:len(res)-2]
        res += "}"

        return res


if __name__ == '__main__':
    hm = HashMap(10)
    hm.put("aaa", 5)
    hm.put("ouiiiiii",1)
    hm.put("Titouan",12)
    print(hm.get("aaa"))
    hm.delete("aaa")
    print(hm)
