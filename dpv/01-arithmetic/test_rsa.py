import hypothesis.strategies as st
from hypothesis import given

import rsa
public, private = rsa.keypair()  # to use for encode/decode test


@given(st.text(max_size=8))
def test_encode_decode(s):
    assert rsa.decode(rsa.encode(s, public), private) == s
