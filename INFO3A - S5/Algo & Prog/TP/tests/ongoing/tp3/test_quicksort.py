try:
    from tp3.sorts import quicksort
except ImportError:
    if 'quicksort' not in globals():
        def quicksort(l): pass
try:
    from tp3.arraylist import al_new, al_get
except ImportError:
    if 'al_new' not in globals():
        def al_new(size, l): pass
    if 'al_get' not in globals():
        def al_get(al, i): pass

import pytest


@pytest.mark.key("e7q1")
class TestQuicksort:

    def test_quicksort(self, input_list_with_null):
        l = input_list_with_null  # alias
        size = 0 if l is None else len(l)
        al = al_new(size, l)

        quicksort(al)
        l = l or []
        l.sort()
        assert all(al_get(al, i) == l[i] for i in range(len(l)))