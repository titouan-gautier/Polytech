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
        hs = hs_new(char_list)
        assert isinstance(hs, HashSet)

    def test_hashset_is_empty(self, char_list):
        hs = hs_new(char_list)
        if len(char_list) == 0:
            assert hs_is_empty(hs) is True
        else:
            assert hs_is_empty(hs) is False

    def test_hashset_size(self, char_list):
        hs = hs_new(char_list)
        assert hs_size(hs) == len(char_list)

    def test_hashset_member(self, char_list):
        hs = hs_new(char_list)
        for letter in char_list:
            assert hs_member(hs, letter) is True
        assert hs_member(hs, 'Z') is False

    def test_hashset_iterate(self, char_list):
        hs = hs_new(char_list)
        for letter in hs_iterate(hs):
            assert letter in char_list

    def test_hashset_insert(self, char_list):
        hs = hs_new()
        for letter in char_list:
            hs_insert(hs, letter)
        for letter in char_list:
            assert hs_member(hs, letter) is True

    def test_hashset_delete(self, char_list):
        hs = hs_new(char_list)
        for letter in char_list:
            hs_delete(hs, letter)
        assert hs_size(hs) == 0

    def test_hashset_union(self, char_list, char_list2):
        hs = hs_new(char_list)
        hs2 = hs_new(char_list2)
        hsboth = hs_union(hs, hs2)
        for letter in char_list:
            assert hs_member(hsboth, letter) is True
        for letter in char_list2:
            assert hs_member(hsboth, letter) is True

    def test_hashset_intersection(self, char_list, char_list2):
        hs = hs_new(char_list)
        hs2 = hs_new(char_list2)
        hsboth = hs_intersection(hs, hs2)
        for letter in char_list:
            if letter in char_list2:
                assert hs_member(hsboth, letter) is True
            else:
                assert hs_member(hsboth, letter) is False

    def test_hashset_difference(self, char_list, char_list2):
        hs = hs_new(char_list)
        hs2 = hs_new(char_list2)
        hsboth = hs_difference(hs, hs2)
        for letter in char_list:
            if letter in char_list2:
                assert hs_member(hsboth, letter) is False
            else:
                assert hs_member(hsboth, letter) is True