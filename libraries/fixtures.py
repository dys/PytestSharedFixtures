from functools import wraps

def global_fixture(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        name = '_' + cls.__class__.__name__
        try:
            return globals()[name]
        except KeyError:
            globals()[name] = cls(*args, **kwargs)
            return globals()[name]
    return wrapper
