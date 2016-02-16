class LibraryOne(object):
    def __init__(self, config="default"):
        self.config = config

def library_one(*args, **kwargs):
    global _library_one
    try:
        return _library_one
    except NameError:
        _library_one = LibraryOne(*args, **kwargs)
        return _library_one
