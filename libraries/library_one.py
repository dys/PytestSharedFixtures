from libraries.fixtures import global_fixture

class LibraryOne():
    def __init__(self, config="default"):
        self.config = config

import pytest
@pytest.fixture
def library_one(*args, **kwargs):
    return global_fixture(LibraryOne)
