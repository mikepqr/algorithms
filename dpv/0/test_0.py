import pytest
from hypothesis import given
import hypothesis.strategies as st

import ex03
import expsq
import fib


def test_fib1_fib3_agree():
    for i in range(1000):
        assert fib.fib1(i) == fib.fib3(i)


@given(st.integers())
def test_expsq_integers_0(x):
    assert expsq.expsq(x, 0) == 1


@given(st.integers(), st.integers(min_value=0, max_value=100))
def test_expsq_python_agree(x, n):
    assert expsq.expsq(x, n) == x**n


def test_ex03b():
    assert not ex03.ex03b(0)
    assert not ex03.ex03b(0.69)
    assert ex03.ex03b(0.8)
    assert ex03.ex03b(1)
