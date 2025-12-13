import sys
import os
PROJECT_ROOT = r"C:\\Users\\Andrew\\HiGIT\\python_labs"
sys.path.insert(0, PROJECT_ROOT)
import pytest
from src.lab03.umbapumpa import *

@pytest.mark.parametrize(
    "n, expected",
    [
        ("ПрИвЕт \nМИр \t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello \r \nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(n, expected):
    assert normalize(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        ("hello,world!!!", ["hello", "world"]),
        ("это по-настоящему круто", ["это", "по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize_basic(n, expected):
    assert tokenize(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (["a","b","a","c","b","a"], {"a":3,"b":2,"c":1}),
        (["bb","aa","bb","aa","cc"], {"aa":2,"bb":2,"cc":1}),
    ],
)
def test_count_freq(n, expected):
    assert count_freq(n) == expected


@pytest.mark.parametrize(
    "n, b, expected",
    [
        (["a","b","a","c","b","a"], 2, [("a", 3), ("b", 2)]),
        (["bb","aa","bb","aa","cc"], 5, [("aa",2), ("bb",2), ("cc",1)]),
    ],
)
def test_top_n(n, b, expected):
    assert top_n(n, b) == expected
