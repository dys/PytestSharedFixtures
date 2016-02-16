import pytest
import functools

def make_global(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        name = '_' + cls.__class__.__name__
        try:
            return globals()[name]
        except KeyError:
            globals()[name] = cls(*args, **kwargs)
            return globals()[name]
    return wrapper

@pytest.fixture
def library_one():
    from libraries.library_one import library_one as wrapper
    return wrapper

@pytest.fixture
def library_two():
    from libraries.library_two import library_two as wrapper
    return wrapper
