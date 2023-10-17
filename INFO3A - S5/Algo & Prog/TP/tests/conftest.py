import pytest
import random
from pathlib import Path
from .setup import TP_STRUCTURE, TP_CLASS
import dataclasses as dc
import importlib

collect_ignore = []
for tp_class in TP_CLASS.values():
    try:
        module = importlib.import_module(tp_class['module'])
        if dc.is_dataclass(getattr(module, tp_class['class'])):
            collect_ignore.append(tp_class['test_class'])
        else:
            collect_ignore.append(tp_class['test_dataclass'])

    except (ImportError, AttributeError):
        collect_ignore.append(tp_class['test_class'])


def _add_preceding_tests(tp, key):
    keynames = []
    i, tp_struct = None, None
    try:
        tp_struct = TP_STRUCTURE[tp]  # prone to KeyError
        i = tp_struct.index(key)  # prone to ValueError
    except KeyError:
        print(f"\n*** Unknown TP value {tp!s} ***")
    except ValueError:
        print(f"\n*** Unknown key {key!r} for {tp} ***")
    if i is not None:
        keynames = tp_struct[:i + 1]
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


def fake_function(*args):
    raise NotImplementedError(f"Not found")


class FakeStruct:
    __post_init__ = fake_function


##################################################################################
# Fixture definitions
##################################################################################
DELTA_SIZES = [0, 1, 9, 99, 999]
INPUT_LISTS = [[42],
               list(range(1, 6)),
               [random.randint(0, 100) for _ in range(10)],
               [random.randint(0, 100) for _ in range(100)]]
               #[random.randint(0, 100) for _ in range(1_000)]]
EMPTY_LISTS = [None, []]
INPUT_LISTS_WITH_NULL = EMPTY_LISTS + INPUT_LISTS


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
