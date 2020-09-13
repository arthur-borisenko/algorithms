from io import StringIO
import sys


def console_test(in_text, test_call, test_assert):
    orig_out = sys.stdout
    orig_in = sys.stdin
    out = StringIO()
    sys.stdout = out
    sys.stdin = StringIO(in_text)
    test_call()
    test_assert(out.getvalue())
    sys.stdout = orig_out
    sys.stdin = orig_in
