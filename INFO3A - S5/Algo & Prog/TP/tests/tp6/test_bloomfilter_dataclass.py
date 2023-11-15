import pytest

from tests.conftest import import_stuff

import_stuff('bloomfilter')

# beurk!
from tests.conftest import *


@pytest.mark.key("e6q1")
class TestBloomFilter:
    def test_bloomfilter_struct(self):
        try:
            BloomFilter()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_bloomfilter_new(self):
        bf = bf_new(16)
        assert isinstance(bf, BloomFilter)

    def test_bloomfilter_insert_lookup(self, char_list):
        bf = bf_new(16)
        for letter in char_list:
            bf_insert(bf, letter)
            assert bf_lookup(bf, letter) is True
        assert bf_lookup(bf, 'Z') is False
