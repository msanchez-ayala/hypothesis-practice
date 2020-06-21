import pytest
from hypothesis import given, example
from hypothesis.strategies import text
from functions import encode, decode

@given(text())    # Tests wide range of text data
@example("")      # Makes sure "" is always tested
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s