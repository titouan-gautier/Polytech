import pytest

from tests.conftest import import_stuff

import_stuff('unionfind')

# beurk!
from tests.conftest import *


@pytest.mark.key("e8q3")
class TestUnionFindNew:
    def test_unionfind_struct(self):
        try:
            UnionFind()
        except NotImplementedError as e:
            assert False, e
        except TypeError:
            assert True

    def test_unionfind_new(self, dsize):
        uf = uf_new(dsize)
        assert isinstance(uf, UnionFind)


@pytest.mark.key("e8q4")
class TestUnionFindSize:
    def test_unionfind_size(self, dsize):
        uf = uf_new(dsize)
        assert uf_size(uf) == dsize


@pytest.mark.key("e8q5")
class TestUnionFindFindUnion:

    def test_unionfind_find(self, dsize):
        uf = uf_new(dsize)
        for i in range(dsize):
            assert uf_find(uf, i) == i

    def test_unionfind_union(self, dsize):
        uf = uf_new(dsize)
        for i in range(dsize - 1):
            uf = uf_union(uf, i, i + 1)
        for i in range(dsize):
            assert uf_find(uf, i) == 0
