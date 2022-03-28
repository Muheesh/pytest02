import area
import pytest
@pytest.mark.area
def test_areasqr():
    a = 5
    result = area.area_square(a)
    assert result == a*a
@pytest.mark.area
def test_arearec():
    a = 4
    b = 8
    result = area.area_rec(a,b)
    assert result == a*b
@pytest.mark.perimeter
def test_peri():
    a = 78
    b = 8
    result = area.peri_rec(a,b)
    assert result == 2*(a+b)