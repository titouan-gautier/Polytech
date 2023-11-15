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
        hm = hm_new()
        assert isinstance(hm, HashMap)

    def test_hashmap_is_empty(self):
        hm = hm_new()
        assert hm_is_empty(hm) is True

    def test_hashmap_size_empty(self):
        hm = hm_new()
        assert hm_size(hm) == 0

    def test_hashmap_put(self, dsize, char_list):
        hm = hm_new()
        for i, letter in enumerate(char_list):
            hm_put(hm, letter, dsize)
            assert hm_size(hm) == i + 1
        assert hm_size(hm) == len(char_list)

    def test_hashmap_get(self, dsize, char_list):
        hm = hm_new()
        for i, letter in enumerate(char_list):
            hm_put(hm, letter, dsize)
        for i, letter in enumerate(char_list):
            assert hm_get(hm, letter) == dsize
        assert hm_size(hm) == len(char_list)

    def test_hashmap_delete(self, dsize, char_list):
        hm = hm_new()
        for i, letter in enumerate(char_list):
            hm_put(hm, letter, dsize)
        for i, letter in enumerate(char_list):
            hm_delete(hm, letter)
            assert hm_size(hm) == len(char_list) - i - 1
        assert hm_size(hm) == 0

    def test_hashmap_str(self, dsize, char_list):
        hm = hm_new()
        for i, letter in enumerate(char_list):
            hm_put(hm, letter, dsize)
        for i, letter in enumerate(char_list):
            assert f"'{letter}': {dsize}" in hm_str(hm)
