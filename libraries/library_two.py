class LibraryTwo():
    def __init__(self, config="default"):
        self.config = config

def library_two(*args, **kwargs):
    return LibraryTwo(*args, **kwargs)
