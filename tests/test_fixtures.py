"""These tests contain example usage (and actual testing) of the POC for pytest fixture wrappers.

This solution is intended to allow us to use our libraries as pytest fixtures or regular imports with a similar interface.
"""
import libraries

def test_library_as_fixture(library_one):
    l1 = library_one()
    assert l1.config == "default"

def test_library_as_import():
    l1 = libraries.library_one.library_one()
    print l1
    assert l1.config == "default"

def test_library_from_cli():
    cmd = """python -c 'from libraries.library_one import library_one
l1 = library_one()
print l1.config'
"""
    from subprocess import check_output
    config = check_output(cmd, shell=True).rstrip()
    assert config == "default"

def test_fixture_is_global():
    # about ()(): library_one() actually returns a wrapper, so we call the wrapper()
    # this is not normal usage: use one of the above 3 methods instead
    a = libraries.fixtures.library_one()()
    b = libraries.fixtures.library_one()()
    assert a is b
