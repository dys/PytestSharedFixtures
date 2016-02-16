"""These tests contain example usage (and actual testing) of the POC for pytest fixture wrappers.

This solution is intended to allow us to use our libraries as pytest fixtures or regular imports with a similar interface.
"""
import libraries

def test_library_as_fixture(library_one):
    l1 = library_one()
    assert l1.config == "default"

def test_library_as_import():
    l1 = libraries.library_one.library_one()
    assert l1.config == "default"

def test_library_from_cli():
    cmd = 'python -c "from libraries.library_one import library_one; print library_one().config"'
    from subprocess import check_output
    config = check_output(cmd, shell=True).rstrip()
    assert config == "default"

def test_fixture_is_global():
    a = libraries.fixtures.library_one()
    b = libraries.fixtures.library_one()
    assert a is b

def test_fixture_dependency(library_two):
    l2 = library_two()
    assert l2.l1.config == "default"

def test_config_fixture_dependency(library_one, library_two):
    l1 = library_one()
    l1.config = "changed"
    l2 = library_two()
    assert l2.l1.config == "changed"
