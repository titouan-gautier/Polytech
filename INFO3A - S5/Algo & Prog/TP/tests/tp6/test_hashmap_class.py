import pytest
from tests.conftest import import_stuff

import_stuff('hashmap')

# beurk!
from tests.conftest import *


@pytest.mark.key("e2q2")
class TestHashMap:
    def test_hashmap_struct(self):
        try:
            HashMap()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_hashmap_item_struct(self):
        try:
            Item()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_hashmap_new(self):
        hm = HashMap()
        assert isinstance(hm, HashMap)

    def test_hashmap_is_empty(self):
        hm = HashMap()
        assert hm.is_empty() is True

    def test_hashmap_size_empty(self):
        hm = HashMap()
        print("test")
        print(hasattr("HashMap", "size"))
        assert hm.__len__() == 0

    def test_hashmap_put(self, dsize, char_list):
        hm = HashMap()
        for i, letter in enumerate(char_list):
            hm.__setitem__(letter, dsize)
            assert hm.__len__() == i + 1
        assert hm.__len__() == len(char_list)

    def test_hashmap_get(self, dsize, char_list):
        hm = HashMap()
        for i, letter in enumerate(char_list):
            hm.__setitem__(letter, dsize)
        for i, letter in enumerate(char_list):
            assert hm.__getitem__(letter) == dsize
        assert hm.__len__() == len(char_list)

    def test_hashmap_delete(self, dsize, char_list):
        hm = HashMap()
        for i, letter in enumerate(char_list):
            hm.__setitem__(letter, dsize)
        for i, letter in enumerate(char_list):
            hm.delete(letter)
            assert hm.__len__() == len(char_list) - i - 1
        assert hm.__len__() == 0

    def test_hashmap_str(self, dsize, char_list):
        hm = HashMap()
        for i, letter in enumerate(char_list):
            hm.__setitem__(letter, dsize)
        for i, letter in enumerate(char_list):
            assert f"'{letter}': {dsize}" in hm.__str__()
