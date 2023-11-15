import pytest
import random
from pathlib import Path
import dataclasses as dc
import importlib
import string

#importlib.invalidate_caches()

from .setup import TP_QUESTIONS, TP_DATA_STRUCTURES

collect_ignore = []
for struct in TP_DATA_STRUCTURES.values():
    try:
        module = importlib.import_module(struct['module'])
        if dc.is_dataclass(getattr(module, struct['classnames'][0])):
            collect_ignore.append(struct['test_class'])
        else:
            collect_ignore.append(struct['test_dataclass'])

    except (ImportError, AttributeError):
        collect_ignore.append(struct['test_class'])


def _add_preceding_tests(tp, key):
    keynames = []
    i, tp_q = None, None
    try:
        tp_q = TP_QUESTIONS[tp]  # prone to KeyError
        i = tp_q.index(key)  # prone to ValueError
    except KeyError:
        print(f"\n*** Unknown TP value {tp!s} ***")
    except ValueError:
        print(f"\n*** Unknown key {key!r} for {tp} ***")
    if i is not None:
        keynames = tp_q[:i + 1]
    return keynames


def pytest_collection_modifyitems(config, items):
    # check path to a given TP
    tp = None
    for arg in config.invocation_params.args:
        path = Path(config.invocation_params.dir).joinpath(arg)
        if path.is_dir():
            tp = path.name
            break
    # check if there is an option like --key=e4q3
    filter = config.getoption("--key")
    # check combination of TP and filter
    if tp and filter:  # run tests of the given TP up to the filter question
        keynames = ['global'] + _add_preceding_tests(tp, filter)
        for item in items:
            mark = item.get_closest_marker("key")
            if mark and mark.args and mark.args[0] not in keynames:
                item.add_marker(pytest.mark.skip(reason="Not yet implemented"))

    elif filter == 'global' and not tp:  # run only global tests (w/o recursive search in the tests/ dir)
        new_items = []
        for item in items:
            mark = item.get_closest_marker("key")
            if mark and mark.args and mark.args[0] == "global":
                new_items.append(item)
        items[:] = new_items

    elif filter and not tp:  # skip all tests since no tp was specified
        items[:] = []
        print(f"\n*** Missing TP directory (like tests/tp1) although Key {filter} was given. ***")

    else:  # recursively run all tests
        pass


def pytest_configure(config):
    # register our new marker to avoid warnings
    config.addinivalue_line(
        "markers",
        "key(question): specify a test key for a given question"
    )


def pytest_addoption(parser):
    # add your new filter option (you can name it whatever you want)
    parser.addoption('--key', action='store', help="only run tests matching the key.")


# def pytest_runtest_setup(item):
#     if item.config.getoption("--key") is None:
#         return
#     keynames = [mark.args[0] for mark in item.iter_markers(name="key")]
#     if keynames:
#         testnames = ['global'] + _add_subsequent_tests(keynames)
#
#         if item.config.getoption("--key") not in testnames:
#             pytest.skip("Not yet implemented")
#     else:
#         pytest.skip("Undefined test key")


##################################################################################
# Helper definitions
##################################################################################

def fake_function(*args):
    raise NotImplementedError(f"Not found")


class FakeStruct:
    __post_init__ = fake_function


def import_stuff(key):
    module_name = TP_DATA_STRUCTURES[key]['module']
    classnames = TP_DATA_STRUCTURES[key]['classnames']
    funcnames = TP_DATA_STRUCTURES[key]['funcnames']


    try:
        module = importlib.import_module(module_name)     # may raise ImportError
        dataclass: bool = dc.is_dataclass(getattr(module, classnames[0]))
        names = (classnames + funcnames) if dataclass else classnames
        for name in names:
            if not hasattr(module, name):
                if name in classnames:
                    setattr(module, name, FakeStruct)
                else:
                    setattr(module, name, fake_function)
            # it is then "safe" to expose the student's code
            cls = getattr(module, name)
            globals()[name] = cls

            if not dataclass:
                # aliases for the student's code
                if hasattr(cls, 'str') and not hasattr(cls, '__str__'):
                    setattr(cls, '__str__', lambda self: self.str())
                if hasattr(cls, 'len') and not hasattr(cls, '__len__'):
                    setattr(cls, '__len__', lambda self: self.len())
                if hasattr(cls, 'size') and not hasattr(cls, '__len__'):
                    setattr(cls, '__len__', lambda self: self.size())
                if hasattr(cls, 'get') and not hasattr(cls, '__getitem__'):
                    setattr(cls, '__getitem__', lambda self, i: self.get())
                if hasattr(cls, 'set') and not hasattr(cls, '__setitem__'):
                    setattr(cls, '__setitem__', lambda self, i, item: self.set(i, item))
                if hasattr(cls, 'put') and not hasattr(cls, '__setitem__'):
                    setattr(cls, '__setitem__', lambda self, i, item: self.put(i, item))
                if hasattr(cls, 'iter_cells') and not hasattr(cls, '__iter__'):
                    setattr(cls, '__iter__', lambda self: self.iter_cells())
                if hasattr(cls, 'reversed_iter_cells') and not hasattr(cls, '__reversed__'):
                    setattr(cls, '__reversed__', lambda self: self.reversed_iter_cells())
                if hasattr(cls, 'equal') and not hasattr(cls, '__eq__'):
                    setattr(cls, '__eq__', lambda self: self.equal())

    except ImportError:
        pass


##################################################################################
# Fixture definitions
##################################################################################
DELTA_SIZES = [0, 1, 9, 99]
INPUT_LISTS = [[42], [42] * 10,
               list(range(1, 6)),
               [random.randint(0, 100) for _ in range(10)],
               [random.randint(0, 100) for _ in range(100)]]
# random letter lists
CHAR_LISTS = [['a'], [''.join(random.choices(string.ascii_lowercase, k=50)) for _ in range(6)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(10)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(100)]]

CHAR_LISTS2 = [['a'], [''.join(random.choices(string.ascii_lowercase, k=50)) for _ in range(6)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(10)],
                [''.join(random.choices(string.ascii_lowercase, k=50))  for _ in range(100)]]
for i, letter_list in enumerate(CHAR_LISTS):
    CHAR_LISTS[i] = list(set(letter_list))

for i, letter_list2 in enumerate(CHAR_LISTS2):
    CHAR_LISTS2[i] = list(set(letter_list2))

EMPTY_LISTS = [None, []]
INPUT_LISTS_WITH_NULL = EMPTY_LISTS + INPUT_LISTS

INPUT_DUP_TREES = [[1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 2, 2, 3, 3, 4, 4],
        [42, 42, None, 42, None, None, None, 42, None, None, None, None, None, None, None, 42, None, None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, 42]]
INPUT_UNIQUE_TREES = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2, 1, 4, 0, None, 3, 5],
              [1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5, None, None, None, None,
               None, None, None, None, None, None, None, None, None, None, None, 6],
              [6, 4, 5, 2, 1, 9, 7, 3, 0, 11, 12], [6, 4, 5, 2, None, 9, 7, 3, 0, None, None, 11, 12],
               list(range(2 ** 6 + 1))]
INPUT_TREES = INPUT_DUP_TREES + INPUT_UNIQUE_TREES

EMPTY_TREES = [None, []]
INPUT_TREES_WITH_NULL = EMPTY_TREES + INPUT_TREES

INPUT_ORDERED_TREES = [[1], [1, 1], [2, 1], [1, None, 2], [2, 1, 3],
                       [42, 42, None, 42, None, None, None, 42, None, None, None, None, None, None, None, 42],
                       [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4,
                        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5],
                       [6, 2, 11, 1, 4, 7, 12, None, None, 3, None, None, None, 12, 14],
                       [6, 6, 11, 6, None, 11, 12, 6, None, None, None, 11, None, 12, 14, 6],
                       ]


@pytest.fixture
def random_list_of_10():
    return [random.randint(0, 100) for _ in range(10)]


# workaround to return multiple values from a fixture
# @pytest.fixture
# def input_list(list_of_5, random_list_of_10, random_list_of_100, random_list_of_1000):
#     def _input_list():
#         yield list_of_5
#         yield random_list_of_10
#         yield random_list_of_100
#         yield random_list_of_1000
#     return _input_list


# much better workaround to return multiple values from a fixture
# request is itself a built-in fixture
# waiting for pytest to allow fixture as parameters
@pytest.fixture(params=INPUT_LISTS)
def input_list(request):
    return request.param


# same workaround as above
@pytest.fixture(params=DELTA_SIZES)
def dsize(request):
    return request.param


@pytest.fixture(params=EMPTY_LISTS)
def empty_list(request):
    return request.param


@pytest.fixture(params=INPUT_LISTS_WITH_NULL)
def input_list_with_null(request):
    return request.param


@pytest.fixture(params=EMPTY_TREES)
def empty_tree(request):
    return request.param


@pytest.fixture(params=INPUT_TREES)
def input_tree(request):
    return request.param


@pytest.fixture(params=INPUT_UNIQUE_TREES)
def input_unique_tree(request):
    return request.param


@pytest.fixture(params=INPUT_TREES_WITH_NULL)
def input_tree_with_null(request):
    return request.param


@pytest.fixture(params=INPUT_ORDERED_TREES)
def input_ordered_tree(request):
    return request.param


@pytest.fixture(params=CHAR_LISTS)
def char_list(request):
    return request.param


@pytest.fixture(params=CHAR_LISTS2)
def char_list2(request):
    return request.param

