import pytest
import  sample as m

def test_add():
    result = m.add(2, 3)
    assert result == 5

test_add()