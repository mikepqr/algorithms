import math
import pytest
import hypothesis.strategies as st
from hypothesis import given

import arithmetic


@given(st.integers(), st.integers())
def test_mult(x, y):
    assert arithmetic.mult(x, y) == x * y


@given(st.integers())
def test_square(x):
    assert arithmetic.square(x) == x**2


@given(st.integers(), st.integers())
def test_div(x, y):
    q, r = arithmetic.div(x, y)
    if y == 0:
        assert q == 0
        assert r == x
    else:
        assert q == x // y
        assert r == x % y


@given(st.integers(), st.integers())
def test_mod(x, N):
    xmodN = arithmetic.mod(x, N)
    if N == 0:
        assert xmodN == x
    else:
        assert xmodN == x % N


@given(st.integers(), st.integers())
def test_quotient(x, N):
    xmodN = arithmetic.quotient(x, N)
    if N == 0:
        assert xmodN == 0
    else:
        assert xmodN == x // N


@given(st.integers(min_value=-100, max_value=100),
       st.integers(min_value=0, max_value=100),
       st.integers())
def test_modexp(x, y, N):
    xyN = arithmetic.modexp(x, y, N)
    if N == 0:
        assert xyN == (x**y)
    else:
        assert xyN == (x**y) % N


@given(st.integers(), st.integers())
def test_gcd(a, b):
    assert arithmetic.gcd(a, b) == math.gcd(a, b)


@given(st.integers(), st.integers())
def test_egcd(a, b):
    x, y, d = arithmetic.egcd(a, b)
    assert d == math.gcd(a, b)
    assert a*x + b*y == d


@given(st.integers(), st.integers())
def test_multinv(a, N):
    if a == 0 or N <= 1:
        with pytest.raises(ValueError):
            arithmetic.multinv(a, N)
    elif arithmetic.gcd(a, N) != 1:
        with pytest.raises(ValueError):
            arithmetic.multinv(a, N)
    else:
        assert (arithmetic.multinv(a, N) * a) % N == 1


@given(st.integers(max_value=100000))
def test_prime(N):
    if arithmetic.prime(N):
        assert all(N % i for i in range(2, math.ceil(math.sqrt(N))))
