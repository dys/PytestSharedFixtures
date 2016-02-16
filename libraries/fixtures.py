import pytest

@pytest.fixture
def library_one():
    from libraries.library_one import library_one as builder
    return builder

@pytest.fixture
def library_two():
    from libraries.library_two import library_two as builder
    return builder
