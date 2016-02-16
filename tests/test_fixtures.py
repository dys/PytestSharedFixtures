"""
A shared fixture is a python class that can be used normally and as a pytest fixture, and may depend on another fixture.

    # As a fixture in a testcase:
    def test_func(shared_fixture):

    # As a regular import from another library:
    from libraries import shared_fixture
    l = shared_fixture()

Users may want to configure one fixture before it is used by another fixture.
This means we can't initialize fixtures before they've been pulled into a
testcase.

To solve this, the shared fixture has a method to get a singleton instance:

    # shared_fixture.py
    class SharedFixture(): # a typical class
    def shared_fixture(): # returns singleton of SharedFixture

And a matching pytest fixture is defined which calls this method:

    # fixtures.py
    @pytest.fixture
    def shared_fixture(): # returns shared_fixture.py:shared_fixture()

Other fixtures call this to get the shared fixture. If the shared fixture is
not yet initialized they'll get one with defaults: otherwise, they'll get the
existing one:

    # Here we configure shared_fixture before other_fixture gets it
    def test_func(shared_fixture, other_fixture):
        sf = shared_fixture()
        sf.option = "new_opt"
        of = other_fixture()
        assert of.sf.option == "new_opt" # other_fixture has a reference to shared_fixture

    # This would use the default shared_fixture instead:
    def test_func(other_fixture):
        of = other_fixture()
        assert of.sf.option == "default"
"""
import libraries

def test_library_as_fixture(library_one):
    l1 = library_one()
    assert l1.config == "default"

def test_library_as_import():
    l1 = libraries.library_one.library_one()
    assert l1.config == "default"

def test_fixture_is_global(library_one):
    a = library_one()
    b = libraries.library_one.library_one()
    assert a is b

def test_default_fixture_dependency(library_two):
    l2 = library_two()
    assert l2.l1.config == "default"

def test_configured_fixture_dependency(library_one, library_two):
    l1 = library_one()
    l1.config = "changed"
    l2 = library_two()
    assert l2.l1.config == "changed"
