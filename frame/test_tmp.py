import importlib
import re


def test_tmp():
    print(re.search("ab", "abcd"))
    func = importlib.import_module("hello")
    getattr(func,'a')()