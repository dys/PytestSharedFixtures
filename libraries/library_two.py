class LibraryTwo():
    def __init__(self, config="default"):
        self.config = config

def library_two(*args, **kwargs):
    global _library_two
    try:
        return _library_two
    except NameError:
        _library_two = LibraryTwo(*args, **kwargs)
        return _library_two
