import functools
import pdb
import sys


def debug_on(*exceptions):
    """
    Decorator which triggers debugger to start upon a test failure in
    a specific unit test. Recommended to remove before releasing code.

    To use, import this as a method from the tests module, and then
    place a line above a unit test function like this:

        class YourTestCase(unittest.TestCase):
            @debug_on()
            def test_your_code(self):
                raise Exception('Debug here ...')
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
