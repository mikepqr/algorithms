import pytest
import hypothesis.strategies as st
from hypothesis import given

import mult


@given(st.integers(), st.integers())
def test_splitnums_rebuild(x, y):
    if x < 2 or y < 2:
        with pytest.raises(ValueError):
            mult.splitnums(x, y)
    else:
        xl, xr, yl, yr, n = mult.splitnums(x, y)
        assert (xl << n) + xr == x
        assert (yl << n) + yr == y


@given(st.integers(), st.integers())
def test_multiply(x, y):
    assert mult.mult(x, y) == x * y
