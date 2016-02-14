class LibraryOne(object):
    def __init__(self, config="default"):
        self.config = config

def library_one(*args, **kwargs):
    return LibraryOne(*args, **kwargs)
