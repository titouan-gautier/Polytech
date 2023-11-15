from tp6.hashmap import HashMap, Item


class HashSet:
    def __init__(self,char_list):
        self.max_size: int = pow(2, 20)
        self.size = 0
        self.data: HashMap = HashMap()

        for i in char_list:
            self.data.put(i)
            self.size += 1

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        res = "{"
        for i in self.data.table:
            if i is not None:
                if i.cle is not None:
                    res += i.cle + ", "

        res = res[:len(res) - 2]
        res += "}"

        return res

    def member(self, e: str):
        return self.data[e] == e

    def insert(self, e: str):
        self.data.put(e)
        self.size += 1
        return self

    def delete(self, e: str):
        self.data.delete(e)
        self.size -= 1
        return self


if __name__ == '__main__':
    hs = HashSet()
    hs.insert('Titouan')
    hs.insert('Gautier')
    print(hs)
    print(hs.member('Titouan'))
    print(hs.member('Elias'))
    hs.delete('Titouan')
    print(hs)
