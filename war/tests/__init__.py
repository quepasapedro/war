import functools
import pdb
import sys


def debug_on(*exceptions):
    """
    Decorator which triggers debugger to start upon a test failure in
    a specific unit test. Recommended to remove calls to this decorator
    before releasing code.
    """

    if not exceptions:
        exceptions = (AssertionError, )

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except exceptions:
                pdb.post_mortem(sys.exc_info()[2])
        return wrapper
    return decorator
