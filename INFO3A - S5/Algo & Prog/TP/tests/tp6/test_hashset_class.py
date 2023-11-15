import pytest
from tests.conftest import import_stuff

import_stuff('hashset')

# beurk!
from tests.conftest import *


@pytest.mark.key("e4q1")
class TestHashSet:

    def test_hashset_struct(self):
        try:
            HashSet()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_hashset_new(self, char_list):
        hs = HashSet(char_list)
        assert isinstance(hs, HashSet)

    def test_hashset_is_empty(self, char_list):
        hs = HashSet(char_list)
        if len(char_list) == 0:
            assert hs.is_empty() is True
        else:
            assert hs.is_empty() is False

    def test_hashset_size(self, char_list):
        hs = HashSet(char_list)
        assert hs.__len__() == len(char_list)

    def test_hashset_member(self, char_list):
        hs = HashSet(char_list)
        for letter in char_list:
            assert hs.member(letter) is True
        assert hs.member('Z') is False

    def test_hashset_iterate(self, char_list):
        hs = HashSet(char_list)
        for letter in hs.iterate():
            assert letter in char_list

    def test_hashset_insert(self, char_list):
        hs = HashSet()
        for letter in char_list:
            hs.insert(letter)
        for letter in char_list:
            assert hs.member(letter) is True

    def test_hashset_delete(self, char_list):
        hs = HashSet(char_list)
        for letter in char_list:
            hs.delete(letter)
        assert hs.__len__() == 0

    def test_hashset_union(self, char_list, char_list2):
        hs = HashSet(char_list)
        hs2 = HashSet(char_list2)
        hsboth = hs.union(hs2)
        for letter in char_list:
            assert hsboth.member(letter) is True
        for letter in char_list2:
            assert hsboth.member(letter) is True

    def test_hashset_intersection(self, char_list, char_list2):
        hs = HashSet(char_list)
        hs2 = HashSet(char_list2)
        hsboth = hs.intersection(hs2)
        for letter in char_list:
            if letter in char_list2:
                assert hsboth.member(letter) is True
            else:
                assert hsboth.member(letter) is False

    def test_hashset_difference(self, char_list, char_list2):
        hs = HashSet(char_list)
        hs2 = HashSet(char_list2)
        hsboth = hs.difference(hs2)
        for letter in char_list:
            if letter in char_list2:
                assert hsboth.member(letter) is False
            else:
                assert hsboth.member(letter) is True
