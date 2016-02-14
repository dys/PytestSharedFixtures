def test_library_as_fixture(library_one):
    l1 = library_one()
    assert l1.config is "default"

def test_library_as_library():
    from libraries.library_one import library_one
    l1 = library_one()
    assert l1.config is "default"
